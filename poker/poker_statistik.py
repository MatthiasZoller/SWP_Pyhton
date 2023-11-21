import poker as p
import numpy as np
import matplotlib.pyplot as plt


def game(repeat, pulls):
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
        rand_cards = p.draw_5_rand_cards(cards, pulls)
        hand = list(zip(p.get_value(rand_cards), p.get_colour(rand_cards)))
        if p.is_quadruple(hand):
            combinations_count['Four of a Kind'] += 1
        elif p.is_full_house(hand):
            combinations_count['Full-House'] += 1
        elif p.is_flush(hand):
            combinations_count['Flush'] += 1
        elif p.is_straight(hand):
            combinations_count['Straight'] += 1
        elif p.is_triple(hand):
            combinations_count['Three of a Kind'] += 1
        elif p.is_two_pair(hand):
            combinations_count['Two Pairs'] += 1
        elif p.is_pair(hand):
            combinations_count['Pair'] += 1
        elif p.is_straight_flush(hand):
            combinations_count['Straight-Flush'] += 1
        elif p.has_royal_flush(hand):
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
