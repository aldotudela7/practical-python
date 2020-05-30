# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start = 60
extra_payment_end = 108
extra_payment = 1000

while principal>0:
    month += 1
    if (month >= extra_payment_start) & (month <= extra_payment_end):
        principal = principal * (1+rate/12) - (payment + extra_payment)
    else:
        principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, total_paid, principal)

print(f'Total paid = {total_paid:0.2f}')
print(f'Total payments = {month}')