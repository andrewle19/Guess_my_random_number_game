#Author: Andrew Le
#Email: andrewle19@csu.fullerton.edu
# Guess my number game powered by a psudo-random-number generator
# Tells user if guess is warer or colder

from MyPRNG import MyPRNG
import sys
import getopt
import pdb


# intialize psudo random number genrator class
random_num = MyPRNG()


try:
    opts, args = getopt.getopt(sys.argv[1:], 'hvs:n:x:', ['help','debug','seed=','min=','max='])

except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    sys.exit(2)

for opt, arg in opts:
    # help option shows how to run program
    if opt in ('-h','--help'):
        print 'Two was of running the program:'
        print 'Run regular python guess.py'
        print 'Run with options python guess.py -h,-v,-s,-n-x'
        print '-h = help, -v = debugging messages, -s = set seed, -n = set min, -x = set max'
   #place in debug mode
    elif opt in('-v','--debug'):
        print 'Debugging Mode'
        pdb.run()
    #set new seed
    elif opt in('-s','--seed'):
        random_num.setSeed(int(arg))
    #sets new min
    elif opt in('-n','--min'):
        random_num.setMin(int(arg))
    #sets new max
    elif opt in('-x','--max'):
        random_num.setMax(int(arg))
    else:
        sys.exit(2)



# generate 101 random numbers and assign it to the number to guess
num = random_num.generate()

# have user take a guess
guess = int(raw_input("Guess the number: "))
temp = guess #keeps track of last guess to compare
tries = 1

#used to quit the loop
quit = 0

while(quit != 1):

    if(tries > 1):
        #if the distance is closer display warmer
        if(abs(temp-num) > abs(guess-num)):
            temp = guess
            print "warmer \n"
        else:
            temp = guess
            print "colder \n"

    guess = int(raw_input("Guess again(Press 0 to quit): "))

    #if the guess wants to quit
    if(guess == 0):
        print "\nYou quit after ",tries, "tries"
        print "The number was ",num
        quit = 1 #quits the loop
        break

    tries += 1 #increment tries

    # user guesses the number prints out messege and tries
    if(guess == num):
        print "\nYou guessed it! The number was", num
        print "And it only took", tries, "tries!"
        quit = 1






