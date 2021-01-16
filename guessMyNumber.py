import random
number = random.randrange(0, 100)

score= 0
for i in range(1,20):
    myNumber = int(input("Enter a number: "))

    score += 1


    if number == myNumber:
        print(f"Congratulations! The number is:{number}. Your score: {score} ")
        break
    elif number < myNumber:
        print("Number is too high.Try Again!")
    elif number > myNumber:
        print("Number is too low.Try Again!")
    else:
        print("Too many attempts. You lose!")
