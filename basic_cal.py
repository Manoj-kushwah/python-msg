def main():
	enter_values()

def cal_val(o, v1, v2):
	switcher={
		'+': v1+v2,
		'-': v1-v2,
		'*': v1*v2,
		'/': v1/v2,
	}
	return switcher.get(o)


def enter_values():
	a = input("Enter number -> a = ")
	if type(a) == int:
		b = raw_input("Enter any one oprator '+,-,*,/' -> b : ")
		if type(b) == str:
			c = input("Enter number -> c = ")
			if type(c) == int:
				print "a %s c = %d" %(b, cal_val(b, a, c))
			else:
				print "Wrronge value for c."
		else:
			print "Wrronge value for b."
	else:
		print  "Wrronge value for a."


if __name__ == "__main__":
	main()