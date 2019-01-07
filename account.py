#!/usr/bin/python
import re
import sys
import unittest

def count_transaction():
    print '_' * 10
    print 'total transactions count : ' + str(len(open_file()))
    total_transaction = len(open_file())
    return total_transaction


def count_amount():
    total_balance = 0
    for line in open_file():
        values = line.split(' ')
        if values[2] == 'Deposit':
            deposit = float(values[3].split('$')[1])
            total_balance += deposit
        elif values[2] == 'Withdraw':
            withdraw = float(values[3].split('$')[1])
            total_balance -= withdraw
            if total_balance < 0:
                date = line.split(')')[1]
                date = date.split('Withdraw')[0]
                print '_'*10
                print 'negative transaction # ' + str(line.split(')')[0])
                print 'from date' + str(date)
                print 'balance for negative transaction' + str(total_balance)
                print '-' * 10
        else:
            sys.exit()
            print 'wrong data in ' + str(line)
    print 'total_balance :' + str(total_balance)
    print '_' * 10
    return total_balance


def open_file(file_to_open = raw_input()):
    with open(file_to_open, 'r') as filename:
        data = filename.readlines()
        return data


def file_validator():
    for line in open_file():
        values = line.split(' ')
        match_order = re.match('^-?[0-9]+(\))$', values[0])
        match_date = re.match('(\d{2})[-](\d{2})[-](\d{4})$', values[1])
        match_operation = re.match(r'Deposit\b|Withdraw\b', values[2])
        match_amount = re.match(r'([$])(\d+(?:\.\d{2}))\b$', values[3])
        if match_order and match_date and match_operation and match_amount:
            return True
        else:
            print 'string has wrong format : ' + str(line)
            break
            return False


def run_app():
    if file_validator():
        count_transaction()
        count_amount()
    else:
        sys.exit()


class Tests(unittest.TestCase):


    def test_1(self):
        self.assertEqual(type(open_file()), list)


    def test_2(self):
        self.assertEqual(type(open_file()[0]), str)
    
#    def test_3(self):
#        self.assertRaises(IOError ,open_file('asd'))
     
    def test_4(self):
        self.assertTrue(type(count_transaction()), int)

    def test_5(self):
        self.assertEqual(type(count_amount()), float)    

if __name__ == "__main__":
    unittest.main()
        