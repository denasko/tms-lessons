import random
import json


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
        self.__bank_accounts: dict[str, BankAccount] = {account.account_number: account for account in
                                                        bank_accounts or []}

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
        bank_accounts: list[BankAccount] = load_accounts(data_file_name)
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
                    account = self.bank.open_account(input("Введите ФИО: "))
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


def convert_bank_account_to_dict(account: BankAccount) -> dict:
    return {"card_holder": account.card_holder,
            "money": account.money,
            "card_number": account.account_number,
            "account_number": account.card_number}


def save_accounts(bank_accounts: list[BankAccount], file_name: str):
    data = [convert_bank_account_to_dict(account) for account in bank_accounts]
    with open(file_name, "w") as file:
        json.dump(data, file, indent=2)


def load_accounts(file_name: str) -> list[BankAccount] | list[None]:
    try:
        with open(file_name) as file:
            return [BankAccount(**data) for data in json.load(file)]
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
