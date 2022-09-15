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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Choice_1 = input("You have arrived at a crossroad. Which way will you go? Type 'left' or 'right' \n").lower()
if Choice_1 == "left":
  Choice_2 = input("On your way, you notice a large lake and an island far in the distance. Type 'swim' to attempt to swim to the isalnd or type 'wait' to wait for a boat. \n").lower()
  if Choice_2 == "wait":
    Choice_3 = input("After waiting for a while, a friendly fisherman arrives and gives you a ride on his boat to the island. When you arrive, you notice three doors, which will you enter? Type 'red', 'blue' or yellow' \n").lower()
    if Choice_3 == 'red':
      print("A burning infero errupts from the door and you are burnt to a crisp. \nGAME OVER")
    elif Choice_3 == 'blue':
      print("You open the door and see a large treasure chest filled with gold! \nCONGRATULATIONS! YOU WIN!")
    else:
      print("You walk into the dark room only to hear the door slam behind you, leaving you trapped with no way out. \nGAME OVER.")
  else:
    print("You grow weak swimming the large distance and could not escape a hungry shark. \nGAME OVER.")
else:
  print("You stumble on you path and fall into a pit trap. \nGAME OVER")