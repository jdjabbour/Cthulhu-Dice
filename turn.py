import sys
import math
import random


def Yellowsign(w,x,y,z):
    global points1
    global points2
    global CthPoints
    global turn
    if turn %2 != 0:
        turn = turn + 1
        points2 = points2 - 1
        CthPoints = CthPoints + 1
        print ("Player 1, you have rolled YELLOW SIGN")
        print ("Player 2 loses 1 sanity point to Cthulhu.")
        print ("Player 1, your sanity is: ", points1)
        print ("Player 2, your sanity is: ", points2)
        print ("Cthulhu your sanity taken is: ", CthPoints)
        print ("")
    else:
        turn = turn + 1
        points1 = points1 - 1
        CthPoints = CthPoints + 1
        print ("Player 2, you have rolled YELLOW SIGN")
        print ("Player 1 loses 1 sanity point to Cthulhu.")
        print ("Player 1, your sanity is: ", points1)
        print ("Player 2, your sanity is: ", points2)
        print ("Cthulhu your sanity taken is: ", CthPoints)
        print ("")
    return points1,points2,CthPoints,turn;

def Tentacle(x,y,z):
    global points1
    global points2
    global turn
    global CthPoints
    if turn %2 != 0:
        turn = turn + 1
        points1 = points1 + 1
        points2 = points2 - 1
        print ("Player 1, you have rolled TENTACLE")
        print ("Player 1 gains 1 sanity point from Player 2.")
        print ("Player 1, your sanity is: ", points1)
        print ("Player 2, your sanity is: ", points2)
        print ("Cthulhu your sanity taken is: ", CthPoints)
        print ("")
    else:
        turn = turn + 1
        points1 = points1 - 1
        points2 = points2 + 1
        print ("Player 2, you have rolled TENTACLE")
        print ("Player 2 gains 1 sanity point from Player 1.")
        print ("Player 1, your sanity is: ", points1)
        print ("Player 2, your sanity is: ", points2)
        print ("Cthulhu your sanity taken is: ", CthPoints)
        print ("")
    return points1,points2,turn;
        
def Eldersign(w,x,y,z):
    global points1
    global points2
    global CthPoints
    global turn
    if turn %2 != 0:
        turn = turn + 1
        if CthPoints != 0:
            CthPoints = CthPoints - 1
            points1 = points1 + 1
        else:
            print ("Cthulhu has nothing therefore you get NOTHING!!")
        print ("Player 1, you have rolled ELDER SIGN")
        print ("Player 1 gains 1 sanity point from Cthulhu.")
        print ("Player 1, your sanity is: ", points1)
        print ("Player 2, your sanity is: ", points2)
        print ("Cthulhu your sanity taken is: ", CthPoints)
        print ("")
    else:
        turn = turn + 1
        if CthPoints != 0:
            CthPoints = CthPoints - 1
            points2 = points2 + 1
        else:
            print ("Cthulhu has nothing therefore you get NOTHING!!")
        print ("Player 2, you have rolled ELDER SIGN")
        print ("Player 2 gains 1 sanity point from Cthulhu.")
        print ("Player 1, your sanity is: ", points1)
        print ("Player 2, your sanity is: ", points2)
        print ("Cthulhu your sanity taken is: ", CthPoints)
        print ("")
    return points1,points2,CthPoints,turn;
        
def Cthulhu(w,x,y,z):
    global points1
    global points2
    global CthPoints
    global turn
    turn = turn + 1
    print ("You have rolled CTHULHU!!  Everyone loses a little SANITY!!")
    points1 = points1 - 1
    points2 = points2 - 1
    CthPoints = CthPoints + 2
    print ("Player 1, your sanity is: ", points1)
    print ("Player 2, your sanity is: ", points2)
    print ("Cthulhu your sanity taken is: ", CthPoints)
    print ("")
    if points1 == 0:
        print ("Player 2, you win!  Player 1 has gone MAD!")
        sys.exit()
    if points2 == 0:
        print ("Player 1, you win!  Player 2 has gone MAD!")
        sys.exit()
    return points1,points2,CthPoints,turn;

