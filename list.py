def generate(start, end, step):
    x = [i for i in range(start, end, step)]
    return x


def reverse(list):
    list = list[:]
    x = []
    while list:
        x.append(list.pop())
    return x


def is_in(word, list):
    x = True
    if word in list:
        x = True
    return x
