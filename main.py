'''We are going to write a program that generates a random number and asks the user to guess it.

if the player's hues is higher then the actual number , the program displays "Lowernumber plz" 
Similarly if the user's huess is too low , the program prints "higher number plz " 
When theuser huesses the correct number , the program displays the number of gusses the play used to arrive at the number 

Hint : use the random module '''



import random 
n = random.randint(1 , 100)
a = -1
guesses = 1 
while (a !=n):
    a = int(input("Guess the number ?"))
    if (a > n):
        print("Lower number Please !")
        guesses +=1
    elif (a <n):
        print("Higher Number Please !")
        guesses +=1 

print(f"You have guesses the number {n} correctly in {guesses} attempts !")