import random


class Character:
    """
    name = name of character
    hp = health points
    atk = attack points
    score = initial score, defaults to zero
    """

    def __init__(self, name, hp, atk, score=0):
        self.name = name
        self.hp = hp
        self.max_health = hp
        self.atk = atk
        self.score = score


    #after each battle we need to reset health (to make sure there're hp points left)
    def heal(self):
        self.hp = self.max_health
    

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
        return self.score   # used to display the final game points score


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
    pass
    # self.name = name
    # self.hp = hp
    # self.atk = atk
    # self.score = score
