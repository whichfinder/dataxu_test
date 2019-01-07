import re
import sys

def count_transaction():
	print 'total transactions count : ' + str(len(open_file()))

def count_amount():
	total_balance = 0
	for line in open_file():
		values = line.split(' ')
		if values[2] == 'Deposit':
			deposit = float(values[3].split('$')[1])
			total_balance = total_balance + deposit

		elif values[2] == 'Withdraw':
			withdraw = float(values[3].split('$')[1])
			total_balance = total_balance - withdraw

		else:
			print 'error while parsing'
		print total_balance	
		return total_balance

def open_file():
	with open('transaction.txt', 'r') as file:
		data = file.readlines()
    	return data

count_transaction()
count_amount()