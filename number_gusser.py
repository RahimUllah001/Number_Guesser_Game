import random

range_top = input("the number of your choice")

if range_top.isdigit():
    range_top =  int(range_top)

   
    if range_top < 0:
        print("plz enter a number greater tha zero")
        quit()
else:
    print(" plz enter a number next time")
    quit()

random_number = random.randint(0,range_top)

guessess = 0

while True:
    guessess += 1 
    guess_number = input("take a guess_number ")
    if guess_number.isdigit():
        guess_number =  int(guess_number)
    else:
        print("type a number next time")

    if guess_number == random_number:
        print("you  got it ")
        break
    
    elif guess_number > random_number:
        print("u are above the number")
    else:
        print("u are below the numebr")    
       
print("the nubmebr of gusses", guessess)