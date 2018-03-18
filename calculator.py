#!/usr/bin/env python3

import sys

def calc_salary(salary):
	tax = [0,1500,4500,9000,35000,55000,80000]
	tax_rate = [0,0.03,0.1,0.2,0.25,0.3,0.35,0.45]
	sub_num = [0,0,105,555,1005,2755,5505,13505]
	insurance = (0.08,0.02,0.005,0.000,0.000,0.06)

	ins_pay = 0
	for insurance_temp in insurance:
		ins_pay += salary * insurance_temp

	salary_temp = salary - ins_pay -  3500
	i = 0
	for tmp in tax:
		if salary_temp <= tmp:
			tax_pay = salary_temp * tax_rate[i] - sub_num[i]
			break;
		else:
			i = i + 1

	return format(salary - tax_pay - ins_pay,".2f")


if __name__ == '__main__':
	arg_dict = {}
	#if len(sys.argv) < 2:
		#print("Parameter Error")
		#exit()
	for arg in sys.argv[1:]:
		try:
			arg_list = arg.split(':')
			arg_dict[arg_list[0]] = int(arg_list[1])
			#print(arg_dict)
		except:
			print("Parameter Error")
			exit() 
	
	for key,value in arg_dict.items():
		print(key,':',calc_salary(value),sep = '')
		
	exit()
