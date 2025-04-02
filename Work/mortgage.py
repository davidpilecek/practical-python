# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11

    if principal < payment:
        payment = principal
        principal -= payment 
    else:
        principal = principal * (1+rate/12) - payment 

    total_paid = total_paid + payment
    months += 1


    print(f'Months: {months}, Total: ${total_paid:0.2f}, Principal: ${principal:0.2f}')