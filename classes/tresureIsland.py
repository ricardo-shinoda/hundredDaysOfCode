print('''             _ _             
            (_) |            
  __ _ _   _ _| |_ __ _ _ __ 
 / _` | | | | | __/ _` | '__|
| (_| | |_| | | || (_| | |   
 \__, |\__,_|_|\__\__,_|_|   
  __/ |                      
 |___/ 
      ''')

gameOver = "Game Over..."

print("Welcome to the Guitar Disneyland! Your missing is to find the guitar!\n")

direction = input("Do you want to go left or right?\n").lower()


if direction == 'left':
    swim = input("Do you want to swim or wait?\n").lower()
    if swim == "wait":
        door = input("Which door do you pick? Blue, Yellow or Red?\n").lower()
        if door == "yellow":
            print("You win!")
        else:
            print(gameOver)
    else:
        print(gameOver)
else:
    print(gameOver)
