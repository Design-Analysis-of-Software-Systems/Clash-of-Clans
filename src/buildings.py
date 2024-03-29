import numpy as np
import points as pt
from characters import barbarians, dragons, balloons, archers, superArchers, healers,kings,queens


class Building:
    def destroy(self):
        self.destroyed = True
        if self.type == 'wall':
            self.V.remove_wall(self)
            troops = barbarians+archers+superArchers+kings+queens
            if(self.level >=3):
                for tr in troops:
                    if(abs(tr.position[1] - self.position[1]) <=2 and abs(tr.position[0]-self.position[0]) <=2):
                        tr.deal_damage(200)
        elif self.type == 'hut':
            self.V.remove_hut(self)
        elif self.type == 'cannon':
            self.V.remove_cannon(self)
        elif self.type == 'wizardtower':
            self.V.remove_wizard_tower(self)
        elif self.type == 'townhall':
            self.V.remove_town_hall(self)


class Hut(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (2, 2)
        self.V = V
        self.destroyed = False
        self.health = 40
        self.max_health = 40
        self.type = 'hut'


class Cannon(Building):
    def __init__(self, position, V):
        # giving cannon a level
        # initiallizing value of level first to prevent NameError
        self.level = 1
        self.position = position
        self.dimensions = (2, 2)
        self.V = V
        self.destroyed = False
        self.health = 60 + 30*(self.level)
        self.max_health = 60 + 30*(self.level)
        self.type = 'cannon'
        self.attack = 4 + self.level
        self.attack_radius = 5 + (self.level)/2
        self.isShooting = False

    def scan_for_targets(self, King):
        self.isShooting = False
        troops = barbarians + archers
        # adding superarchers after they are visible
        k=0
        while k < len(superArchers):
            if superArchers[k].is_visible == True:
                troops.append(superArchers[k])
            k += 1

        for troop in troops:
            if (troop.position[0] - self.position[0])**2 + (troop.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(troop)
                return

        if King.alive == False:
            return

        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King)

    def attack_target(self, target):
        if(self.destroyed == True):
            return
        target.deal_damage(self.attack)


class Wall(Building):
    def __init__(self, position, V):
        self.level = 3
        self.position = position
        self.dimensions = (1, 1)
        self.V = V
        self.destroyed = False
        self.health = 100 + 40*self.level
        self.max_health = 100 + 40*self.level
        self.type = 'wall'


class TownHall(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (4, 3)
        self.V = V
        self.destroyed = False
        self.health = 100
        self.max_health = 100
        self.type = 'townhall'


class WizardTower(Building):
    def __init__(self, position, V):
        # initiallizing value of level first to prevent NameError
        self.level = 1     
        self.position = position
        self.dimensions = (1, 1)
        self.V = V
        self.destroyed = False
        self.health = 60 + 30*(self.level)
        self.max_health = 60 + 30*(self.level)
        self.type = 'wizardtower'
        self.attack = 5 + self.level
        self.attack_radius = 5 + (self.level)/2
        self.isShooting = False

    def scan_for_targets(self, King):
        self.isShooting = False
        troops = barbarians + archers + dragons + balloons + healers
        # adding superarchers after they are visible
        k=0
        while k < len(superArchers):
            if superArchers[k].is_visible == True:
                troops.append(superArchers[k])
            k += 1
        for troop in troops:
            if (troop.position[0] - self.position[0])**2 + (troop.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(troop,0)
                return

        if King.alive == False:
            return

        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King,1)

    def attack_target(self, target, isKing):
        if(self.destroyed == True):
            return

        if isKing == 1:
            target.deal_damage(self.attack)
        i = target.position[0] - 1
        j = target.position[1] - 1
        troops = barbarians+ archers + dragons + balloons + healers
        # adding superarchers after they are visible
        k=0
        while k < len(superArchers):
            if superArchers[k].is_visible == True:
                troops.append(superArchers[k])
            k += 1
        for row in range(i, i+3):
            for col in range(j, j+3):
                if(row < 0 or col < 0):
                    continue
                for troop in troops:
                    if(troop.position[0] == row and troop.position[1] == col):
                        troop.deal_damage(self.attack)


def shoot_cannons(King, V):
    for cannon in V.cannon_objs:
        V.cannon_objs[cannon].scan_for_targets(King)


def shoot_wizard_towers(King, V):
    for tower in V.wizard_tower_objs:
        V.wizard_tower_objs[tower].scan_for_targets(King)
