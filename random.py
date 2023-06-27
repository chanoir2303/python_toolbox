def fizzbuzz(n):
    for i in range(0, n):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else: print(i)


def palindrome(word):
    y = []
    for i in range(len(word)):
        y.append(word[i])
    if y == y[::-1]:
        print('Palindrome')
    else:
        print('Not palindrome')
    
