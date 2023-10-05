import random
import matplotlib.pyplot as m

liste = list(range(1, 46))
dict = {}


def get_random_number():
    last_num = 44
    while last_num > 39:
        rand_num = random.randint(0, last_num)
        liste[rand_num], liste[last_num] = liste[last_num], liste[rand_num]
        last_num -= 1

        value = liste[last_num + 1]
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1


def show():
    zahlen = list(dict.keys())
    haeufigkeiten = list(dict.values())
    m.bar(zahlen, haeufigkeiten)
    m.xlabel('Zahlen')
    m.ylabel('Häufigkeit')
    m.title('Häufigkeit der Zahlen')
    m.show()


if __name__ == '__main__':

    for _ in range(1000):
        get_random_number()

    for i in range(-6, 0):
        print(liste[i])

    print(dict)

    show()
