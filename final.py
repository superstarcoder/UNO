from random import randint
import random, string
input("welcome to UNO!You must choose 9 cards. In this game, there are 5 numbers.Click enter.")
input("Time to choose your cards! Click enter to continue")
your_cards = []
comp_cards = []
placed_cards = ()
draw_card = (0)
def get_cards(your_cards):
	for x in range(0,9):
		card_type = 0
		card_type = (str(randint(1, 4)))
		if not card_type == "4":
			your_cards.append(card_type)
		else:
			card_type = 0
			card_type = random.choice(("2!", "2!", "4!", "cc", "cc", "cc", "cc"))
			your_cards.append(card_type)
def get_card(your_cards):
	print ("picked a card from the deck")
	card_type = (str(randint(1, 4)))
	if not card_type == "4":
		your_cards.append(card_type)
	else:
		card_type = 0
		card_type = random.choice(("2!", "4!", "cc"))
		your_cards.append(card_type)
		print (card_type)
	return your_cards

def choose_card(your_cards, placed_cards):
	draw_card = 0
	loop_count = 0
	for x in (your_cards):
		if placed_cards == ():
				if not x == "2!" and not x == "4!" and not x == "cc":
					your_cards.remove(x)
					placed_cards = (x)
					print ("computer placed card '%s'" % (placed_cards))
					return your_cards, placed_cards, draw_card
		else: 
			for x in (your_cards):
				if x == "2!":
					your_cards.remove(x)
					draw_card = 2 
					print ("computer placed card '%s' Now you must draw cards" % (x))
					return your_cards, placed_cards, draw_card
				elif x == "4!":
					your_cards.remove(x)
					draw_card = 4
					print ("computer placed card '%s' Now you must draw cards" % (x))
					return your_cards, placed_cards, draw_card
			for x in (your_cards):
				loop_count = loop_count + 1
				if x == placed_cards:
					your_cards.remove(x)
					placed_cards = (x)
					print ("computer placed card '%s'" % (placed_cards))
					return your_cards, placed_cards, draw_card
				elif x == "cc":
						print ("computer chose the 'change' card")
						for y in (your_cards):
							if not y == "2!" and not y == "4!" and not y == "cc":
								your_cards.remove(x)
								placed_cards = (y)
								print ("computer changed the card to %s" % (y))
								return your_cards, placed_cards, draw_card
				elif loop_count == len(your_cards):
					print ("computer did not have the card.")
					your_cards = get_card(your_cards)
					return your_cards, placed_cards, draw_card


def you_choose_card(your_cards, placed_cards):
	draw_card = 0
	done = False
	while done == False:
		print (your_cards)
		x = input("Choose your card. If you don't have the card, type '0'")
		if x == placed_cards and x in placed_cards:
			your_cards.remove(x)
			placed_cards = (x)
			done = True
			return your_cards, placed_cards, draw_card
		elif  x == "0":
			input("Since you don't have the card, you have to pick a card from the main deck")
			your_cards = get_card(your_cards)
			done = True
			return your_cards, placed_cards, draw_card
		elif x == "cc":
			placed_cards = (input("which number do you want to change it to?"))
			your_cards.remove(x)
			done = True
			return your_cards, placed_cards, draw_card
		elif x == "2!":
			input("good work! You secured a draw card. Now the computer will draw cards!")
			your_cards.remove(x)
			draw_card = 2
			done = True
			return your_cards, placed_cards, draw_card
		elif x == "4!":	
			input("good work! You secured a draw card. Now the computer will draw cards!")
			your_cards.remove(x)
			draw_card = 4
			done = True
			return your_cards, placed_cards, draw_card
done = False
get_cards(your_cards)
get_cards(comp_cards)
print (your_cards)
print (comp_cards)

while not done == True:
	input("computer's turn")
	if draw_card > 1:
		for x in range(0, draw_card):
			comp_cards = get_card(comp_cards)
	comp_cards, placed_cards, draw_card = choose_card(comp_cards, placed_cards)	
	print (comp_cards)
	if comp_cards == []:
		print ("YOU LOOSE! COMPUTER WON!")
		done = True
		break
	print ("TOP CARD: '%s'" % (placed_cards))
	input("your turn")
	if draw_card > 1:
		for x in range(0, draw_card):
			your_cards = get_card(your_cards)
	your_cards, placed_cards, draw_card = you_choose_card(your_cards, placed_cards)	
	print (your_cards)
	print ("PLACED CARD: '%s'" % (placed_cards))
	if your_cards == []:
		print ("YOU WIN!")
		done = True
		break
					