def Eye(w,x,y,z):
    global points1
    global points2
    global CthPoints
    global turn
    if turn %2 != 0:
        print ("Player 1, your have rolled the EYE.")
        print ("Please choose your sign.  But choose wisely!")
        eye = raw_input ("Press Y for YELLOW SIGN, T for TENTACLE, E for ELDER SIGN... or C for CTHULHU!")
        if eye == "y" or eye == "Y":
            Yellowsign(points1,points2,CthPoints,turn)
        if eye == "t" or eye == "T":
            Tentacle(points1,points2,turn)
        if eye == "e" or eye == "E":
            Eldersign(points1,points2,CthPoints,turn)
        if eye == "c" or eye == "C":
            Cthulhu(points1,points2,CthPoints,turn)
    else:
        print ("Player 2, your have rolled the EYE.")
        print ("Please choose your sign.  But choose wisely!")
        eye = raw_input ("Press Y for YELLOW SIGN, T for TENTACLE, E for ELDER SIGN... or C for CTHULHU!")
        if eye == "y" or eye == "Y":
            Yellowsign(points1,points2,CthPoints,turn)
        if eye == "t" or eye == "T":
            Tentacle(points1,points2,turn)
        if eye == "e" or eye == "E":
            Eldersign(points1,points2,CthPoints,turn)
        if eye == "c" or eye == "C":
            Cthulhu(points1,points2,CthPoints,turn)           
    return points1,points2,CthPoints,turn;


points1 = 3
points2 = 3
CthPoints = 0
turn = 1
print ("Welcome to CTHULHU DICE! Both players start with 3 sanity points.")
print ("The first to go MAD by losing all of his sanity points loses the game...")
print ("AND THEIR SANITY TO CTHULHU!!")
while points1 != 0 or points2 != 0:
    print ("")
    if turn %2 != 0:
        roll = raw_input ("Player 1, press r to roll the dice!")
        if roll == "r" or roll == "R":
            x = random.randrange(1,6)
            if x == 1:
                Yellowsign(points1,points2,CthPoints,turn)
                if points2 == 0:
                    print ("Player 1, you win!  Player 2 has gone MAD!")
                    sys.exit()
            if x == 2:
                Tentacle(points1,points2,turn)
                if points2 == 0:
                    print ("Player 1, you win!  Player 2 has gone MAD!")
                    sys.exit()
            if x == 3:
                Eldersign(points1,points2,CthPoints,turn)
                if points2 == 0:
                    print ("Player 1, you win!  Player 2 has gone MAD!")
                    sys.exit()
            if x == 4:
                Cthulhu(points1,points2,CthPoints,turn)
                if points2 == 0:
                    print ("Player 1, you win!  Player 2 has gone MAD!")
                    sys.exit()
            if x == 5:
                Eye(points1,points2,CthPoints,turn)
                if points2 == 0:
                    print ("Player 1, you win!  Player 2 has gone MAD!")
                    sys.exit()
    if turn %2 == 0:
        roll = raw_input ("Player 2, press r to roll the dice!")
        if roll == "r" or roll == "R":
            x = random.randrange(1,3)
            if x == 1:
                Yellowsign(points1,points2,CthPoints,turn)
                if points1 == 0:
                    print ("Player 2, you win!  Player 1 has gone MAD!")
                    sys.exit()
            if x == 2:
                Tentacle(points1,points2,turn)
                if points1 == 0:
                    print ("Player 2, you win!  Player 1 has gone MAD!")
                    sys.exit()
            if x == 3:
                Eldersign(points1,points2,CthPoints,turn)
                if points1 == 0:
                    print ("Player 2, you win!  Player 1 has gone MAD!")
                    sys.exit()
            if x == 4:
                Cthulhu(points1,points2,CthPoints,turn)
                if points1 == 0:
                    print ("Player 2, you win!  Player 1 has gone MAD!")
                    sys.exit()
            if x == 5:
                Eye(points1,points2,CthPoints,turn)
                if points1 == 0:
                    print ("Player 2, you win!  Player 1 has gone MAD!")
                    sys.exit()

