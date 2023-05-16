# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0
num_month = 0

#while principal > 0:
while principal > payment:
	if num_month >= extra_payment_start_month and num_month <= extra_payment_end_month:
		num_month = num_month + 1
		principal = principal * (1 + rate/12) - (payment + extra_payment)
		total_paid = total_paid + payment + extra_payment
		print(num_month, round(total_paid, 2), round(principal, 2))
	else:
		num_month = num_month + 1
		principal = principal * (1 + rate/12) - payment
		total_paid = total_paid + payment
		print(num_month, round(total_paid, 2), round(principal, 2))


print("Total Months, Total paid", num_month, round(total_paid, 4))
