from random import randint


class Menu:
	elems = ['1. Create an account', '2. Log into account', '0. Exit']

	def __init__(self):
		pass

	def start_menu(self):
		# print('1. Create an account\n' + '2. Log into account\n' + '0. Exit')
		for each in self.elems:
			print(each)


class Card:
	number = 4000000000000000
	pin = ""

	def __init__(self):
		number = rand_card_number()
		self.rand_pin()

	def rand_pin(self):
		for i in range(0, 4):
			i = randint(0, 9)
			self.pin += str(i)

	def __str__(self):
		return 'Your card number:\n{}\nYour card PIN:\n{}'.format(self.number, self.pin)


def rand_card_number():
	return 34


def choice_treat(choice):
	if choice == 0:
		print('_0')
	elif choice == 1:
		print('_1')
	elif choice == 2:
		print('_2')
	else:
		print('Wrong choice')


menu = Menu()
menu.start_menu()
choice = int(input())
choice_treat(choice)

card = Card()
print(card)
# print(card.pin)