import random
num = random.randint(1,100)
print("Guess the number between 1 to 100")

guess = 0
while(guess!=num):
    guess = int(input("\nEnter your number : "))
    if(guess>num):
        print("Your number is big...")
    elif(guess<num):
        print("Your number is small...")
    else:
        print("Congratulation you got the number : ",num)         