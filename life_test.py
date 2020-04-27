
from life import *


def emptyArena():
    return Arena()

def test_EmptyArenaCellsNotAlive():
    assert not emptyArena().alive(0, 0)


def test_EmptyArenaCellsCanBeMadeAlive():
    a = emptyArena()
    a.setAlive(0, 0)
    assert a.alive(0, 0)
    assert not a.alive(0, 1)


def stringArena(alist):

    a = Arena()
    
    for y in range(len(alist)):
        for x in range(len(alist[y])):
            if not alist[y][x] == '.':
                a.setAlive(x, y)

    return a


def threeSquareDiagonal():
    return stringArena(['X..',
                        '.X.',
                        '..X'])


def test_StringArena():
    a = threeSquareDiagonal()
    assert a.alive(0, 0)
    assert a.alive(1, 1)
    assert a.alive(2, 2)
    assert not a.alive (0, 1)



def test_Equality():
    a = threeSquareDiagonal()
    b = threeSquareDiagonal()

    assert a == b


def test_Inequality():
    a = threeSquareDiagonal()

    b = stringArena(['X..',
                     '.X.',
                     '...'])

    assert not a == b


def test_LiveCellWithFewerThanTwoLiveNeighboursDies():
    a = threeSquareDiagonal()
    assert not a.survives(0, 0)
    assert not a.survives(2, 2)



def test_CountNeighbours():

    a = threeSquareDiagonal()
    assert a.countNeighbours(0, 0) == 1
    assert a.countNeighbours(1, 1) == 2
    
    
def test_LiveCellWithTwoOrThreeLiveNeighboursSurvives():
    a = stringArena(['X..',
                     '.X.',
                     '.XX'])
    assert a.survives(2, 2), "two neighbours survives"
    assert a.survives(1, 2), "three neighbours survives"


def test_LiveCellWithMoreThanThreeLiveNeighboursDies():
    a = stringArena(['X..',
                     '.XX',
                     '.XX'])
    assert not a.survives(1, 1)


def test_DeadCellWithExactlyThreeLiveNeighboursBecomesAlive():
    a = stringArena(['X..',
                     '.X.',
                     '.XX'])
    assert a.survives(2, 1)


def block():
    return stringArena(['....',
                         '.XX.',
                         '.XX.',
                         '....'])

def test_StillLifeBlock():
    a = block()
    a.next()
    assert a == block()


def vbar():
    return stringArena(['.....',
                        '..X..',
                        '..X..',
                        '..X..',
                        '.....'])

def hbar():
    return stringArena(['.....',
                        '.....',
                        '.XXX.'
                        '.....'
                        '.....'])


def test_OscillatorBlinker():
    a = hbar()
    a.next()
    assert a == vbar()
    a.next()
    assert a == hbar()
