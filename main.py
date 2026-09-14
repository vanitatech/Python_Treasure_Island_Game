print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to the Treasure Island.\nYour mission is to find the treasue. ")
crossroad = input('You are at a crossroad. Where do you want to go?  Type "left" or "right"\n').lower()

if crossroad == "left":
    swim_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Do you want to swim or wait? Type "swim" to swim across or "wait" to wait for a boat\n').lower()

    if swim_wait == "wait":
        which_door = input('Which door do you wnt to take? Type "red" or "blue" or "yellow"\n').lower()

        if which_door == "red":
            print("Burned by fire. Game Over.")

        elif which_door == "blue":
            print("Eaten by beasts. Game Over.")

        elif which_door == "yellow":
            print("You found the treasure. You Win!")

        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print('You got attacked by an angry trout. Game Over.')

else:
    print('You have fallen into a hole. Game over.')

