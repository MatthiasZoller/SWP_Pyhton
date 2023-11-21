import random
import numpy as np
import matplotlib.pyplot as plt


# Liste mit 52 Zahlen
# 5 Zufallszahlen ziehen
# /13 %13


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


def draw_5_rand_cards(deck, pulls):
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

    for i in range(len(values) - 1):
        if values[i] + 1 != values[i + 1]:
            return False

    return True


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


