class Bill:
    
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.amount.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BillBatch:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum(self.bills)

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:

    def __init__(self):
        self.all_bills = {}

    def __add_to_all_bills(self, bill):
        if bill in self.all_bills:
            self.all_bills[bill] += 1
        else:
            self.all_bills[bill] = 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.__add_to_all_bills(money)
        elif isinstance(money, BillBatch):
            for bill in money:
                self.__add_to_all_bills(bill)

    def total(self):
        return sum([int(bill) * self.all_bills[bill] for bill in self.all_bills])

    def inspect(self):
        for bill in self.all_bills:
            print("{}$ bills - {}".format(bill, self.all_bills[bill]))