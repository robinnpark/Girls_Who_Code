print("I am the age Wizard. What is your name?")
name = input()

print ("What is your age?")
age = input()

age2 = int(age)

if age2 >= 100:
    print("Wow you old as hell")
elif age2 > 12 and age2 < 20:
    print("You are a teenager")
else:
    print("Under 100 years old? Quite the youngin'")

print("I'm going to tell you something about you...")
print("Your name is %s and your age is %d." %(name, age2))
