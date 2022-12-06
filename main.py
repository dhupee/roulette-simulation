import random
import time

# roulette have 0 to 36
# then first 12(1-12), second 12(13-24), third 12(25-36)
# then there is 1-18, 19-36
# Odd number, Even number
# Red and Black values
# it means there is 46 types of decision making player can make

def decide():
    '''Get random int from 0 to 36

    Returns:
        int: The number it will generate
    '''

    decision = random.randint(0, 36)
    
    return decision

def get_result():
    '''Get random int from 0 to 36

    Returns:
        int: The number it will generate
    '''

    result = random.randint(0, 36)
    
    return result

while True:
    result = get_result()
    decision = decide()
    print(decision)
    print(result)
    print('\n')
    time.sleep(5) # delay 2 seconds