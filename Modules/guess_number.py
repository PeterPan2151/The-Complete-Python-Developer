import random
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
random_number = random.randint(start, end)
while True:
    print(random_number)
    user_number = int(input(f"Guess a number between {start} and {end}: "))
    if user_number == random_number:
        print('You guessed it!!')
        break
    else:
        print('Nope, try again')