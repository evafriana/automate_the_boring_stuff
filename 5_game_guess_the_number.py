# This is a guess the number game
import random

print ('hello what is your name ')
name = input()

print('Well, {}, I am thingking of a number beetween 1 and 20. take a guess.'.format(name))
result = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('take a guess.')
    guess = int(input())

    if guess < result:
        print('your guess is too low')
    elif guess > result:
        print('Your guess is too high')
    else:
        break # This condition is for correct guess!
    
if guess == result:
    print('Good job, {}! you guessed my number in {} guesses.'.format(name, str(guessesTaken)))
else:
    print('Nope. the number i was thingking of was {}'.format(guess))


