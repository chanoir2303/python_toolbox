def prime(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                print("Not prime")
                break
            else:
                print("Prime")
    else:
        print("Not prime")
         
         
def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)
# [fibonacci(n) for n in range(10)]


def sort_even_and_odd(list):
    even_list = []
    odd_list = []
    for i in list:
        if str(i / 2.0)[-1:] == "0":
            even_list.append(i)
        elif str(i / 2.0)[-1:] == "5":
            odd_list.append(i)

            
def largest_prime_factor(n):
    largest = None
    for i in range(2, n):
        while n % i == 0:
            largest = i
            n //= i
        if n == 1:
            return largest
    if n > 1:
        return n
    
    
def is_palindrome(n):
   # returns true if n is a palindrome
    return str(n) == str(n)[::-1]
