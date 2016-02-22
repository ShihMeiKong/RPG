import random

class Character():
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = 1
        self.score = 0

    def attack(self):
        """
        Returns a damage amount to enemy
        """
        rand = random.randint(0,20)
        # serves as a 20 side dice roll for random/chance
        if rand > 7:
            return int(self.attack_power * 2)
        return 0
    
    def take_damage(self, damage):
        """
        Affects current user/player. If player/user hp is 
        less or equal to zero (ie. if a enemy attacks 20 points and the user only has 10 hp,
        it results in -10 hp) they are killed
        """
        self.hp -= damage
        if self.hp <= 0:
            print("{} has been killed!".format(self.name))
            return True
            # True means the character is dead
        else:
            print("{} has lost {} health".format(self.name, damage))
            return False

    def add_points(self, amount): #calculate function for adding game points
        self.score += amount
        return self.score   # used to display the final game points score


class Player(Character):

    def pick_weapon(self):
        user_pick = input ("You have been called into the forgery. Pick a weapon (1, 2, 3)")
        if user_pick == "1":
            self.attack_power += 20
            print("You have chosen the Dwarven-forged battle axe Jarnbjorn, Wrecker of Worlds as your weapon. Your attack power has increased by 20 points")
        if user_pick == "2":
            self.attack_power += 15
            print("You have donned Megingjord, the belt of strength. Your attack power has increased by 15 points")
        if user_pick == "3":
            self.attack_power += 50 
            print("You have chosen Mjolnir, imbued with the might of Thor and created using the core of a star. Your attack power has increased by 50")


class Destroyer_Armor(Character):
    def __init__(self):
        self.name = "Destroyer Armor"
        self.hp = 5
        self.attack_power = 5
        self.score = 0

class Amora(Character):
    def __init__(self):
        self.name = "Amora the Enchantress"
        self.hp = 10
        self.attack_power = 10
        self.score = 0

class Absorbing_Man(Character):
    def __init__(self):
        self.name = "Absorbing Man"
        self.hp = 15
        self.attack_power = 15
        self.score = 0
 
"""
SK: Let's work on a game plan on Monday for the below functions

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
                    print("Try again")


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

"""

father_or_self_choice = input("""You have been informed that the Frost Giants 
    have violated the peace treaty set forth by your father. Do you speak to your father (1) or 
    Take matters into your own hands (2)""")
if father_or_self_choice == "1":
    print("Your father dismisses your concern. You decide to take matters into your hands")
if father_or_self_choice == "2":
    print("You gather a band of warriors and creep into the the Frost Giant's territory")



user = Player("test_user1", 30, 100)
user.pick_weapon()
enemy = Destroyer_Armor()



# # Battle happens here. Battle uses while loop
# while:
#     enemy_killed = enemy.take_damage(user.attack())
#     user_killed = user.take_damage(enemy.attack())
#     # attack is ongoing until some condition is met 
# # Battle ends, either enemy or user is killed
# while enemy_killed:

