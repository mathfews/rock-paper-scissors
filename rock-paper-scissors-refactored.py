import colorama, time, random
from colorama import Style, Back, Fore, init
init(autoreset=True)
playerScore = 0
computerScore = 0
def wait(num):
    if num == 1:
        time.sleep(0.5)
    elif num == 2:
        time.sleep(1)
    else:
        print("None!")

def foreBright(color, text, noStyleText=None):
    color = color.upper()
    if noStyleText is None:
        return f"{getattr(Fore, color)}{Style.BRIGHT}{text}{Style.RESET_ALL}"
    else:
        return f"{getattr(Fore, color)}{Style.BRIGHT}{text}{Style.RESET_ALL}{noStyleText}"


def scoreboard(playerScore=0,computerScore=0):
    scoreboard = f"""
          ╔════════════════╗
          ║   {foreBright("YELLOW", "SCOREBOARD")}   ║
          ╚════════════════╝
          Player :  {foreBright("YELLOW", playerScore)}
          Computer:  {foreBright("YELLOW", computerScore)}
          """
    return scoreboard

def ask(text):
    while True:
        ask = input(text).lower()
        if ask == "y" or ask == "s" or ask == "yes" or ask == "sim":
            return True
        if ask == "n" or ask == "n" or ask == "no" or ask == "não":
            return False

def discoverAbreviations(abbreviation):
    abbreviationLower = abbreviation.lower()
    if abbreviation == "y":
        return "yes"
    elif abbreviationLower == "e":
        return "easy"
    elif abbreviationLower == "n":
        return "normal"
    elif abbreviationLower == "i":
        return "impossible"
    elif abbreviationLower == "r":
        return "rock"
    elif abbreviationLower == "s":
        return "scissors"
    elif abbreviationLower == "p":
        return "paper"
    else:
        return abbreviation

options = ["rock", "paper", "scissors", "r", "p", "s"]

print(foreBright("YELLOW", "# Rock, Paper and scissors", ""))

rules = [foreBright("YELLOW", "Rock beats scissors", " by smashing them"), foreBright("YELLOW", "Scissors beats paper", " by cutting it"), foreBright("YELLOW", "Paper beats rock", " by covering it")]

levels = ["Easy(E)", "Normal(N)", "Impossible(I)", "e", "n", "i", "easy", "normal", "impossible"]


def showRules():
    while True:
        for rule in rules:
            print(f"* {rule}")
            wait(2)
        if ask("Did you understand the rules? (y/n) "):
            break

def selectLevel():
    print("Select difficulty: ")
    for level in levels:
        if len(level) > 1: 
            if level == "Impossible(I)":
                print(f"* {foreBright("RED", level)}")
            else:
                print(f"* {level}")
        else:
            break
        wait(1)
    level = input("> ").lower()
    if level in levels:
        if discoverAbreviations(level) == "impossible":
            print(f"You choose {foreBright("RED", discoverAbreviations(level))}")
        else:
            print(f"You choose {foreBright("YELLOW", discoverAbreviations(level))}")
    else:
        selectLevel()
    return level

def play():
    while True: 
        messages = ["So, let's play! ...", "Rock", "Paper", "Scissors", "Shoot!"]
        for message in messages:
            print(message)
            wait(2)
        playerChoose = input("> ").lower()
        if playerChoose in options:
            return playerChoose

def rockPaperScissors(_playerChoose, level):
    global playerScore, computerScore
    def beat(_playerChoose):
        if _playerChoose == "paper" or _playerChoose == "p":
            win = ["scissors", "s"]
            lose = ["rock", "r"]
        if _playerChoose == "rock" or _playerChoose == "r":
            win = ["paper", "p"]
            lose = ["scissors", "s"]
        if _playerChoose == "scissors" or _playerChoose == "s":
            win = ["rock", "s"]
            lose = ["paper", "p"]
        return win, lose
    win, lose = beat(_playerChoose)
    def difficulty(_level):
        if discoverAbreviations(_level) == "easy":
            print(lose[0])
            computerChoose = lose[0]
        elif discoverAbreviations(_level) == "normal":
            computerChoose = random.choice(options)
        elif discoverAbreviations(_level) == "impossible":
            print(win[0])
            computerChoose = win[0]
        return computerChoose
    computerChoose = difficulty(level)
    if computerChoose in win:
        print(f"{foreBright("yellow", "You lose, ", "I choose ")}{foreBright("yellow", discoverAbreviations(computerChoose))}!")
        computerScore += 1
    elif computerChoose not in win and computerChoose is not _playerChoose and computerChoose is not _playerChoose:
        print(f"{foreBright("yellow", "You won, ", "I choose ")}{foreBright("yellow", discoverAbreviations(computerChoose))}!")
        playerScore += 1
    elif computerChoose is _playerChoose:
        print(f"{foreBright("yellow", "Draw, ", "I choose ")}I choose{foreBright("yellow", discoverAbreviations(computerChoose))} too!")
        playerScore += 1
        computerScore += 1
    return playerScore, computerScore
def playAgain():
    while True:
        again = ask("Do you want to play again?(y/n) ")
        if again:
            level = selectLevel()
            print("------------------------")
            playerChoose = play()
            rockPaperScissors(playerChoose, level)
            playAgain()
        elif again is False:
            while True:
                showScoreboard = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
                if showScoreboard is True:
                    print(scoreboard(playerScore, computerScore))
                print("Thanks for playing!")
                while True:
                    exit = input("Press ENTER to exit...")
                    if exit == "":
                        quit()
""" if ask("Do you want to see the rules?(y/n) "):
    showRules()
print("------------------------")
wait(1) """
level = selectLevel()
print("------------------------")
playerChoose = play()
rockPaperScissors(playerChoose, level)
playAgain()