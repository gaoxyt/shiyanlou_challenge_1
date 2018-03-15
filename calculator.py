#!/usr/bin/env python3

import sys

tax      = [0,1500,4500,9000,35000,55000,80000]
tax_rate = [0,0.03,0.1,0.2,0.25,0.3,0.35,0.45]
sub_num  = [0,0,105,555,1005,2755,5505,13505]


if __name__ == '__main__':
	try:
		salary = int(sys.argv[1])
	except:
		print("Parameter Error")
		exit() 
	salary = salary - 3500
	i = 0
	for tmp in tax:
		if salary <= tmp:
			tax_pay = salary * tax_rate[i] - sub_num[i]
			break;
		else:
			i = i + 1

	print(format(tax_pay,".2f"))
	exit()
