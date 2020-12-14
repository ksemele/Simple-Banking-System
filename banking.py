from random import randint
import sqlite3


class Account:
    id = 0
    card_num = ''
    pin = ''
    balance = 0

    def __init__(self):
        pass

    def empty(self):
        self.card_num = ''
        self.pin = ''
        self. balance = 0

    def new_account(self):
        self.rand_card_number()
        self.rand_pin()

    def rand_card_number(self):
        self.card_num = '400000' + ''.join(str(randint(0, 9)) for i in range(9))  # wow!
        self.calc_luhn_last()

    def calc_luhn_last(self):
        self.card_num = calc_luhn_num(self.card_num)

    def rand_pin(self):
        self.pin = ''.join(str(randint(0, 9)) for i in range(4))

    def save_to_sql(self):
        cur.execute('INSERT INTO card VALUES (?,?,?,?);', (self.id, self.card_num, self.pin, self.balance))
        conn.commit()

    def print_balance(self):
        print(f'Balance: {self.balance}\n')

    def add_income(self):
        print('Enter income:\n')
        try:
            income = int(input())
            print('Add ', income, 'to ->', self.balance)  # todo del
            self.balance += income
            cur.execute('UPDATE card SET balance = ? WHERE number = ?;', (self.balance, self.card_num))
            conn.commit()
            print('Income was added!\n')
        except ValueError:
            print('Error input!\n')

    def do_transfer(self):
        print('Transfer\nEnter card number:\n')
        acc_to_transfer = input()
        if not check_luhn_num(acc_to_transfer):
            print('Probably you made a mistake in the card number. Please try again!\n')
            return
        if not storage.search_card_num(acc_to_transfer):  # todo do it!
            print('Such a card does not exist.\n')
            return
        print('Enter how much money you want to transfer:\n')
        try:
            money = int(input())
        except ValueError:
            return
        if money > self.balance:
            print('Not enough money!\n')
            return
        # todo do transfer && save to SQL
        pass

    def delete_account(self):
        cur.execute('DELETE from card WHERE number = (?);', (self.card_num,))
        conn.commit()
        index = 0
        for each in storage.cards:
            if each.card_num == self.card_num:
                index = storage.cards.index(each)
        storage.cards.pop(index)
        print('The account has been closed!\n')

    def __str__(self):
        return 'Your card number:\n{}\nYour card PIN:\n{}\n'.format(self.card_num, self.pin)


def is_odd(num):
    if num % 2:
        return True  # Odd (нечетное)
    else:
        return False  # Even


def check_luhn_num(number):
    calc_part = number[:-1]
    calculated_num = calc_luhn_num(calc_part)
    if calculated_num != number:
        return False
    else:
        return True


def calc_luhn_num(number):  # calculate luhn num from number
    checksum = []
    odd = 1
    for each in number:
        if odd:
            checksum.append(int(each) * 2)
            odd = 0
        else:
            checksum.append(int(each))
            odd = 1
    for each in checksum:
        if int(each) > 9:
            checksum[checksum.index(each)] = each - 9
    res = 0
    for each in checksum:
        res = res + int(each)
    calc = res
    while calc % 10:
        calc += 1
    luhn_num = number + ''.join(str(calc - res))
    return luhn_num


def convert_sql_to_new_account(sql_element):
    # print('parse this:', sql_element)  # todo tmp print RAW data
    new_account = Account()
    new_account.empty()
    new_account.id = sql_element[0]
    new_account.card_num = sql_element[1]
    new_account.pin = sql_element[2]
    new_account.balance = sql_element[3]
    return new_account


class Storage:
    __instance__ = None
    cards = []
    cards_counter = 0
    login_in = Account()

    def __init__(self):
        if Storage.__instance__ is None:
            Storage.__instance__ = self
            cur.execute('SELECT * from card;')
            self.sql_cur = cur
            self.conn = conn
            for each in self.sql_cur:
                self.add_account(new_account=convert_sql_to_new_account(each))
            self.cards_counter = len(self.cards)
        else:
            raise Exception("Storage already created!")

    @staticmethod
    def get_instance():

        if not Storage.__instance__:
            Storage()
        return Storage.__instance__

    def add_account(self, new_account):
        self.cards.append(new_account)

    def create_account(self):
        new_card = Account()
        new_card.new_account()
        if new_card.card_num in [x.card_num for x in self.cards]:
            new_card.rand_card_number()
        self.add_account(new_card)
        new_card.save_to_sql()
        self.cards_counter += 1
        print(new_card)

    def search_card_num(self, card_num):
        passbase = {c.card_num: c.pin for c in self.cards}
        if self.cards_counter > 0 and card_num in passbase:
            return True
        else:
            return False

    def search_card_pin(self, card_num):
        passbase = {c.card_num: c.pin for c in self.cards}
        if self.cards_counter > 0 and card_num in passbase:
            storage.login_in.card_num = card_num
            storage.login_in.pin = passbase[card_num]
            return passbase[card_num]
        else:
            return None


class MenuMain:
    elems = ['1. Create an account', '2. Log into account', '0. Exit']

    def __init__(self):
        pass

    def print_menu(self):
        for each in self.elems:
            print(each)


def menu_main_choice_treat():
    storage = Storage.get_instance()
    menu_funcs = {
        0: exit_banking,
        1: storage.create_account,
        2: menu_login_treat,
    }
    while 1:
        menu.print_menu()
        try:
            choice = int(input())
            try:
                menu_funcs.get(choice)()
            except TypeError:
                pass
        except ValueError:
            pass

def exit_banking():
    print('Bye!')
    exit()


class MenuLogin:
    elems = ['1. Balance', '2. Add income', '3. Do transfer', '4. Close account', '5. Log out', '0. Exit']

    def print_menu(self):
        for each in self.elems:
            print(each)


def menu_login_treat():
    storage = Storage.get_instance()
    menu_funcs = {
        0: exit_banking,
        1: storage.login_in.print_balance,
        2: storage.login_in.add_income,
        3: storage.login_in.do_transfer,
        4: storage.login_in.delete_account,
        5: storage.login_in.empty,
    }
    if try_login():
        print('You have successfully logged in!\n')
        while 1:
            menu_login.print_menu()
            try:
                choice = int(input())
                menu_funcs.get(choice)()
                if choice == 5 or choice == 4:
                    break
            except ValueError:
                pass
    else:
        print('Wrong card number or PIN!\n')


def try_login():
    storage = Storage.get_instance()
    print('Enter your card number:')
    card_num = input()
    print('Enter your PIN:')
    pin = input()
    if storage.search_card_pin(card_num) is not None:
        storage.logged_in = card_num
        if storage.login_in.pin == pin:
            cur.execute('SELECT balance FROM card WHERE number = (?)', (storage.login_in.card_num,))
            for each in cur:
                storage.login_in.balance = each[0]  # todo how i can do this wich another variant???
            return True
    else:
        return False


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS card(
    id INTEGER,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
    );""")
conn.commit()
storage = Storage()
menu = MenuMain()

for each in storage.cards:  # todo del - print all accounts in storage
    print(each.card_num, each.pin, each.balance)

menu_login = MenuLogin()
menu_main_choice_treat()
