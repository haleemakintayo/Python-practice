import random

randnum = random.randint( 1, 100)
attempts = 5
while attempts > 0 : 

    number = int(input('Guess a random number between 1 and 100 : '))

    if number > 100 or number <  0 :
        print('invalid input , ensure you put in value between 1 and 100')
        continue 
    elif number > randnum :
        attempts -= 1
        print(f'Wrong ! your number is higher than the random number , attempts remaining : {attempts} ')
        
    elif number < randnum :
        attempts -= 1   
        print(f'Wrong !! , Your number is lesser than the random number , attempts remaining : {attempts} ')
    else :
        print(f'Correct , The number is {randnum}') 
        break      
    if attempts == 0 :
        print(f'Game over, the number was {randnum}')        


