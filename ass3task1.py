#recursive factorial function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

#user input
number=int(input("enter the number:"))
#output
print('factorial of',number,'is:',factorial(number))
