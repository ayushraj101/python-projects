import random
print 'Welcome to the rock,paper,scissors game '
print 'press 1 for single player and press 2 for double player'
a = input('give the input:  ')
if a==1:

	print "Welcome I am the computer player."
	input1=input("Enter your choise as 1, 2 or 3 . 1.rock  2.paper  3.scissors ")
	comp = random.choice([1, 2, 3])
	if(comp==1 and input1 == 2):
		print " rock "
		print 'you win'
	elif (comp==1 and input1==3):
		print "rock"
		print " you lose "
	elif(comp==2 and input1==1):
		print 'paper'
		print ' you lose '
	elif(comp==2 and input1==3):
		print 'paper'
		print 'you win'
	elif(comp==3 and input1==1):
		print 'scissors '
		print 'you win'
	elif(comp==3 and input1==2):
		print 'scissors '	
		print 'you lose'
	else:
		print "same same . so...........it's a draw"
if a==2:
	print "So player 1's turn. player 2 close your eyes."
	comp = input("Enter your choise as 1, 2 or 3 . 1.rock  2.paper  3.scissors ")
	print "Now player 2's turn. player 1 close your eyes."
	input1 = input("Enter your choise as 1, 2 or 3 . 1.rock  2.paper  3.scissors ")
	if(comp==1 and input1 == 2):
		print 'player 2 wins'
	elif (comp==1 and input1==3):
		print "player 1 wins "
	elif(comp==2 and input1==1):
		print 'player 1 wins  '
	elif(comp==2 and input1==3):
		print 'player 2 wins'
	elif(comp==3 and input1==1):
		print 'player 1 wins'
	elif(comp==3 and input1==2):	
		print 'player 2 wins'
	else:
		print "same same . so...........it's a draw"

