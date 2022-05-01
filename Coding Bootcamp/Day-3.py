# Control flow with If/else statements
height = int(input('What is your height in cm? '))
if height >= 120:
    Bill = 0
    age = int(input('How old are you? '))
    if age < 12:
        Bill = 5
        print('you have to pay $5')
    elif age <= 18:
        Bill = 7
        print('you have to pay $7')
    else:
        Bill = 12
        print('you have to pay $12')
    
    # Check if they need a photo taken
    wants_photo_taken = input('Do you want a photo taken? Y or N ')
    if wants_photo_taken == 'Y':
        Bill += 3
    print(f'Your final bill is ${Bill}')
else:
    print('Sorry kid, too short')