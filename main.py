def score(total, correct, wrong):
    _correct  = 2
    _wrong = 1
    _total = (correct * _correct) + wrong
    return (_total / (total * 2)) *  100


def fizzbuzz(n):
    for i in range(0, n):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else: print(i)



def multiply(x, y):
    z = 0
    for i in  range(0, y):
        z += x
    return z


def generate_list(start, end, step):
    x = [i for i in range(start, end, step)]
    return x


def reverse_list(list):
    list = list[:]
    x = []
    while list:
        x.append(list.pop())
    return x


def is_in_list(n, list):
    x = True
    if n in list:
        x = True
    else:
        x = False
    return x


def intersection(list1, list2):
    list = []
    for i in list1:
        if is_in_list(i, list):
            continue
        for j in list2:
            if i == j:
                list.append(i)
                break
    return list


def palindrome(word):
    y = []
    for i in range(len(word)):
        y.append(word[i])
    if y == y[::-1]:
        print('Palindrome')
    else:
        print('Not palindrome')
    
