#Basic programming with Chutes and Ladders#

In this tutorial, I'm going to show some basic programming concepts using the Milton Bradley game Chutes and Ladders as a problem to solve. What we're attempting to do is puzzle through the logic of a game intended for ages 3 and up using Python. For purposes of this tutorial, I used the game board for a Dora The Explorer branded game, but it should make no difference to the game play.

###Gameplay basics###

If you have never played Chutes and Ladders, it's a simple game involving 1-4 players, a spinner with numbers 1-6 and a game board that is divided into 100 squares. On the board are squares that have ladders to advance you forward and chutes, or slides, to take you backwards. A player spins the spinner and moves the number of spaces indicated. If that square has a chute or ladder, the player must go to the square it leads to. A player must get to square 100 exactly, meaning if they go over 100, they must spin again. 

###Basic programming concepts###

The basic programming concepts covered by this tutorial are:

* Importing libraries
* Variables
* Dictionaries
* Functions
* Conditional logic
* While loops
* For loops
* Updating dictionary keys with new values

###The tutorial###


#####Problem decomposition#####

For a classroom exercise, the first step is to discuss [problem decomposition](https://en.wikipedia.org/wiki/Decomposition_%28computer_science%29) and strategies for figuring out what steps are necessary to solve the problem. Have the students play the game, writing down the discreet steps they must take to complete a turn. As a follow-on to that process, have them group common steps into functions. I had them do this in plain language -- the students did not have any programming experience and had not been introduced to a language yet.

#####Players#####

Through problem decomposition, one of the first problems to solve is setting up players on the board. In Python, there are several ways to do this. For the sake of ease in updating a value (which square the player is on), I chose a dictionary. It looks like this:

    players = {"Player 4": 0, "Player 3":0, "Player 2":0, "Player 1":0}

Python dictionaries are unordered, so the order in which players play is not set. When I ran this, putting them in reverse order like this had them play 1, 2, 3, 4, but for our purposes, it doesn't matter so long as the ordering is the same each turn. 

Each player (or key in the Python dictionary) is assigned an initial value of 0. That's the square they start on.

#####The spinner#####

After we get players, they must spin to move. So we need a random number inclusive of 1 up and including 6. 

Python has a random library, that we can easily import and use to generate a number from 1 to 6. 

    import random
    
That's it. That's all there is to using an external library. Now we have to do something. Since a spin is something we'll do repeatedly, it's time to define a function that we can call. Functions are just a group of instructions. Some functions have inputs, and all but the most rare functions return something. In our case, the spin doesn't have an input, but the output is the number found. Here's what our spin function looks like.     

    def spin():
        return random.randrange(1, 6)

In words, the spin function returns the result of a function from the random library called randrange. We give that function a lower bound and and upper bound and it gives us back a number somewhere along those boundaries. 

#####The move#####

After a player has spun, they must move their piece. However, it's not that simple. If they player lands on a certain square, good or bad things happen. So let's start with just moving the piece.

    for k,v in players.iteritems():
            roll = spin()
            print "%s has spun a %i" % (k, roll)
            spinmove = roll + v
 
There's a little to unpack here, so lets start with `for k,v in players.iteritems():`

What that does is a little Python magic. Our dictionary is composed of keys and values -- k and v. But dictionaries are not iterable by default. What that means is that you can go through the dictionary one by one like you can with a list. But iteritems makes that possible. So that line says for each key and value pair in the dictionary players, lets do some things.

The first thing we do is spin. Then, because I like to see things on my screen to let me know it's working, we print out what the player has rolled. In this case, we're using string substitutions to change the print statement with whatever info we have at that moment. So `"%s has spun a %i" will be replaced with the value of the key -- Player 1, Player 2, etc -- and the roll, which is what is coming back from our spin function.

To know where to move, you must add the players original position, v, to the roll. That will tell you where they're going to go, but it won't tell you where they're going to end up.

#####Chutes and Ladders#####

The main feature of Chutes and Ladders is where it gets its name from. You spin, move your piece and hope for a ladder and hope to avoid a chute. In programming, we need to check if the square is a chute or a ladder, and if so, where does the player end up. 

We can turn this into a function as well.

    def move(spin, playermove):
        if playermove == 1:
             playermove = 38
        elif playermove == 4:
            playermove = 14
        elif playermove == 9:
            playermove = 31
            
           ...
        elif playermove > 100:
            playermove = playermove - spin
        return playermove

So this function has two inputs. First is what the player spun, which we need to know for the end of the game, and second is the playermove, which is the players position plus the spin. The logic is pretty easy to follow. If that position+spin number equals one of the magic squares on the board, the player move variable gets rewritten to be what the chute or ladder dictates. 

If you follow that all the way down, we get to the end of the game logic. To win the game, the player must land exactly on square 100. They don't, they stay where they are at. To keep a player where they are at, we take the square they were supposed to move to and subtract the spin, keeping them where they originated from. 

The very last line of a long function returns the square the player is supposed to be on. 

To call this function, we create a variable called turnmove, call the function and update our screen. 

    turnmove = move(roll, spinmove)
    print "%s ended up on square %i" % (k, turnmove)

The next thing we need to do is update each player on what square they are on. We do this by updating the specific key -- k -- with a new value.    
    
    players[k] = turnmove
    
This says in dictionary players there is a key called k, which is really a variable that contains Player 1, Player 2, etc. So whoever's turn it is, they're k. And we're going to update their position with the value of turnmove, which we get from our really long function that checks for chutes and ladders. Once this is done, we need to do one last thing. 

#####Winner#####

We need this script to keep going until someone gets to 100. To do that, we are going to use a While Loop. A while loop basically says while something is True or False, keeping doing something. When it no longer is what we say it is, stop.

So up at the top, under our set of players, we're going to set a variable winner to false

    winner = False
    
Then, below our functions, we're going to wrap everything we've been doing in a while loop.

    while winner == False:
        for k,v in players.iteritems():
            roll = spin()
            ...
            
So to end the game, we have to check if someone has landed on square 100. To do that, we need to check two things: if someone spins and lands exactly on square 100, the game is over. Secondarily, if they land on a square that takes them to square 100, the game is over. To end the game, we must first check if either of our two variables that could equal 100 are 100 and then we have to break the for loop, so our while loop can then break. It looks like this:

    if spinmove == 100 or turnmove == 100:
        print "%s has won the game" % k
        winner = True
        break
    else:
        continue
        
What that says is if the spinmove or the turnmove are 100, then print out that the current player has won the game, set winner to True and break out of the loop, which will then cause the While loop to break because winner is no longer false. If the current player isn't at 100, then keep playing is what the else statement says. 

And that's it. If you run the code on the command line -- python chutes.py -- you'll get the step by step printout of the game until someone wins.

    Player 2 has spun a 1
    Player 2 is moving to square 100
    Player 2 ended up on square 100
    Player 2 has won the game

