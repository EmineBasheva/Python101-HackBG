from cashdesk import Bill, BillBatch, CashDesk


a = Bill(10)
b = Bill(5)
c = Bill(10)

print(int(a))  # 10
print(str(a))  # "A 10$ bill"

print(a == b)  # False
print(a == c)  # True

money_holder = {}
money_holder[a] = 1

if c in money_holder:
    money_holder[c] = money_holder[c] + 1

print(money_holder)

# ========= batchbil ==========

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

# ========= CashDesk ==========

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()

# We have a total of 390$ in the desk
# We have the following count of bills, sorted in ascending order:
# 10$ bills - 2
# 20$ bills - 1
# 50$ bills - 1
# 100$ bills - 3

bla = {}
a = 3
if a in bla:
    bla[a] += 1
else:
    bla[a] = 1