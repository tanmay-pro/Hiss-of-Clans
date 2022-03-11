# Hiss-of-Clans

## About the Project

A terminal version of Clash of Clans implemented in Python from scratch without use of PyGame Library. All concepts of OOPS were followed for making this game. Only numpy and colorama are the major libraries used. All characters of the game are made using ASCII characters.

## Running the Game

* `pip3 install -r requirements.txt`
* `python3 game.py`

## Rules of the Game

* `W A S D` for movement of the King.
* `<SPACE>` for making the king attack at the position in front of him.
* `1 2 3` are the three differet keys for spawning the barbarians.
* Pressing `r` deploys the rage spell.
* Pressing `h` deploys the healing spell.
* To Win the game you have to strategically destroy all the non-wall buildings.
* You will lose the game if all active troops die.

## Usage of OOPS Concepts

* Inheritance: There is only one Building class and all the different kinf=d of buildings inherit from that particular class. Similarly, kings and barbarians share the same super class.
* Polymorphism: Many Functions like move(), attack(), updatePosition(), changeColor(), etc belong to multiple classes and behave differently for each of them.
* Encapsulation: I have used classes and Objects which successfully encapsulate the project.
* Abstraction: The names of functions are intuitive (example: move(), attack(), etc) and hide the inner implementation details from the end user.

## Replay Functionality

* Input of every frame gets stored in the replay.json file inside the replays folder. On entering the game number (0 based indexing), the particular game gets replayed on the screen move by move. This feature could be implemented because of the deterministic nature of the game.
