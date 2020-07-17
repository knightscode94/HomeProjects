#python3 stranded

from time import *
from random import *
import os,sys

#This is a function, we use it to do lots of things and then call it by it's name later on
#To create a function we use "def name():" where name can be anything.

def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name=='nt' else 'clear')

def title():
     print ("Stranded")



###############################################
     #movement

def north():
    print ("To go North press n then enter")
def east():
    print ("To go East press e then enter")
def south():
    print ("to go South press s then enter")
def west():
    print ("To go West press w then enter")


######################################
    #Players

def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global AP
    global FA
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name? ")
    #randint is a great way of adding some variety to your players statistics.
    HP = randint(45,100)
    AP = randint(5,35)
    FA = randint(5,50)

def control():
    #This will create a randomly named Controler to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Are you ok?", "Be careful theres danger ahead", "Don't forget to eat", "Don't forget to drink"]
    npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan", "Dave", "Lisa"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] My name is "+npcname+", I am here to help you get home...\n")
    shuffle(responses)
    print ("Press t to talk to Control")
    if input() == "t":
        print ("["+npcname+":] " +responses[0])
    else:
        print("["+npcname+":] Your on your own...")
#enemy
def enemy():
    global enemyHP
    global enemyAP
    global enemyname
    enemyHP = randint(15,100)
    enemyAP = randint(5,15)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for Control above.
    enemynamechoice = ["Creepy skull thing", "Big ugly worm", "Teeth Beast", "Chris Hawkeswood"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(enemynamechoice)
    enemyname = enemynamechoice[0]
    print ("\nSuddenly you hear a deathly cry, and in the distance you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has " + " " + str(enemyHP) + " " + "Health Points")
    print ("Your enemy has " + " " + str(enemyAP) + " " + "Attack Points")

###############
     #game start
def start():
    global name
    global HP
    global AP
    print (name + "...,", name + "..., the mission failed... We couldn't save you, you are Stranded...")
    sleep(1)
    print ("\nYou are hurt, the mission failed, you are in Delta, Echo, Alpha, Tango, Hotel 68719")
    sleep(1)
    #Below we are using the helper functions to join a string of text to an integer via the str() helper.
    print ("\nYour health is" + " " + str(HP))
    print ("Your attack is" + " " + str(AP))

############
#fight
def fight():
    global name
    global HP
    global AP
    global enemyHP
    global enemyAP
    global enemyname
    global npcname
    global FA
    fight = input("Is conflict the best method here?" )

    if fight == "y":
        while HP > 0:
    #This loop will only work while our characters HP is greater than 0.
            hit = randint(0,AP)
            print ("You shoot and cause " + str(hit) + " of damage")
            enemyHP = enemyHP - hit
            print ("Enemy HP", enemyHP)
            sleep(2)
            print("\n")
            if enemyHP <= 0:
                #Healing
                    heal = input("Would you like to heal? [y/n] ")
                    print ("\n")
                    if heal =="y":
                        print("The first aid kit gives:",FA,"HP")
                        HP = FA + HP
                        print("You use your first aid kit and your HP is: ",HP,"HP")
                        print("\n")
                        sleep(1)
                        stage2()
                    else:
                        print(HP)  
                        print ("["+npcname+"]: You made it! well done!")
                        sleep(3)
                        print ("\n")
                        stage2()
            enemyhit = randint(0,enemyAP)
            print ("["+enemyname+":] The " +enemyname+ " swings for you and causes " + str(enemyhit) + " of damage")
            HP = HP - enemyhit
            print ("Your HP", HP)
            sleep(2)
            print("\n")
            if HP <= 0:
                print ("["+npcname+"]: ", name + "!...,", name + "!..., Goodbye...")
                print ("Game Over")
                sys.exit(0)
    else:
        print ("["+npcname+"]:"" You pussy, you turn and run away from the " + enemyname)
        print ("\n")
        stage2()

####################################
    #Stages

#stage 1
def stage1():
    print ("\nIn the distance to the North you can see a Forrest, to the East you can see a River and to the West Space.")

    #Remember those functions we created at the start of the code? Well here we are using them in the game.
    north()
    east()
    west()
    move = input("Where would you like to go? ")
    if move == 'n':
        print ("\nGood Choice, there maybe food and water ahead.")
        print ("We dont know much about this planet but you have to watch your back.")
    #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
    elif move == 'e':
        print ("\nGo to the river there will be water here.")
        print ("We dont know much about this planet but you have to watch your back.")
    elif move == 'w':
        print ("\nIs this a good idea? I don't know what lies ahead")
        print ("Space is beautiful this time of year.\n")
    else:
        sleep(3)
        print ("Haha very funny...")
        move = input("Where would you like to go? ")
        if move == 'n':
            print ("\nGood Choice, there maybe food and water ahead.")
            print ("We dont know much about this planet but you have to watch your back.")
        #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
        elif move == 'e':
            print ("\nGo to the river there will be water here.")
            print ("We dont know much about this planet but you have to watch your back.")
        elif move == 'w':
            print ("\nIs this a good idea? I don't know what lies ahead")
            print ("Space is beautiful this time of year.\n")
        else:
            print ("You die from stupidity...")
            print ("Game over")
            sleep(5)
            sys.exit(0)

    control()
    enemy()
    fight()
    

#####################
#stage 2
def stage2():
    print ("In the distance to the North you can see a Cave, to the East you can see a Lake and to the West Space.")
    print ("\n")
    north()
    east()
    west()
    move = input("Where would you like to go? ")
    if move == 'n':
        print ("\nGood Choice, will be good shelter for the night")
        print("["+npcname+"]: Goodnight sleep well " +name )
    #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
    elif move == 'e':
        print ("\nGo to the Lake there maybe food.")
    elif move == 'w':
        print ("\nIs this a good idea? I don't know what lies ahead")
        print ("\n")
    else:
        sleep(3)
        print ("Haha very funny...")
        move = input("Where would you like to go? ")
        if move == 'n':
            print ("\nGood Choice, will be good shelter for the night")
        #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
        elif move == 'e':
            print ("\nGo to the Lake there maybe food.")
        elif move == 'w':
            print ("\nIs this a good idea? I don't know what lies ahead")
            print ("\n")
        else:
            print ("You die from stupidity...")
            print ("Game over")
            sleep(5)
            sys.exit(0)

    
    sleep(3)
    print("Good morning " +name+ ". How did you sleep?")
    stage3()

############

#stage 3
def stage3():
    global name
    global HP
    global AP
    global enemyHP
    global enemyAP
    global enemyname
    global npcname
    print ("In the distance to the North you can see a Mountain, to the East you can see a Swamp and to the West a Ship.")
    print ("\n")
    north()
    east()
    west()
    move = input("Where would you like to go? ")
    if move == 'n':
        print ("\nBetter get climbing")
    #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
    elif move == 'e':
        print ("\nI wonder what creatures lurk here...")
    elif move == 'w':
        print ("\nErmmmmmmm...")
        print ("\n")
    else:
        sleep(3)
        print ("Haha very funny...")
        move = input("Where would you like to go? ")
        if move == 'n':
            print ("\nBetter get climbing")
        #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
        elif move == 'e':
            print ("\nI wonder what creatures lurk here...")
        elif move == 'w':
            print ("\nErmmmmmmm...")
            print ("\n")
        else:
            print ("You die from stupidity...")
            print ("Game over")
            sleep(5)
            sys.exit(0)

    sleep(2)
    enemy()
    fight = input("Is conflict the best method here?" )

    if fight == "y":
        while HP > 0:
    #This loop will only work while our characters HP is greater than 0.
            hit = randint(0,AP)
            print ("You shoot and cause " + str(hit) + " of damage")
            enemyHP = enemyHP - hit
            print ("Enemy HP", enemyHP)
            sleep(2)
            print("\n")
            if enemyHP <= 0:
                #Healing
                heal = input("Would you like to heal? [y/n] ")
                print ("\n")
                if heal =="y":
                    print("The first aid kit gives:",FA,"HP")
                    HP = FA + HP
                    print("You use your first aid kit and your HP is: ",HP,"HP")
                    print("\n")
                    sleep(1)
                    stage4()
                else:
                    print ("["+npcname+"]: You made it! well done!")
                    sleep(3)
                    print ("\n")
                    stage4()
            enemyhit = randint(0,enemyAP)
            print ("["+enemyname+":] The " +enemyname+ " swings for you and causes " + str(enemyhit) + " of damage")
            HP = HP - enemyhit
            print ("Your HP", HP)
            sleep(2)
            print("\n")
            if HP <= 0:
                print ("["+npcname+"]: ", name + "!...,", name + "!..., Goodbye...")
                print ("Game Over")
                sleep(5)
                sys.exit(0)
    else:
        print ("["+npcname+"]:"" You pussy, you turn and run away from the " + enemyname)
        print ("\n")
        stage4()

###########
    #stage 4
def stage4():
    print("Congratulations you have made it to the ship")
    print("You win and go home")
    print("Or do you...")
    sleep(5)
    sys.exit(0)



####################################################
#main
clear_screen()
title()
setup()
start()


#maingame
print ("Shall we make a move? Press y then enter to continue")
#Below we use raw_input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("We can guide you to the ship but we need you, will you help us? Press y then enter to continue")

else:
    print ("You stay where you are, slowly the cold creeps in. your tank is running empty. You are Alone...")
    print ("Game Over")
    sleep(5)
    sys.exit(0)
    
if input() == "y":
    #This is a list, and it can store many items, and to do that we "append" items to the list.
    itemsc = ["3L Water","a Shovel","3 food rashens", "a First Aid Kit", "an Oxygen Tank", " a Repair module"]
    shuffle(itemsc)
    items = itemsc[0]
    shuffle(itemsc)
    items2 = itemsc[0]
    shuffle(itemsc)
    items3 = itemsc[0]
    i = []
    i.append("Pistol")
    i.append("Radio")
    print ("You are carrying a" + " " + i[0] + " " + "and your" + " " + i[1])
    print ("You also have " + ""+items+", " + ""+items2+" and " + ""+items3+"" + ". Lets go...")
    stage1()
else:
    print ("Really...")
    print ("You have nothing but your sense of humour, you stand up ready to start walking.")
    stage1()

          






