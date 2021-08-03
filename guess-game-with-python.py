import random
choice = input("Which game do you wanna play?\nWord Guess\nNumber Guess\n")
if choice == "Word Guess":
    words = ["Laptop", "Mobile", "Car", "Television"]
    correctWord = random.choice(words)
    userInput = input("\n Which word am I guessing?\n Your Options:\n 1). Laptop\n 2). Mobile\n 3). Car\n 4). Television\n")
    if userInput == correctWord:
        print("\n Congrats! You got it correct! I love playing with ya!")
    elif userInput != correctWord:
        print("\n Wrong! The correct word was",correctWord,"Better luck next time!\n")
    else:
        print("An Error Occured! Cannot continue the game!")
elif choice == "Number Guess":
    minNumber = int(input("\n Enter the minimum number\n"))
    maxNumber = int(input("\n Enter the maximum number\n"))
    number = random.randint(minNumber, maxNumber)
    userNumber = int(input("\n What number am I guessing?\n"))
    if userNumber == number:
        print("\n Congrats! You got it correct! I love playing with ya!")
    elif userNumber != number:
        print("\n Wrong! I was guessing ",number," Better luck next time!\n")
    else:
        print("An Error Occured! Cannot continue the game!")
else:
    print("\n Please make a valid choice!\nWord Guess\nNumber Guess\n")
