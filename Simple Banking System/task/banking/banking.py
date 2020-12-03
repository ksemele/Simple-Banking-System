from random import randint


class Storage:
	__instance__ = None
	cards = []
	cards_counter = 0

	def __init__(self):
		if Storage.__instance__ is None:
			Storage.__instance__ = self
		else:
			raise Exception("Storage already created!")

	@staticmethod
	def get_instance():
		# Статический метод для того, чтобы вытащить текущий экземпляр
		# При извлечении объекта с помощью метода get_instance() мы проверяем,
		# доступен ли существующий экземпляр, и возвращаем его.
		# Если нет, то создаем его и опять возвращаем.
		if not Storage.__instance__:
			Storage()
		return Storage.__instance__

	def add_card(self, new_card):  # todo add only if !found same number in storage
		self.cards.append(new_card)

	def create_account(self):
		new_card = Account()  # todo rebuild to Storage.method
		if new_card.card_num in [x.card_num for x in self.cards]:
			new_card.rand_card_number()
		self.add_card(new_card)
		print(new_card)

	def search_card_pin(self, card_num):
		print('input num', card_num)  # todo del
		passbase = {c.card_num: c.pin for c in self.cards}
		print('total cards', storage.cards_counter)  # todo del
		if self.cards_counter > 0:
			print('pin:', passbase[card_num])  # todo del
			return passbase[card_num]
		else:
			return None


class Account:  # todo login()  --> account
	card_num = '400000'  # 0000000000'  # 400000
	pin = ''
	balance = ''

	def __init__(self):
		self.rand_card_number()
		self.rand_pin()

	def rand_card_number(self):
		self.card_num = self.card_num + ''.join(str(randint(0, 9)) for i in range(10))  # wow!

	def rand_pin(self):
		self.pin = ''.join(str(randint(0, 9)) for i in range(4))

	def print_balance(self):
		print(f'Balance: {self.balance}')

	def __str__(self):
		return 'Your card number:\n{}\nYour card PIN:\n{}\n'.format(self.card_num, self.pin)


class MenuMain:
	elems = ['1. Create an account', '2. Log into account', '0. Exit']

	def __init__(self):
		pass

	def print(self):
		for each in self.elems:
			print(each)


def menu_main_choice_treat(choice):
	if choice == '0':  # exit
		print('Bye!')
	elif choice == '1':  # todo Create account {1: choice_1()}
		storage = Storage.get_instance()
		storage.create_account()
		storage.cards_counter += 1
	elif choice == '2':  # login
		menu_login_treat()
	else:
		print('Wrong choice\n')


class MenuLogin:
	elems = ['1. Balance', '2. Log out', '0. Exit']

	def __init__(self):
		pass

	def print(self):
		for each in self.elems:
			print(each)


def menu_login_treat():
	choice = ''  # {1: , 2:}  # ключи д.б. неизменяемые (mutable obj)
	if try_login():
		storage = Storage.get_instance()
		while choice != '0':
			menu_login.print()
			choice = input()
			if choice == '1':  # balance
				print('Balance: ')  # todo acc balance

			if choice == '2':  # Log out
				print('You have successfully logged out!\n')
	else:
		print('Wrong card number or PIN!')


def try_login():
	# ['Enter your card number:', 'Enter your PIN:', 'Wrong card number or PIN!', 'You have successfully logged in!']
	storage = Storage.get_instance()
	print('Enter your card number:')
	card_num = input()
	print('Enter your PIN:')
	pin = input()
	if storage.search_card_pin(card_num) is not None:
		print('TRUUUE')  # todo del
		return True
	else:
		print('FAAALSEEEE')  # todo del
		return False


storage = Storage()
menu = MenuMain()
menu_login = MenuLogin()
choice = ''
while choice != '0':
	menu.print()
	choice = input()
	menu_main_choice_treat(choice)
