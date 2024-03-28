def main():
#	x = int(input("What is x? "))
#	y = int(input("Whats is y? "))
	print("x squared is", f"{square():,}")
	print("x plus y is", f"{sum():,}")
	print("x divided by y is", f"{div():,}")

def div(n=2,m=3):
	return round(n / m, 2)

def sum(n=999,m=1):
	return n + m

def square(n=97):
	return pow(n, 2)

main()
