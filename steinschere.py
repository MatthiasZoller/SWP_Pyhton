import random
import json
from pathlib import Path

statistik_path = Path("statistik.json")


def load_statistik():
    if statistik_path.exists():
        with open(statistik_path, 'r') as file:
            return json.load(file)
    else:
        return {"count_Player": 0, "count_Comp": 0,
                "symbol_counts": {"Schere": 0, "Stein": 0, "Papier": 0, "Echse": 0, "Spock": 0}}


def save_statistik(statistik):
    with open(statistik_path, 'w') as file:
        json.dump(statistik, file)


def schere(com):
    if com == "Stein" or com == "Spock":
        print("Verloren")
        return "comp"
    elif com == "Papier" or com == "Echse":
        print("Gewonnen")
        return "player"
    else:
        print("Unentschieden")
        return "draw"


def stein(com):
    if com == "Papier" or com == "Spock":
        print("Verloren")
        return "comp"
    elif com == "Schere" or com == "Echse":
        print("Gewonnen")
        return "player"
    else:
        print("Unentschieden")
        return "draw"


def papier(com):
    if com == "Schere" or com == "Echse":
        print("Verloren")
        return "comp"
    elif com == "Stein" or com == "Spock":
        print("Gewonnen")
        return "player"
    else:
        print("Unentschieden")
        return "draw"


def echse(com):
    if com == "Stein" or com == "Schere":
        print("Verloren")
        return "comp"
    elif com == "Papier" or com == "Spock":
        print("Gewonnen")
        return "player"
    else:
        print("Unentschieden")
        return "draw"


def spock(com):
    if com == "Echse" or com == "Papier":
        print("Verloren")
        return "comp"
    elif com == "Stein" or com == "Schere":
        print("Gewonnen")
        return "player"
    else:
        print("Unentschieden")
        return "draw"


def symbol_comp():
    symbols = ["Schere", "Stein", "Papier", "Echse", "Spock"]
    return random.choice(symbols)


def play_game():
    input_symbol = input("Wähle zwischen Schere, Stein, Papier, Echse und Spock: ")
    if input_symbol == "Schere":
        return input_symbol, schere(symbol_comp())
    elif input_symbol == "Stein":
        return input_symbol, stein(symbol_comp())
    elif input_symbol == "Papier":
        return input_symbol, papier(symbol_comp())
    elif input_symbol == "Echse":
        return input_symbol, echse(symbol_comp())
    elif input_symbol == "Spock":
        return input_symbol, spock(symbol_comp())


def main():
    statistik = load_statistik()

    while True:
        print("--- Menü ---")
        print("1. Spiel spielen")
        print("2. Statistik anzeigen")
        print("3. Beenden")

        choice = input("Wähle eine Option (1/2/3): ")

        if choice == "1":
            input_symbol, result = play_game()
            print(result)
            if result == "player":
                statistik['count_Player'] += 1
            elif result == "comp":
                statistik['count_Comp'] += 1
            elif result == "draw":
                pass
            statistik['symbol_counts'][input_symbol] += 1
            save_statistik(statistik)

        elif choice == "2":
            print(statistik)

        elif choice == "3":
            break

        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")


2if __name__ == '__main__':
    main()
