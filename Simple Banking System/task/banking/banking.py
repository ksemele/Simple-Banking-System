from random import randint


class Menu:
	elems = ['1. Create an account', '2. Log into account', '0. Exit']

	def __init__(self):
		pass

	def print(self):
		for each in self.elems:
			print(each)


class MenuLogin:
	elems = ['1. Balance', '2. Log out', '0. Exit']
		# ['Enter your card number:', 'Enter your PIN:', 'Wrong card number or PIN!', 'You have successfully logged in!']

	def __init__(self):
		pass

	def print(self):
		for each in self.elems:
			print(each)


class Card:
	number = '400000'  # 0000000000'  # 400000
	pin = ''
	balance = 0

	def __init__(self):
		self.rand_card_number()
		self.rand_pin()

	def rand_card_number(self):
		for i in range(1, 10):
			i = randint(0, 9)
			self.number += str(i)

	def rand_pin(self):
		for i in range(0, 4):
			i = randint(0, 9)
			self.pin += str(i)

	def __str__(self):
		return 'Your card number:\n{}\nYour card PIN:\n{}'.format(self.number, self.pin)


class Storage:  # todo find_card() in storage
	cards = []
	cards_counter = 0

	def __init__(self):
		pass

	def add_card(self, new_card):  # todo add only if !found same number in storage
		self.cards.append(new_card)


def create_card():
	new_card = Card()  # todo simplify to 1 return
	print(new_card)
	return new_card


def choice_treat(choice, storage):
	if choice == 0:  # exit
		print('_0')
	elif choice == 1:  # Create account
		# print('_1')
		storage.add_card(create_card())
		storage.cards_counter += 1
	elif choice == 2:  # login
		menu_login.print()
	else:
		print('Wrong choice')


storage = Storage()
menu = Menu()
menu_login = MenuLogin()

menu.print()
print(storage.cards)
choice = int(input())
choice_treat(choice, storage)
