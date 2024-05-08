import random

# print(random.randrange(0,10))
# print(random.randint(0,10))

top_of_range = input('Type a number greater than zero: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
elif int(top_of_range)<=0:
    print('Enter a number greater than zero')
    quit()
else:
    print('Please only enter a number')
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses+=1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please only enter a number')
        continue
    
    if user_guess == random_number:
        print('You got it..!')
        break
    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')

print(f'You got it in {guesses} guesses')