#Program til at skifte mellem states
from random import random
from time import sleep

def state0():
    print ("state0")
        # Sleep er en forsinkelse af programmet
    sleep(1.5)
    if random()>=.5:
        return state1
    else:
        return state2

def state1():
    

def state2():
    

state=state0    # initial state
while state: state=state()  # launch state machine
print ("Done with states")
