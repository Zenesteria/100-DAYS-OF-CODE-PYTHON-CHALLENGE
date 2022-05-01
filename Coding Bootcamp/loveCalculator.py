# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
couplename = (name1 + name2).lower()

no_TRUE = str(couplename.count('t') + couplename.count('r') + couplename.count('u') + couplename.count('e'))

no_LOVE = str(couplename.count('l') + couplename.count('o') + couplename.count('v') + couplename.count('e')) 

loveScore = int(no_TRUE + no_LOVE)

if loveScore < 10 or loveScore > 90:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif loveScore >= 40 and loveScore <= 50:
    print(f'Your score is {loveScore}, you are alright together.')
else:
    print(f'Your score is {loveScore}')