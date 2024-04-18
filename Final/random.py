# A function randomAvg(int A), which returns an integer greater than 0, with A as average

import random

def rand():

    return random.random()

def randomPos(N):
    return random.randint(1, N)


def randomNat(N):
    return random.randint(0, N)

def randomInt(A, B):
    return random.randint(A, B)

def randomAvg(A):
    return randomPos(2 * A -1)

def randomEvent(N):
    return rand() < 1.0 / N

random = randomAvg(A = 10)
print(random)

