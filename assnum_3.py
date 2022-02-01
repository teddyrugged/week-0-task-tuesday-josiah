# n = int(input("Enter the number of rows:"))


# for i in range(1,n):
# 	for j in range(1,n+1):
# 		print
def prime_number(n):
    if n <= 1:
    	return(f"{n} is not a prime number")
    for i in range(2, n+1):
        if (n % i== 0): 
            return(f"{n} is not a prime number")
            print (i)
    else: 
        return(f"{n} is a prime number")

        
print(prime_number(6))