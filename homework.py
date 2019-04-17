#Question 1

# name = input ("Hey, what's your name? ")
# print ("Well, it's nice to have you onboard, %s." %(name))

# Question 2

# name2 = input ("Are you serious, man? Tell me your name so we can get this sorted out. ")
# name_output = name2.upper()
# print ("Hello, " + str (name_output) + "!")
# print ("There are " + str(len(name_output)) + " letters in your name!")

#Question 3

# name = input("What is your name, sir, or ma'am? ")
# power_level = input("How strong do you think you are on a scale of 1-10000? ")
# times_lost = input ("So if you had to admit your defeats and, you have to have had at least 1, how many have you suffered?")
# print ("""
# The universe fighter {0} had no idea what awaited ahead. Even with the strength of {1} bodybuilders, 
# {0} could not have seen it coming! 
# The meteor that was about to strike the earth was {2} stronger than anything the earth had seen!
# """.format (name, power_level, times_lost))

#Question 4

# date = input("So, in numbers 0-6, give me a number and I'll give you a day? ")
# day = int(date)
# if day == 0:
#     print ("Oh...it's already Sunday!")
# elif day == 1:
#     print ("Good god, it's Monday.")
# elif day == 2:
#     print ("Ugh, it's only Tuesday...")
# elif day == 3:
#     print ("We can take a breather, it's Wednesday...")
# elif day == 4:
#     print ("We're almost there...but it's only Thursday.")
# elif day == 5:
#     print ("Holy sweet mother of jesus, it's Friday!")
# elif day == 6:
#     print ("zzzzz...I think...it's Saturday...zzz...")
# else:
#     print ("You clearly don't know how to follow instructions.")

#Question 5

# date = input("So, in numbers 0-6, give me a number and I'll give you a day? ")
# day = int(date)
# if day < 6 and day > 0 :
#     print ("Oh...fudge, I'm late for work!")
# elif day == 0 or day == 6:
#     print ("Pfft, time to get my sleep on!")
# else:
#     print ("Seriously, what's so hard about instructions!")

#Question 6

# temp = input ("Hey, what's the current temperature in degrees Celsius?")
# tempF = int(temp) * 1.8 + 32
# print ("Well, that temperature in Fahrenheit is %s!" % (tempF))

#Question 7
# bill = float(input("So how much was your meal, sir/madam?"))
# service = input ("How would you rate your service, sir/ma\'am? ")
# servicef = service.lower()
# tip = float(0.0)
# if servicef == "good" or servicef == "great":
#     tip += float(bill * 0.2)
# elif servicef == "bad" or servicef == "terrible":
#     tip += float(bill * 0.001)
# else:
#     tip += 0
# total = float(bill + tip)
# print ("Well, if that's how you feel, this is your total. {:.2f}".format(total))

#Question 8
# bill = float(input("So how much was your meal, sir/madam?"))
# service = input ("How would you rate your service, sir/ma\'am? ")
# party_count = int(input("Would you like to split the bill evenly? If so, how many are paying? "))
# servicef = service.lower()
# tip = float(0.0)
# if servicef == "good" or servicef == "great":
#     tip += float(bill * 0.2)
# elif servicef == "bad" or servicef == "terrible":
#     tip += float(bill * 0.001)
# else:
#     tip += 0
# totalp = (bill + tip) / party_count
# print ("Your total is {:.2f}".format(totalp))

#Question 9
# number = 0
# while number < 10:
#     number += 1
#     print (number)

#Question 10
coins_earned = 0
print("You have %d coins earned." %(coins_earned))
while coins_earned < 20:
    coins_earned_total = input("Would you like to buy a coin? ")
    if coins_earned_total == "yes":
       coins_earned += 1
       print ("You have gained another coin! Your current total is %d" % (coins_earned))
    elif coins_earned_total == "no":
        print ("Then...leave.")
        break
