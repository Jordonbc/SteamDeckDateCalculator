#If anybody is here to improve and or fix this code, feel free to credit youself. However some quick notes, please keep the original credits. They are deserved and removing them would be doing a disservice to me and the other people involved in this project. Secondly, I know this code is probably a mess, but I'm trying my best, I'm only 15 and working with what I know. Feel free to critisize it all you like, but at least make what you say constructive. Lastly, if you make any fixes, and don't mind losing out of the fame a little. Let me know what to change and I will implement it into the main fork, (you will be credited, of course). I will also try to keep the data used by this code semi-up to date, so if you ever fork this try and do the same for the best results.

#Other than that, feel free to do whatever you like!

#Loading Dependencies

import math
from numpy import loadtxt
import time
import os

#Defining clear_screen function


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
Steam Deck Date Calculator! v1.5 rewrite

Made by u/jplayzgamezevrnonsub (send bug reports to this guy if anything goes wrong)
Data provided by u/Hoxeel
Big thank you to jimmosio for helping to get the calculator and filtration code working

THE DATES PROVIDED BY THIS CALCULATOR SHOULD NOT BE EXPECTED TO BE ACCURATE
THIS CALCULATOR WAS MADE AS A FUN GIMMICK, NOT SOMETHING YOU SHOULD BE TAKING AS FACT!
""")


#Loading text files into lists

models = loadtxt('models.txt', dtype="int")
regions = loadtxt('regions.txt', dtype="str")
times = loadtxt('times.txt', dtype="int")
quarters = loadtxt('quarters.txt', dtype="str")
models = list(models)
regions = list(regions)
times = list(times)
quarters = list(quarters)
allDataPoints = len(times)

print("""
Steam Deck Date Calculator! v1.5 rewrite

Made by u/jplayzgamezevrnonsub (send bug reports to this guy if anything goes wrong)
Data provided by u/Hoxeel
Big thank you to jimmosio for helping to get the calculator and filtration code working
""")
time.sleep(3)
print(
    """THE DATES PROVIDED BY THIS CALCULATOR SHOULD NOT BE EXPECTED TO BE ACCURATE
THIS CALCULATOR WAS MADE AS A FUN GIMMICK, NOT SOMETHING YOU SHOULD BE TAKING AS FACT!
""")
time.sleep(5)

#Quarter Question

print("""
Are you Q1, Q2 or Q2+(Beta)?
(Please type your answer in the same way as the question, this is case sensitive)
""")
answer = input(":")

questionAnswered = 0

while questionAnswered == 0:
    if answer == "Q1" or answer == "q1" or answer == "1":
        userQuarter = "Q1"
        questionAnswered = 1
    elif answer == "Q2" or answer == "q2" or answer == "2":
        userQuarter = "Q2"
        questionAnswered = 1
    elif answer == "Q2+" or answer == "q2+" or answer == "After Q2" or answer == "after q2" or answer == "after Q2":
      clear_screen()
      print("""
WARNING, AFTER Q2 PREDICTION IS IN BETA.
IT WILL BE MORE INACCURATE AND CURRENTLY ONLY WORKS FOR THOSE WHO WERE Q2 BEFORE THE DELAY.
      
IF YOU HAVE ALWAYS BEEN Q2, THIS METHOD WILL NOT WORK FOR YOU!
      """)
      userQuarter = "Q3"
      time.sleep(5)
      questionAnswered = 1
    elif answer == "Gecked":
      questionAnswered = 1
    else:
        print("""
The text you entered was not recognised, please try again and please be sure to type it in the same way as in the question
(e.g. "Q1" instead of "q1" or "quarter 1")
""")
        answer = input(":")

clear_screen()

if answer == "Gecked":
  print()
  print("Wow, Gecked is getting hers March 7th! That's awesome!")
  time.sleep(9999)
#Region Question

print("""
Which regions would you like to be included in your date analysis?
EU, US, UK or ALL
(The more regions you include, the more datapoints you will have, however it may lead to other inaccuracies due to the queue being regional)
+++I seriously advise using all regions+++
""")
answer = input(":")

questionAnswered = 0

while questionAnswered == 0:
    if answer == "US" or answer == "us":
        userRegion = "US"
        questionAnswered = 1
    elif answer == "EU" or answer == "eu":
        userRegion = "EU"
        questionAnswered = 1
    elif answer == "UK" or answer == "uk":
        userRegion = "UK"
        questionAnswered = 1
    elif answer == "ALL" or answer == "All" or answer == "all":
        userRegion = "ALL"
        questionAnswered = 1
    else:
        clear_screen()
        print("""
