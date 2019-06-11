'''
Created on 23 avr. 2019

@author: gtexier
'''
from enum import IntEnum, unique

@unique
class Orientation(IntEnum):
    '''
    Name of the directions used during the robot moves
    '''
    WEST = 1
    NORTH = 2
    EAST = 3
    SOUTH = 4

def inverse_direction(dir):
    '''
    Returns the inverse of the direction dir
    Parameters:
        dir: the direction to be inverted
    '''
    # Ajoutez le code pour renvoyer la direction opposee a dir
    if dir == Orientation.WEST:
        return Orientation.EAST
    elif dir == Orientation.EAST:
        return Orientation.WEST
    elif dir == Orientation.NORTH:
        return Orientation.SOUTH
    else:
        return Orientation.NORTH
def get_left(dir):
    '''
    Returns the next direction when we are in direction dir and turn left
    Parameters:
        dir: the initial direction (before going left)
    '''
    # Ajoutez le code pour renvoyer la direction dans laquelle le robot sera
    # apres avoir tourne a gauche
    if dir == Orientation.WEST:
        return Orientation.SOUTH
    elif dir == Orientation.EAST:
        return Orientation.NORTH
    elif dir == Orientation.NORTH:
        return Orientation.WEST
    else:
        return Orientation.EAST

def get_right(dir):
    '''
    Returns the next direction when we are in direction dir and turn right
    Parameters:
        dir: the initial direction (before going right)
    '''
    # Ajoutez le code pour renvoyer la direction dans laquelle le robot sera
    # apres avoir tourne a droite
    if dir == Orientation.WEST:
        return Orientation.NORTH
    elif dir == Orientation.EAST:
        return Orientation.SOUTH
    elif dir == Orientation.NORTH:
        return Orientation.EAST
    else:
        return Orientation.WEST

class OrientationError(Exception):
    pass
