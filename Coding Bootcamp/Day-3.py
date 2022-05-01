# Control flow with If/else statements
height = int(input('What is your height in cm? '))
if height >= 120:
    age = int(input('How old are you? '))
    if age < 12:
        print('you have to pay $5')
    elif age <= 18:
        print('you have to pay $7')
    else:
        print('you have to pay $12')
else:
    print('Sorry kid, too short')