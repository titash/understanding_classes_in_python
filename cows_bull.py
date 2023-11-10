import random


def getDigits(num):
    return [int(i) for i in str(num)]


def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num


print(generateNum())

list_of_numbers = getDigits(199)

print(list_of_numbers)
