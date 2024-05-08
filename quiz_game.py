print('Welcome to my computer quiz!')
playing = input('Do you want to play? (y/n) ').lower()

if playing== 'n':
    print('Sorry to see you go...!')
    quit()
elif playing == 'y':
    print('Let\'s begin...!')
else:
    print('Wrong input please only use y or n')


count = 0
total = 5

answer = input('What does CPU stands for? ').lower()
if answer == 'central processing unit':
    print('Correct Answer..!')
    count+=1
else:
    print('Incorrect Answer..!')


answer = input('What does ALU stands for? ').lower()
if answer == 'arithmetic logical unit':
    print('Correct Answer..!')
    count+=1
else:
    print('Incorrect Answer..!')


answer = input('What does LAN stands for? ').lower()
if answer == 'local area network':
    print('Correct Answer..!')
    count+=1
else:
    print('Incorrect Answer..!')


answer = input('What does RAM stands for? ').lower()
if answer == 'random access memory':
    print('Correct Answer..!')
    count+=1
else:
    print('Incorrect Answer..!')


answer = input('What does ROM stands for? ').lower()
if answer == 'read only memory':
    print('Correct Answer..!')
    count+=1
else:
    print('Incorrect Answer..!')

score = round((count/total)*100,2)

if count>=3:
    print(f'You got {count} questions correct.')
    print(f'You total score: {score}') 
    print('Passed the quiz...!')
else:
    print(f'You got {count} questions correct.')
    print(f'You total score: {score}')
    print('Sorry you failed the quiz...!')
