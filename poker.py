import random
import numpy as np
import matplotlib.pyplot as plt

# Liste mit 52 Zahlen
# 5 Zufallszahlen ziehen
# /13 %13

pulls = 5


def get_colour(pulled_cards):
    colors = []

    for x in pulled_cards:
        colour = x // 13
        colors.append(colour)

    return colors


def get_value(pulled_cards):
    values = []

    for x in pulled_cards:
        value = x % 13
        values.append(value)

    return values


def draw_5_rand_cards(deck):
    random.shuffle(deck)
    rand_cards = deck[:pulls]
    return rand_cards


def is_pair(hand):
    values = [card[0] for card in hand]
    for x in values:
        if values.count(x) == 2:
            return True
    return False


def is_two_pair(hand):
    values = [card[0] for card in hand]
    pair_count = 0
    for value in set(values):
        if values.count(value) == 2:
            pair_count += 1
    return pair_count == 2


def is_triple(hand):
    values = [card[0] for card in hand]
    for x in values:
        if values.count(x) == 3:
            return True
    return False


def is_straight(hand):
    values = [card[0] for card in hand]
    values.sort()
    if values[-1] - values[0] == 4:
        return True
    return False


def is_flush(hand):
    values = [card[1] for card in hand]
    for x in values:
        if values.count(x) == 5:
            return True
    return False


def is_full_house(hand):
    if is_triple(hand) and is_pair(hand):
        return True
    return False


def is_quadruple(hand):
    values = [card[0] for card in hand]
    for x in values:
        if values.count(x) == 4:
            return True
        return False


def is_straight_flush(hand):
    if is_straight(hand) and is_flush(hand):
        return True
    return False


def has_royal_flush(hand):
    values = [card[0] for card in hand]
    values.sort()
    if values == ([8, 9, 10, 11, 12]) and is_flush(hand):
        return True
    return False


def game(repeat):
    cards = np.arange(0, 52)
    combinations_count = {
        'Pair': 0,
        'Two Pairs': 0,
        'Three of a Kind': 0,
        'Four of a Kind': 0,
        'Flush': 0,
        'Straight': 0,
        'Full-House': 0,
        'Straight-Flush': 0,
        'Royal-Flush': 0,
        'No-Hand': 0
    }

    sizes = []
    for _ in range(repeat):
        rand_cards = draw_5_rand_cards(cards)
        hand = list(zip(get_value(rand_cards), get_colour(rand_cards)))
        if is_quadruple(hand):
            combinations_count['Four of a Kind'] += 1
        elif is_full_house(hand):
            combinations_count['Full-House'] += 1
        elif is_flush(hand):
            combinations_count['Flush'] += 1
        elif is_straight(hand):
            combinations_count['Straight'] += 1
        elif is_triple(hand):
            combinations_count['Three of a Kind'] += 1
        elif is_two_pair(hand):
            combinations_count['Two Pairs'] += 1
        elif is_pair(hand):
            combinations_count['Pair'] += 1
        elif is_straight_flush(hand):
            combinations_count['Straight-Flush'] += 1
        elif has_royal_flush(hand):
            combinations_count['Royal-Flush'] += 1
        else:
            combinations_count['No-Hand'] += 1

    for combination, count in combinations_count.items():
        percentage = (count / repeat) * 100
        sizes.append(percentage)
        print(f'{combination}: {percentage:}')

    # Kreisdiagramm erstellen
    labels = combinations_count.keys()
    plt.pie(sizes, labels=labels)
    plt.show()


if __name__ == '__main__':
    game(100000)
