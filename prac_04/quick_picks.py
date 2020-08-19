import random

def quick_picks():
    CONSTANTS = []
    quick_p = int(input("How many quick picks? "))
    for i in range(quick_p):
        CONSTANTS=[]
        while len(CONSTANTS) != 6:
            numbers = random.randint(1,45)
            if numbers not in CONSTANTS:
                CONSTANTS.append(numbers)
                CONSTANTS.sort()
        print(CONSTANTS)

quick_picks()
