# Hiss-of-Clans

## About the Project

A terminal version of Clash of Clans implemented in Python from scratch without use of PyGame Library. All concepts of OOPS were followed for making this game. Only numpy and colorama are the major libraries used. All characters of the game are made using ASCII characters.

## Running the Game

* `pip3 install -r requirements.txt`
* `python3 game.py`

## Rules of the Game

* `W A S D` for movement of the King/ Queen depending on the initially chosen character.
* `<SPACE>` for making the king/ Queen attack (Standard Attacks).
* `1 2 3` are the three differet keys for spawning the barbarians.
* `4 5 6` are the three different keys for spawning the archers.
* `7 8 9` are the three different keys for spawning the balloons.
* Pressing `r` deploys the rage spell.
* Pressing `h` deploys the healing spell.
* Pressing `q` quits the game.
* Pressing `l` will make the king use his leviathan axe (Damage on a larger area inside a particular range).
* Pressing `k` makes the Queen use it's special Eagle Arrow attack (Damage in a larger range and at a farther distance).
* To Win the game you have to strategically destroy all the non-wall buildings.
* You will lose the game if all active troops die.
* Psst: A secret key will make you directly go to the next level :)

## Usage of OOPS Concepts

* Inheritance: There is only one Building class and all the different kinf=d of buildings inherit from that particular class. Similarly, kings and barbarians share the same super class.
* Polymorphism: Many Functions like move(), attack(), updatePosition(), changeColor(), etc belong to multiple classes and behave differently for each of them.
* Encapsulation: I have used classes and Objects which successfully encapsulate the project.
* Abstraction: The names of functions are intuitive (example: move(), attack(), etc) and hide the inner implementation details from the end user.

## Replay Functionality

* Input of every frame gets stored in the replay.json file inside the replays folder. On entering the game number (0 based indexing), the particular game gets replayed on the screen move by move. This feature could be implemented because of the deterministic nature of the game.
