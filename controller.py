import random

from model import Player, Enemy
from view import View


"""
hp = health points
atk = attack points

"""


class Game:
    def play(self):
        choice = input("Do you want to start the game?")
        while choice.lower() not in ['quit', 'exit', 'no']:
            enemies_template = [
                {'name': 'Destroyer_Armor', "hp": 5, "atk": 5},
                {'name': 'Amora', 'hp': 10, "atk": 10},
                {'name': 'Absorbing_Man', "hp": 15, "atk": 15},
            ]
            random_index = random.randint(0, len(enemies_template))
            enemy_attributes = enemies_template[random_index]
            enemy = Enemy(**enemy_attributes)
            print(enemy)

    def fight(self, user, enemy):
        """
        Takes two instances of Character class a user and an enemy combatants.
        Returns the winner.
        """
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

#         # need to assign point value for each enemy

#         for x in Enemies_template:
#             self.enemy_list.append(Enemies(name=x["name"], points = x["points"]))
#             #gives the ability to define enemies


# counting_points = 0    #calculate game points

#                 counting_points += enemy.get_points() - damage.get_points()
#                 print(self.player.add_points(counting_points)) #player we declared to add game points

# 



view = View()
view.backstory()
game = Game()
user = Player("test_user1", 30, 100)
enemy = Enemy("enemy", 10, 200)
user.pick_weapon()
game.fight(user, enemy)
