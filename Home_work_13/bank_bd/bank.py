import random
import sqlite3


def get_random_digits(count):
    return ''.join([str(random.randint(1, 10)) for _ in range(count)])


class BankAccount:
    def __init__(self, card_holder: str, money=0.0, account_number=None, card_number=None):
        if len(card_holder.split()) == 3:
            self.card_holder: str = card_holder.upper()
            self.money: int | float = money
            self.card_number: str = get_random_digits(16) if card_number is None else card_number
            self.account_number: str = get_random_digits(20) if account_number is None else account_number
        else:
            raise TypeError('В ФИО должно быть имя,фамилия и отчество')


class Bank:
    def __init__(self, bank_accounts=None):
        self.__bank_accounts: dict[str, BankAccount] = bank_accounts if bank_accounts else {}

    def open_account(self, card_holder: str) -> BankAccount:
        new_account = BankAccount(card_holder)
        self.__bank_accounts[new_account.account_number] = new_account
        return new_account

    def __get_account(self, account_number: str) -> BankAccount | None:
        return self.__bank_accounts[account_number]

    def get_all_bank_accounts(self) -> list[BankAccount]:
        return list(self.__bank_accounts.values())

    def add_money(self, account_number: str, money: int | float):
        account = self.__get_account(account_number)
        account.money += money

    def transfer_money(self, from_account_number: str, to_account_number: str, money: int | float):
        from_account_number = self.__get_account(from_account_number)
        to_account_number = self.__get_account(to_account_number)
        if from_account_number.money - money >= 0:
            from_account_number.money -= money
            to_account_number.money += money
        else:
            print("Недостаточно средств на счете отправителя.")

    def external_transfer(self, from_account_number: str, to_external_number: str, money: int | float):
        from_account_number = self.__get_account(from_account_number)
        if from_account_number.money - money >= 0:
            from_account_number.money -= money
            print(f"Банк перевёл {money}$ с вашего счёта {from_account_number.account_number}"
                  f" на внешний счёт {to_external_number}")
        else:
            print("Недостаточно средств на счете отправителя.")


class Controller:
    def __init__(self, data_file_name: str):
        self.data_file_name = data_file_name
        bank_accounts: dict[BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print("Здравствуйте, наш банк открылся!")
        while True:
            print("Выберите действие:", "0. Завершить программу",
                  "1. Открыть новый счёт",
                  "2. Просмотреть открытые счета",
                  "3. Положить деньги на счёт",
                  "4. Перевести деньги между счетами",
                  "5. Совершить платёж", sep='\n')

            answer = int(input())

            match answer:
                case 0:
                    save_accounts(self.bank.get_all_bank_accounts(), self.data_file_name)
                    print("До свидания!")
                    return
                case 1:
                    account = self.bank.open_account(input("Введите ФИО держателя карты : "))
                    print(f"Счёт {account.account_number} создан")
                case 2:
                    print("Все счета:")
                    for account in self.bank.get_all_bank_accounts():
                        print(f"Счёт: {account.account_number}", f"Остаток на счету: {account.money}$",
                              f"Номер карты: {account.card_number}", f"Держатель карты: {account.card_holder}",
                              sep="\n")
                case 3:
                    to_account_number = input("Введите номер счета: ")
                    money = float(input("Введите количество денег: "))
                    self.bank.add_money(to_account_number, money)
                case 4:
                    from_account_number = input("Введите номер счета отправителя: ")
                    to_account_number = input("Введите номер счета получателя: ")
                    money = float(input("Введите количество денег: "))
                    self.bank.transfer_money(from_account_number, to_account_number, money)
                case 5:
                    from_account_number = input("Введите номер счета отправителя: ")
                    to_external_number = input("Введите номер внешнего счета: ")
                    money = float(input("Введите количество денег: "))
                    self.bank.external_transfer(from_account_number, to_external_number, money)
                case _:
                    print("Вы ввели неподдерживаемую команду.")


def save_accounts(bank_accounts: list[BankAccount], file_name: str):
    with sqlite3.connect(file_name) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS bank_accounts(
            card_holder VARCHAR,
            money VARCHAR,
            card_number VARCHAR,
            account_number VARCHAR)""")
        for account in bank_accounts:
            cursor = conn.execute(r"SELECT card_holder FROM bank_accounts WHERE card_holder = ?",
                                  (account.card_holder,))
            if cursor.fetchone():
                pass
            else:
                conn.execute(f"""INSERT INTO bank_accounts (card_holder,money,card_number,account_number)
                VALUES (?,?,?,?)""", (account.card_holder, account.money, account.card_number, account.account_number))
    conn.commit()


def load_accounts(file_name: str):
    try:
        with sqlite3.connect(file_name) as conn:
            cursor = conn.execute("""SELECT * FROM bank_accounts""")
            accounts = cursor.fetchall()
            if accounts:
                return {account[3]: BankAccount(*account) for account in accounts}
            else:
                return {}
    except sqlite3.OperationalError:
        return {}


if __name__ == '__main__':
    controller = Controller('bank_db.db')
    controller.run()
