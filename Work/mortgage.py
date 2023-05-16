# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_month = 1

while principal > 0:
	while num_month <= 12:
		principal = principal * (1 + rate/12) - (payment + 1000)
		total_paid = total_paid + payment + 1000
		num_month = num_month + 1
	else:
		principal = principal * (1 + rate/12) - payment
		total_paid = total_paid + payment
		num_month = num_month + 1

print("Total Months, Total paid", num_month, round(total_paid, 4))
