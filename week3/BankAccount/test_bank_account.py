import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def test_create_new_BankAccount_class(self):
        bank_account = BankAccount("Rado", 0, "$")
        self.assertTrue(isinstance(bank_account, BankAccount))

    def test_str_dunder_for_bank_account_with_dollar(self):
        bank_account = BankAccount("Rado", 10, "$")
        self.assertEqual(str(bank_account), 'Bank account for Rado with balance of 10$')

    def test_str_dunder_for_bank_account_with_BGN(self):
        ivo = BankAccount("Ivo", 0, "BGN")
        self.assertEqual(str(ivo), 'Bank account for Ivo with balance of 0BGN')

    def test_int_dunder(self):
        bank_account = BankAccount("Rado", 1000, "$")
        self.assertEqual(int(bank_account), 1000)

    def test_balance(self):
        bank_account = BankAccount("Rado", 10, "$")
        self.assertEqual(bank_account.balance(), 10)

    def test_deposit(self):
        bank_account = BankAccount("Rado", 0, "$")
        bank_account.deposit(1000)
        self.assertEqual(int(bank_account), 1000)

    def test_withdraw_with_right_value(self):
        bank_account = BankAccount("Rado", 1000, "$")
        self.assertTrue(bank_account.withdraw(500))

    def test_balance_after_withdraw_with_right_value(self):
        bank_account = BankAccount("Rado", 1000, "$")
        bank_account.withdraw(500)
        self.assertEqual(bank_account.balance(), 500)

    def test_withdraw_with_wrong_value(self):
        bank_account = BankAccount("Rado", 500, "$")
        self.assertFalse(bank_account.withdraw(600))

    def test_balance_after_withdraw_with_wrong_value(self):
        bank_account = BankAccount("Rado", 500, "$")
        bank_account.withdraw(600)
        self.assertEqual(bank_account.balance(), 500)

    def test_transfer_to_with_same_currencies_and_check_rado_balance(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        rado.transfer_to(ivo, 400)
        self.assertEqual(rado.balance(), 600)

    def test_transfer_to_with_same_currencies_and_check_ivo_balance(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        rado.transfer_to(ivo, 400)
        self.assertEqual(ivo.balance(), 400)

    def test_transfer_to_with_same_currencies(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        self.assertTrue(rado.transfer_to(ivo, 400))

    def test_transfer_to_with_different_currencies(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "$")
        self.assertFalse(rado.transfer_to(ivo, 400))

    # def test_history(self):
    #   account = BankAccount("Rado", 0, "$")
    #   account.deposit(1000)
    #   account.balance()
    #   a = str(account)
    #   b = int(account)

    #   answer = ['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$']
    #   self.assertEqual(account.history(), answer)


if __name__ == '__main__':
    unittest.main()
