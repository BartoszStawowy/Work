import random

def random_number_gen(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

def IDcard_generator():
    letters = {
        "A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16,
        "H":17, "I":18, "J":19,"K":20, "L":21, "M":22, "N":23, "O":24,
        "P":25, "Q":26, "R":27, "S":28, "T":29,
		"U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35
    }
    chosen_letters = random.choice(list(letters.keys()))\
                     +random.choice(list(letters.keys()))\
                     +random.choice(list(letters.keys()))
    digits = data_generators.random_number_gen(5)
    sumControl = letters.get(chosen_letters[0])*7 + letters.get(chosen_letters[1])*3\
                 +letters.get(chosen_letters[2])\
                +int(str(digits)[0])*7 + int(str(digits)[1])*3 \
                 + int(str(digits)[2])+int(str(digits)[3])*7+ int(str(digits)[4])*3
    IdCard = chosen_letters + str(sumControl%10) + str(digits)
    return IdCard
