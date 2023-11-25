import random

# 0 - snake 
# 1 - water
# 2 - gun



print("\n\tWelcome to Snake Water Gun Game\n")

userName = input("Enter Your Name : ")
print(f"\nHello {userName.strip()}, see the option from below :- ") # strip() removes before and after string whitespaces
print("0 - Snake\n1 - Water\n2 - Gun\n111 - exit the game")
rounds = int(input("\nplease enter number of rounds you wanna play : "))
print(f"\nThe Game will be of {rounds} rounds\n")
print("The Game Begins :- \n")
# win = [0,1,2][1,2,0]
# lose = [0,1,2][2,0,1]
# draw = [0,1,2][0,1,2]

def userInput():
  try:
    userChoice = int(input("Enter your choice : "))
    return userChoice
  except ValueError:
    print("please enter a valid option from above")
    
    
def computerInput():
  computerChoice = random.randint(1,3)
  return computerChoice

def game():
  userScore = 0
  computerScore = 0
  for i in range(1,rounds+1):
    print(f"\nRound {i}")
    userChoice = userInput()
    computerChoice = computerInput()
  
    
    if userChoice == 0 and computerChoice == 1:
      print(f"{userName} selects snake\nComputer selects water")
      print(f"{userName} wins this round")
      userScore += 1 
      print(f"{userName} : {userScore}\tComputer : {computerScore}")
    elif userChoice == 0 and computerChoice == 0:
      print(f"{userName} selects snake\nComputer selects snake")
      print(f"Round {i} Draw")
      userScore += 0
      print(f"{userName} : {userScore}\tComputer : {computerScore}")
    elif userChoice == 0 and computerChoice == 2:
      print("Computer wins this round")
      computerScore += 1
      print(f"{userName} : {userScore}\nComputer : {computerScore}")
    elif userChoice == 1 and computerChoice == 2:
      print(f"{userName} selects water\nComputer selects gun")
      print(f"{userName} wins this round")
      userScore += 1
      print(f"{userName} : {userScore}\tComputer : {computerScore}")
    elif userChoice == 1 and computerChoice == 1:
      print(f"{userName} selects water\nComputer selects water")
      print(f"Round {i} Draw")
      userScore += 0
      print(f"{userName} : {userScore}\tComputer : {computerScore}") 
    elif userChoice == 1 and computerChoice == 0:
        print("Computer wins this round")
        computerScore += 1
        print(f"{userName} : {userScore}\nComputer : {computerScore}")  
    elif userChoice == 2 and computerChoice == 0:
        print(f"{userName} selects gun\nComputer selects snake")
        print(f"{userName} wins this round")
        userScore += 1
        print(f"{userName} : {userScore}\nComputer : {computerScore}")
    elif userChoice == 2 and computerChoice == 2:
        print(f"{userName} selects gun\nComputer selects gun")
        print(f"Round {i} Draw")
        userScore += 0
        print(f"{userName} : {userScore}\nComputer : {computerScore}")
    elif userChoice == 2 and computerChoice == 1:
        print("Computer wins this round")
        computerScore += 1
        print(f"{userName} : {userScore}\nComputer : {computerScore}")
    elif userChoice == 111:
       print("thank you for playing our game\nplease visit again")
       exit()
    else:
        print("please enter a valid choice")
        game()
  print(f"\t{userName} final score is {userScore}\n\tcomputer final score is {computerScore}")
  if computerScore>userScore:
    print("\n\t\tComputer Wins The Game\n")
  elif computerScore==userScore:
    print("\n\t\tThe Game is Draw\n")
  else:
    print(f"\n\t\tCongratulations to{userName} for winning the game\n")  

     
game()
