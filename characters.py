import random


class Character:
    """
    name = name of character
    hp = health points
    max_health = hp 
    atk = attack points
    score = initial score, defaults to zero
    """

    def __init__(self, name, hp, atk, score=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.score = score

    def attack(self):
        """
        Returns a damage amount to enemy
        """
        rand = random.randint(0, 20)
        # serves as a 20 side dice roll for random/chance
        if rand > 7:
            return int(self.atk * 2)
        return 0

    def take_damage(self, damage):
        """
        Affects current user/player. If player/user hp is
        less or equal to zero (ie. if a enemy attacks 20 points and the user only has 10 hp,
        it results in -10 hp) they are killed
        """
        self.hp -= damage
        print("{} has lost {} health".format(self.name, damage))
        return self.hp

    def is_dead(self):
        """
        Returns boolean saying when character is dead.
        """
        return self.hp <= 0

    def add_points(self, amount): # calculate function for adding game points
        self.score += amount
        return self.score   # to display the final game points score


class Player(Character):

    def pick_weapon(self):
        user_pick = input("Pick a weapon (1, 2, 3)")
        if user_pick == "1":
            self.atk += 20
            print("You have chosen the Dwarven-forged battle axe Jarnbjorn, Wrecker of Worlds as your weapon. Your attack power has increased by 20 points")
        if user_pick == "2":
            self.atk += 15
            print("You have donned Megingjord, the belt of strength. Your attack power has increased by 15 points")
        if user_pick == "3":
            self.atk += 50
            print("You have chosen Mjolnir, imbued with the might of Thor and created using the core of a star. Your attack power has increased by 50")
        else:
            print("Pick a weapon (1, 2, 3)")


class Enemy(Character):
    def __init__(self, name, hp, atk, score=0):
        super().__init__(name, hp, atk, score)
        self.name = name
        self.hp = hp
        self.atk = atk
        self.score = score


class Battle:

    def fight(self, user, enemy):
        """
        Takes two instances of Character class a user and an enemy combatants.
        Returns the winner.
        """
        if (self.hp > 0):

        if enemy.is_dead():
            print("The enemy has died")
            return user
        elif user.is_dead():
            print("You have died")
            return enemy

        while not enemy.is_dead() and not user.is_dead():
            enemy.take_damage(user.attack())
            if enemy.is_dead():
                print("The enemy has been vanquished")
                return user
            user.take_damage(enemy.attack())
            if user.is_dead():
                print("You have died")
                return enemy



    def battle(player, enemy):
        print ("An enemy {0.name} appears...".format(enemy))

        # Combat loop
        while player.hp > 0 and enemy.hp > 0:
        player.attack(enemy)
        print("The health of the {0.name} is now {0.health}.".format(enemy))
        if enemy.health <= 0:
            break
        enemy.attack(player)
        print("Your health is now {0.health}.".format(player))

    # Display outcome
        if player.health > 0:
        print("You killed the {0.name}.".format(enemy))
        elif enemy.health > 0:
        print("The {0.name} killed you.".format(enemy))



class Game:

    def play(self):
        choice = ""
        while choice not in ['quit', 'exit', 'Quit']:
            enemies_template = [
                {'name': 'Destroyer_Armor', "hp": 5, "atk": 5},
                {'name': 'Amora', 'hp': 10, "atk": 10},
                {'name': 'Absorbing_Man', "hp": 15, "atk": 15},
            ]
            random_index = random.randint(0, len(enemies_template))
            enemy_attributes = enemies_template[random_index]
            enemy = Enemy(**enemy_attributes)
            print(enemy)
            # print(enemy_attributes['name'])


#
#   for x in Enemies_template:
#       self.enemy_list.append(Enemies(name=x["name"], points = x["points"]))
  
## gives the ability to define enemies


# counting_points = 0    #calculate game points

#                 counting_points += enemy.get_points() - damage.get_points()
#                 print(self.player.add_points(counting_points)) 



user = Player("test_user1", 30, 100)
enemy = Enemy("enemy", 10, 200)
user.pick_weapon()
battle = Battle()
battle.fight(user, enemy)
# enemy = Destroyer_Armor()


# # Battle happens here. Battle uses while loop
# while :
#     enemy_killed = enemy.take_damage(user.atk())
#     user_killed = user.take_damage(enemy.atk())
#     # attack is ongoing until some condition is met
# # Battle ends, either enemy or user is killed
# while enemy_killed:
