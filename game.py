from multiprocessing.spawn import spawn_main
from matplotlib.pyplot import bar
import numpy as np
import colorama
import time
import tty
import sys
import os
import json
from colorama import Fore, Back, Style
from src.buildings import *
from src.movingObjects import *
from src.others import *
from src.spells import *
from src.map import *
from src.input import *

inputs = []

colorama.init(autoreset=True)
currLevel = 1
if __name__ == "__main__":
    while currLevel != 4:
        os.system("cls" if os.name == "nt" else "clear")
        char = input("What do you want to play with King(K) or Queen(Q)? Press K for King and Q for Queen\n")
        orig_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        gameStatus = "playing"

        currBarbarians = 0
        currArchers  = 0
        currBalloons = 0
        currSpellsUsed = 0
        chosenKing = -1
        if char == "K" or char == "k":
            chosenKing = 1
        elif char == "Q" or char == "q":
            chosenKing = 0
        else:
            print("Invalid input. By default, king has been selected!")
            time.sleep(2)
            chosenKing = 1
        frames = 0
        attackFactorBuilding = 1

        nameOfFile = "src/config" + str(currLevel) + ".json"
        with open(nameOfFile) as json_file:
            data = json.load(json_file)

        GAME_SCREEN_WIDTH = data['game_screen_width']
        GAME_SCREEN_HEIGHT = data['game_screen_height']
        GAME_HORIZONTAL_BOUNDARY = data['game_horizontal_boundary']
        GAME_VERTICAL_BOUNDARY = data['game_vertical_boundary']
        KING_STARTING_X = data['king_starting_x']
        KING_STARTING_Y = data['king_starting_y']
        KING_HEALTH = data['king_health']
        KING_SPEED = data['king_speed']
        KING_ATTACK = data['king_attack']
        QUEEN_STARTING_X = data['queen_starting_x']
        QUEEN_STARTING_Y = data['queen_starting_y']
        QUEEN_HEALTH = data['queen_health']
        QUEEN_SPEED = data['queen_speed']
        QUEEN_ATTACK = data['queen_attack']
        TOWN_X_POSITION = data['town_x_position']
        TOWN_Y_POSITION = data['town_y_position']
        TOWN_HEALTH = data['town_health']
        NUMBER_HUTS_IN_ROW = data['number_huts_in_row']
        NUMBER_HUTS = data['number_huts']
        HUT_STARTING1 = data['hut_starting1']
        HUT_STARTING2 = data['hut_starting2']
        HUT_HEALTH = data['hut_health']
        HUT_STARTINGY = data['hut_startingy']
        NUMBER_WALLS_X = data['number_walls_x']
        NUMBER_WALLS_Y = data['number_walls_y']
        WALL_STARTING1X = data['wall_starting1x']
        WALL_STARTING1Y = data['wall_starting1y']
        WALL_STARTING2X = data['wall_starting2x']
        WALL_STARTING2Y = data['wall_starting2y']
        WALL_HEALTH = data['wall_health']
        CANNON_1X = data['cannon_1x']
        CANNON_1Y = data['cannon_1y']
        CANNON_2X = data['cannon_2x']
        CANNON_2Y = data['cannon_2y']
        CANNON_HEALTH = data['cannon_health']
        CANNON_DAMAGE = data['cannon_damage']
        CANNON_RANGE = data['cannon_range']
        TOWER_1X = data['tower_1x']
        TOWER_1Y = data['tower_1y']
        TOWER_2X = data['tower_2x']
        TOWER_2Y = data['tower_2y']
        TOWER_HEALTH = data['tower_health']
        TOWER_DAMAGE = data['tower_damage']
        TOWER_RANGE = data['tower_range']
        MAX_BARBARIANS = data['max_barbarians']
        MAX_BALLOONS = data['max_balloons']
        MAX_SPELLS = data['max_spells']
        MAX_ARCHERS = data['max_archers']
        TIMEOUT_VAL = data['timeout_val']
        AXE_RANGE = data['axe_range']
        BARBARIAN_HEALTH = data['barbarian_health']
        BARBARIAN_ATTACK = data['barbarian_attack']
        BARBARIAN_SPEED = data['barbarian_speed']
        ARCHER_HEALTH = data['archer_health']
        ARCHER_ATTACK = data['archer_attack']
        ARCHER_SPEED = data['archer_speed']
        ARCHER_RANGE = data['archer_range']
        BALLOON_HEALTH = data['balloon_health']
        BALLOON_SPEED = data['balloon_speed']
        BALLOON_ATTACK = data['balloon_attack']

        mainMap = map(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, GAME_HORIZONTAL_BOUNDARY, GAME_VERTICAL_BOUNDARY)
        mainMap.createMap()
        mainKing = king(KING_STARTING_X, KING_STARTING_Y, KING_HEALTH, KING_SPEED, KING_ATTACK)
        texture, heightTexture, maxWidthTexture = getTexture("src/textures/king.txt")
        mainKing.assignHeight(heightTexture)
        mainKing.assignmaxWidth(maxWidthTexture)
        mainKing.assignTexture(texture)
        mainKing.isKing = True
        
        mainQueen = archerQueen(QUEEN_STARTING_X, QUEEN_STARTING_Y, QUEEN_HEALTH, QUEEN_SPEED, QUEEN_ATTACK)
        texture, heightTexture, maxWidthTexture = getTexture("src/textures/archerQueen.txt")
        mainQueen.assignHeight(heightTexture)
        mainQueen.assignmaxWidth(maxWidthTexture)
        mainQueen.assignTexture(texture)
        mainQueen.isKing = True

        if chosenKing == 1:
            mainKing.assignInitialPosition(mainMap)
        else:            
            mainQueen.assignInitialPosition(mainMap)
        
        mainTownHall = townHall(TOWN_X_POSITION, TOWN_Y_POSITION, TOWN_HEALTH)
        texture, heightTexture, maxWidthTexture = getTexture(
            "src/textures/townHall.txt")
        mainTownHall.assignHeight(heightTexture)
        mainTownHall.assignmaxWidth(maxWidthTexture)
        mainTownHall.assignTexture(texture)
        mainTownHall.assignPosition(mainMap)

        arrayHuts = []
        texture, heightTexture, maxWidthTexture = getTexture("src/textures/hut.txt")
        for i in range(0, NUMBER_HUTS_IN_ROW):
            arrayHuts.append(hut(HUT_STARTING1, HUT_STARTINGY + 6*i, HUT_HEALTH))
        for i in range(0, NUMBER_HUTS_IN_ROW):
            arrayHuts.append(hut(HUT_STARTING2, HUT_STARTINGY + 6*i, HUT_HEALTH))
        for Hut in arrayHuts:
            Hut.assignHeight(heightTexture)
            Hut.assignmaxWidth(maxWidthTexture)
            Hut.assignTexture(texture)
            Hut.assignPosition(mainMap)

        arrayWalls = []
        texture, heightTexture, maxWidthTexture = getTexture(
            "src/textures/wall.txt")
        for i in range(0, NUMBER_WALLS_Y):
            arrayWalls.append(wall(WALL_STARTING1X, WALL_STARTING1Y + i, WALL_HEALTH))
        for i in range(0, NUMBER_WALLS_Y):
            arrayWalls.append(wall(WALL_STARTING2X, WALL_STARTING1Y + i, WALL_HEALTH))
        for i in range(0, NUMBER_WALLS_X):
            arrayWalls.append(wall(WALL_STARTING1X + i, WALL_STARTING1Y, WALL_HEALTH))
        for i in range(0, NUMBER_WALLS_X):
            arrayWalls.append(wall(WALL_STARTING1X + i, WALL_STARTING2Y, WALL_HEALTH))

        for Wall in arrayWalls:
            Wall.assignHeight(heightTexture)
            Wall.assignmaxWidth(maxWidthTexture)
            Wall.assignTexture(texture)
            Wall.assignPosition(mainMap)

        arrayCannons = []
        texture, heightTexture, maxWidthTexture = getTexture(
            "src/textures/cannon.txt")
        cannon1 = cannon(CANNON_1X, CANNON_1Y, CANNON_HEALTH, CANNON_DAMAGE, CANNON_RANGE)
        cannon2 = cannon(CANNON_2X, CANNON_2Y, CANNON_HEALTH, CANNON_DAMAGE, CANNON_RANGE)
        arrayCannons.append(cannon1)
        arrayCannons.append(cannon2)
        for Cannon in arrayCannons:
            Cannon.assignHeight(heightTexture)
            Cannon.assignmaxWidth(maxWidthTexture)
            Cannon.assignTexture(texture)
            Cannon.assignPosition(mainMap)

        arrayTowers = []
        texture, heightTexture, maxWidthTexture = getTexture(
            "src/textures/tower.txt")
        tower1 = wizardTower(TOWER_1X, TOWER_1Y, TOWER_HEALTH, TOWER_DAMAGE, TOWER_RANGE)
        tower2 = wizardTower(TOWER_2X, TOWER_2Y, TOWER_HEALTH, TOWER_DAMAGE, TOWER_RANGE)
        arrayTowers.append(tower1)
        arrayTowers.append(tower2)
        for Tower in arrayTowers:
            Tower.assignHeight(heightTexture)
            Tower.assignmaxWidth(maxWidthTexture)
            Tower.assignTexture(texture)
            Tower.assignPosition(mainMap)

        mainMap.drawMap2()
        
        spBarbarian = []; spArcher = []; spBalloon = []
        spBarbarian, spArcher, spBalloon = makeSpawningPoints(mainMap)
        
        arrayBarbarians = []
        arrayArchers = []
        arrayBalloons = []
        
        while gameStatus == "playing":
            frames += 1
            startTime = time.time()
            os.system("cls" if os.name == "nt" else "clear")
            mainMap.drawMap2()
            if not mainKing.isDead:
                if chosenKing == 1:
                    mainKing.displayHealth()
                else:
                    mainQueen.displayHealth()
            print("Number of barbarians you can still spawn: " + str(MAX_BARBARIANS -currBarbarians))
            print("Number of archers you can still spawn: " + str(MAX_ARCHERS -currArchers))
            print("Number of balloons you can still spawn: " + str(MAX_BALLOONS -currBalloons))
            print("Number of spells you can still use: " + str(MAX_SPELLS - currSpellsUsed))
            # print("Chosen King value = " + str(chosenKing))
            print("Current level = " + str(currLevel))
            
            if frames % 2 ==0:
                for everyBarbarian in arrayBarbarians:
                    if not everyBarbarian.isDead: 
                        everyBarbarian.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)
                        everyBarbarian.move(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)
            for everyArcher in arrayArchers:
                if not everyArcher.isDead:
                    if not everyArcher.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers):
                        everyArcher.move(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)
            for everyBalloon in arrayBalloons:
                if not everyBalloon.isDead:
                    if not everyBalloon.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers):
                        everyBalloon.move(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)
                  
            if(frames % attackFactorBuilding == 0):
                for everyCannon in arrayCannons:
                    if not everyCannon.isDestroyed:
                        everyCannon.spawnAgain(mainMap)
                        everyCannon.attack(mainMap, mainKing, mainQueen, arrayBarbarians, arrayArchers, arrayBalloons, chosenKing)    
                for everyTower in arrayTowers:
                    if not everyTower.isDestroyed:
                        everyTower.spawnAgain(mainMap)
                        everyTower.attack(mainMap, mainKing, mainQueen, arrayBarbarians, arrayArchers, arrayBalloons, chosenKing)

            if TIMEOUT_VAL > (time.time() - startTime):
                time.sleep(TIMEOUT_VAL - (time.time() - startTime))
            ch = input_to(Get())
            inputs.append(ch)
            
            if ch == "w" or ch == "a" or ch == "s" or ch == "d":
                if chosenKing == 1:                
                    if not mainKing.isDead:
                        mainKing.move(ch, mainMap)
                else:
                    if not mainQueen.isDead:
                        mainQueen.move(ch, mainMap)

            elif ch == "q":
                gameStatus = "quit"
            
            elif ch == " ":
                if chosenKing == 1:
                    if not mainKing.isDead:
                        mainKing.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)
                else:
                    if not mainQueen.isDead:
                        mainQueen.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)
            
            elif (ch == "1" or ch=="2" or ch=="3") and currBarbarians < MAX_BARBARIANS:
                currBarbarians += 1 
                if ch == "1":
                    barbarian1 = barbarian(spBarbarian[0].positionX, spBarbarian[0].positionY, BARBARIAN_HEALTH, BARBARIAN_SPEED, BARBARIAN_ATTACK)
                elif ch == "2":
                    barbarian1 = barbarian(spBarbarian[1].positionX, spBarbarian[1].positionY, BARBARIAN_HEALTH, BARBARIAN_SPEED, BARBARIAN_ATTACK)
                elif ch=="3":
                    barbarian1 = barbarian(spBarbarian[2].positionX, spBarbarian[2].positionY, BARBARIAN_HEALTH, BARBARIAN_SPEED, BARBARIAN_ATTACK)
                arrayBarbarians.append(barbarian1)
                texture, heightTexture, maxWidthTexture = getTexture(
                    "src/textures/barbarian.txt")
                barbarian1.assignHeight(heightTexture)
                barbarian1.assignmaxWidth(maxWidthTexture)
                barbarian1.assignTexture(texture)
                barbarian1.assignInitialPosition(mainMap)
            
            elif (ch == "4" or ch=="5" or ch=="6") and currArchers < MAX_ARCHERS:
                currArchers +=1
                if ch == "4":
                    archer1 = archer(spArcher[0].positionX, spArcher[0].positionY, ARCHER_HEALTH, ARCHER_SPEED, ARCHER_ATTACK, ARCHER_RANGE)
                elif ch=="5":
                    archer1 = archer(spArcher[1].positionX, spArcher[1].positionY, ARCHER_HEALTH, ARCHER_SPEED, ARCHER_ATTACK, ARCHER_RANGE)
                elif ch=="6":
                    archer1 = archer(spArcher[2].positionX, spArcher[2].positionY, ARCHER_HEALTH, ARCHER_SPEED, ARCHER_ATTACK, ARCHER_RANGE)
                arrayArchers.append(archer1)
                texture, heightTexture, maxWidthTexture = getTexture(
                    "src/textures/archer.txt")
                archer1.assignHeight(heightTexture)
                archer1.assignmaxWidth(maxWidthTexture)
                archer1.assignTexture(texture)
                archer1.assignInitialPosition(mainMap)
            
            elif (ch == "7" or ch=="8" or ch=="9") and currBalloons < MAX_BALLOONS:
                currBalloons += 1
                if ch == "7":
                    balloon1 = balloon(spBalloon[0].positionX, spBalloon[0].positionY, BALLOON_HEALTH, BALLOON_SPEED, BALLOON_ATTACK)
                elif ch=="8":
                    balloon1 = balloon(spBalloon[1].positionX, spBalloon[1].positionY, BALLOON_HEALTH, BALLOON_SPEED, BALLOON_ATTACK)
                elif ch=="9":
                    balloon1 = balloon(spBalloon[2].positionX, spBalloon[2].positionY, BALLOON_HEALTH, BALLOON_SPEED, BALLOON_ATTACK)
                arrayBalloons.append(balloon1)
                texture, heightTexture, maxWidthTexture = getTexture(
                    "src/textures/balloon.txt")
                balloon1.assignHeight(heightTexture)
                balloon1.assignmaxWidth(maxWidthTexture)
                balloon1.assignTexture(texture)
                balloon1.assignPositionAir(mainMap)

            elif (ch == "r" or ch == "h") and currSpellsUsed < MAX_SPELLS:
                currSpellsUsed += 1
                if ch == "r":
                    movementFactorMuliplication = 2
                    Spell = spell(2, movementFactorMuliplication, 1)
                    TIMEOUT_VAL/=movementFactorMuliplication
                    attackFactorBuilding *= movementFactorMuliplication
                else:
                    Spell = spell(1, 1, 1.5)
                if not mainKing.isDead:            
                    mainKing.castSpell(Spell)
                for everyBarbarian in arrayBarbarians:
                    if not everyBarbarian.isDead:
                        everyBarbarian.castSpell(Spell)
            
            elif ch == "l" and chosenKing == 1:
                if not mainKing.isDead:
                    mainKing.attackMajor(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers, AXE_RANGE)    
            
            elif ch == "k":
                if not mainQueen.isDead and chosenKing == 0:
                    time.sleep(1)
                    mainQueen.attackMajor(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons, arrayTowers)

            elif ch== "p":
                currLevel += 1
                break 

            sys.stdin.flush()
            sys.stdout.flush()
            returnVal = checkGameStatus(
                    mainMap, mainTownHall, arrayHuts, arrayCannons, mainKing, arrayBarbarians, mainQueen, chosenKing)
            if returnVal == 0:
                gameStatus = "lost"
            elif returnVal == 1:
                currLevel += 1
                break
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
        if gameStatus != "playing":
            break
        
    if currLevel == 4:
        os.system("cls" if os.name == "nt" else "clear")
        print("You won!")
    elif gameStatus == "lost":
        os.system("cls" if os.name == "nt" else "clear")
        print("You lost!")
    elif gameStatus == "quit":
        os.system("cls" if os.name == "nt" else "clear")
        print("You quit!")

    with open('replays/replay.json', 'r+') as f:
        data = json.loads(f.read())
        data.append(inputs)
            
    with open('replays/replay.json', 'w') as f:
        json.dump(data, f)