The text you entered was not recognised,
please try again and please be sure to type it in the same way as in the question

(e.g. "US" instead of "us" or "united states")

Also note you can only select one of the options, you cannot do something like "UK and US",
it's one of them or it's all of them.
""")
        answer = input(":")

#Model Question

clear_screen()

print("""
Which model of Deck did you reserve?
64GB, 256GB or 512GB?
""")
answer = input(":")

questionAnswered = 0

while questionAnswered == 0:
    if answer == "64GB" or answer == "64gb" or answer == "64":
        userModel = int(64)
        questionAnswered = 1
    elif answer == "256GB" or answer == "256gb" or answer == "256":
        userModel = int(256)
        questionAnswered = 1
    elif answer == "512GB" or answer == "512gb" or answer == "512":
        userModel = int(512)
        questionAnswered = 1
    else:
        clear_screen()
        print("""
The way you entered your model was incorrect.
Please ensure you format it the same way the question did.
(e.g. "64GB" instead of "64 GB")
    """)
        answer = input(":")

#UnixTimeStamp Question

clear_screen()

print("""
Ok, things get a bit more technical here.

Firstly:
Make sure you are signed into https://steampowered.com ON YOUR BROWSER.

Second:
Visit this link, and copy the number after "rtReserveTime"
NOTE: IF THE WEB PAGE IS EITHER BLACK OR JUST SHOWS "SUCCESS:21", YOU ARE NOT SIGNED IN

https://store.steampowered.com/reservation/ajaxgetuserstate?rgReservationPackageIDs=%5B595603,595604,595605%5D

Third:
Come back and past it into the calculator.
PLEASE MAKE SURE TO REMOVE ANY SPACES BEFORE AND AFTER THE NUMBER, IF YOU DON'T, THE CALCULATOR WILL FAIL AND YOU WILL HAVE TO DO THIS WHOLE PROCESS AGAIN.

(Note: Repl can be a little finnicky, so you might have to right click to paste)
""")

timeStamp = int(input(":"))

#Filter Calculation

clear_screen()

print("""
Calculating date...
(This may take a while)
""")


def removeValue(x):
    models.pop(x)
    quarters.pop(x)
    regions.pop(x)
    times.pop(x)

def filtration(filterList, filterCondition):
    x = 0
    while x < len(filterList):
        if filterList[x] != filterCondition:
            removeValue(x)
        else:
            x += 1

filtration(models, userModel)
filtration(quarters, userQuarter)
if userRegion != "ALL":
    filtration(regions, userRegion)

if userQuarter == "Q1":
  daysInQuarter = 34
elif userQuarter == "Q2":
  daysInQuarter = 91
else:
  daysInQuarter = 62
#Calculation Code

for x in range (0, len(times)):
  if timeStamp >= times[x]:
    userQueuePos = (x+2)
#I'm not entirely sure why you need to add 2 to x and 1 to len(times), but it works, so just roll with it . I'm pretty sure it's because the list needs to account for the User's date not being in the list, but who knows kekw

ans = daysInQuarter / (len(times)+1)
userDate = ans*userQueuePos
userDate = math.ceil(userDate)

#Presenting user data

clear_screen()

print("Your expected Deck order date is")

if userQuarter == "Q1":
  if userDate <= 3:
    print("February" , (userDate+25))
  else:
    print("March" , (userDate-3))
elif userQuarter == "Q2":
  if userDate <= 30:
    print("April" , userDate)
  elif userDate <= 61:
    print("May" , (userDate-30))
  else:
    print("June" , (userDate-61))
else:
  if userDate <= 31:
    print("July" , userDate)
  else:
    print("August" , (userDate-31))

print("Calculated from" , len(times) , "data points out of a possible" , allDataPoints , "data points")
print()
print("User details")
print("(Don't worry, these are totally safe to include in a screenshot of your result. It just makes it a lot easier for me to fix something if somebody gets an oddball result.)")
print()
print("Region:" , userRegion)
print("Model:" , userModel)
print("Quarter:" , userQuarter)
print("Timestamp:" , timeStamp)