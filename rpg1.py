# RPG1
# June 29, 2018

import os
import sys

class Player:
	def __init__(self):
        #self.name = name
		self.hp = 20
		self.mp
		self.lives = 3
		self.gameOver = False
		self.playerClass
		self.inventory = {}
		self.currentRoom = ""
		self.status

	def hpStatus(self):
		return self.hp

	def mpStatus(self):
		return self.mp

	def inventoryCheck(self):
		print(self.inventory)

	def livesCheck(self):
		return self.lives

#class Ranger(Player): # inherits from Player
	# Ranger attacks and abilities



#class Wizard(Player): # inherits from Player
	# Wizard attacks and abilities
	


# Enemies: Uthrak, Minaru, Kaldova

class Uthrak:
	def __init__(self):
		self.name = "Uthrak"
		self.hp = 12
		self.attacks = [ruthlessCleave(), roaringDoom(), wrecklessCharge()]
		self.attackNames = ["Ruthless Cleave", "Roaring Doom", "Wreckless Charge"]

	def ruthlessCleave(self):

		print("description")

		#random number if damage

		return "effect damage"

	#def roaringDoom(self):


	#def wrecklessCharge(self):


class Minaru:
	def __init__(self):		
		self.name = "Minaru"
		self.hp = 10
		self.attacks = [mindCloud(), blindingLight(), psychicTorment()]
		self.attackNames = ["Mind Cloud", "Blinding Light", "Psychic Torment"]

	#def mindCloud(self):


	#def blindingLight(self):


	#def psychicTorment(self):

# Vampire like enemy that can be reasoned with if you have a particular item, also if you are carrying certain items, you will gain an advantage and auto-crit
class Kaldova:
	def __init__(self):
		self.name = "Kaldova"
		self.hp = 18
		self.attacks = [dauntlessWager(), piercingSaber(), wormTongue()]
		self.attackNames = ["Dauntless Wager", "Piercing Saber", "Worm Tongue"]

	#def dauntlessWager(self):


	#def piercingSaber(self):


	#def wormTongue(self):


def combat(Player, Enemy):

	playerAlive = True
	enemyAlive = True

	initiativeRollPlayer = random 1 to 20
	initiativeRollEnemy = random

	print("Rolling for initiative! You rolled a #{initiativeRollPlayer}")
	print("The #{Enemy.name} rolled a #{initiativeRollEnemy}")

	if initiativeRollPlayer >= initiativeRollEnemy:
		print("Your roll was greater than or equal to #{Enemy.name}! You get to go first!")
		currentTurn = 0 # 0 represents that it is the player's turn

	else:
		print("Your roll was less than #{Enemy.name}'s! They go first!")
		currentTurn = 1 # 1 represents that it is the enemy's turn

	while(playerAlive == True && enemyAlive == True)
		if currentTurn == 0:
			print("Decide what you want to do: ")

			if Enemy.hp <= 0:
				enemyAlive = False
				print("You've defeated #{Enemy.name}!")

			currentTurn = 1

		else:
			# Randomly determine what attack the enemy will use
			attackChoice = random 0 to 2

			# Simulate the attack
			print("The enemy used #{Enemy.attackNames[attackChoice]}!")

			# split the result into an array to assess the effect and applicable damage separately
			enemyAttack = Enemy.attack[attackChoice]

			if Player.hp <= 0:
				Player.lives--
				gameStatus()
				playerAlive = False

			currentTurn = 0

def gameStatus():
	if Player.livesCheck() == 0:
		Player.gameOver = True

def characterSelection():
	print("Welcome to _____! Please select which class of character you would like to play: Ranger or Wizard")

	classChoice = gets()

	while classChoice.trim != "Ranger" || classChoice.trim != "Wizard":
		print("You entered an invalid class! Please enter Ranger or Wizard: ")
		classChoice = gets()

	if classChoice == "Ranger":
		Player.playerClass = "Ranger"
		Player.inventory = {"Longbow": 1, "Arrows": 10, "Quiver": 1, "Dagger": 1, "Health Potion": 1}
	else:
		Player.playerClass = "Wizard"
		Player.inventory = {"Spellbook": 1, "Staff": 1, "Health Potion": 2}
		Player.mp = 20


def main():
    characterSelection()

	do:

	while (Player.gameOver == false)

if __name__ == "__main__":
    main()


