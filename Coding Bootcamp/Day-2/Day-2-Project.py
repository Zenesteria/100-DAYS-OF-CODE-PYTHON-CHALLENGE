total_bill = float(input('What was the total bill? $'))
percentage_tip = int(input('What percentage tip would you like to give? ')) / 100
no_of_people = int(input('How many people to split the bill? '))

total_bill_including_tip = total_bill + (percentage_tip * total_bill)

bill_per_person = round((total_bill_including_tip / no_of_people),2)



print(f'Each person should pay: ${bill_per_person}')


