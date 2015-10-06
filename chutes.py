import random

winner = False

players = {"Player 4": 0, "Player 3":0, "Player 2":0, "Player 1":0}

def spin():
    return random.randrange(1, 7)

def move(spin, playermove):
    if playermove == 1:
        playermove = 38
    elif playermove == 4:
        playermove = 14
    elif playermove == 9:
        playermove = 31
    elif playermove == 16:
        playermove = 6
    elif playermove == 21:
        playermove = 42
    elif playermove == 28:
        playermove = 84
    elif playermove == 36:
        playermove = 44
    elif playermove == 48:
        playermove = 26
    elif playermove == 49:
        playermove = 11
    elif playermove == 51:
        playermove = 67
    elif playermove == 56:
        playermove = 53
    elif playermove == 62:
        playermove = 19
    elif playermove == 65:
        playermove = 60
    elif playermove == 71:
        playermove = 91
    elif playermove == 80:
        playermove = 100
    elif playermove == 87:
        playermove = 24
    elif playermove == 93:
        playermove = 73
    elif playermove == 95:
        playermove = 75
    elif playermove == 98:
        playermove = 78
    elif playermove > 100:
        playermove = playermove - spin
    return playermove


while winner == False:
    for k,v in players.iteritems():
        roll = spin()
        print "%s has spun a %i" % (k, roll)
        spinmove = roll + v
        print "%s is moving to square %i" % (k, spinmove)
        turnmove = move(roll, spinmove)
        print "%s ended up on square %i" % (k, turnmove)
        players[k] = turnmove
        if spinmove == 100 or turnmove == 100:
            print "%s has won the game" % k
            winner = True
            break
        else:
            continue
    
    

    
