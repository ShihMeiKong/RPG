import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.attack = 1
    
    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp < 0

	def add_points(self, amount): #calculate function for adding game points
		self.score += amount
		return self.score   # used to display the final game points score


class Enemies:
	def __init__(self, name, points):
		self.name = name
		self.points = points

	def take_damage(self, damage):
		self.hp -= damage

	def is_dead(self):
		return self.hp < 0

	def get_points(self):  # get the value of points earned (at the end)
		return self.points


class Destroyer_Armor(Enemies):
	def __init__(self, name, hp, attack):
    	self.name = "Destroyer Armor"
    	self.hp = 5
		self.attack = 5

class Amora(Enemies):
	def __init__(self, name, hp, attack):
		self.name = "Amora the Enchantress"
		self.hp = 10
        self.attack = 10

class Absorbing_Man(Enemies):
	def __init__(self, name, hp, attack):
		self.name = "Absorbing Man"
		self.hp = 15
        self.attack = 15
 



def game(self):
		# every function in Py needs 'self'
		# we need to ramdomly select enemies (call for random funct)
		
		running = True
		while running ==True:
			enemy = self.enemy_list[random.randint(0,len(self.enemy_list) - 1)]

			# need to create a choice for the player/ Thor: boolean 

			to_fight_or_not = True
			fighting = True
			while to_fight_or_not == True:
				choice = input("Do you want to fight this enemy? (y/n)")
				if choice == "y":
					fighting = True
					to_fight_or_not = False
				elif choice == "n":
					fighting = False
					to_fight_or_not = False
				else:
					print("Try again, asshole!!!")


			# next, after y/n, we need to do the reaction outside the loop
			if fighting == True:



#create a list of dictionaries = enemies
		Enemies_template = [{'name' : 'Destroyer_Armor', "points" : 5 }, {'name' : 'Amora', 'points' : 10 }, 'name' : 'Absorbing_Man', "points" : 15]
		

		# create list of enemies 
		self.enemy_list = []
		# need to assign point value for each enemy
		
		for x in Enemies_template:
			self.enemy_list.append(Enemies(name=x["name"], points = x["points"]))
			#gives the ability to define enemies


counting_points = 0    #calculate game points
				
				counting_points += enemy.get_points() - damage.get_points()
				print(self.player.add_points(counting_points)) #player we declared to add game points


			else:
				running = False

c = Controller()
c.game()
#activate game



