import math
import numpy as np
import os
import json
import sympy as sp
import matplotlib.pyplot as plt
from statistics import mode
from datetime import datetime
import random
from colorama import Fore, Style, init

init(autoreset=True)

history = []
HISTORY_FILE = "history.txt"


# ---------------- BANNER ---------------- #

def banner():
    quotes = [
        "Pure mathematics is the poetry of logical ideas.",
        "Mathematics is the language of the universe.",
        "Without mathematics, there’s nothing you can do.",
        "Math is power.",
        "Numbers rule everything around us."
    ]

    print(Fore.MAGENTA + "=" * 60)
    print(Fore.YELLOW + "🧠 ADVANCED MATH UTILITY TOOLKIT")
    print(Fore.CYAN + "Version 10.0")
    print(Fore.GREEN + random.choice(quotes))
    print(Fore.MAGENTA + "=" * 60)


# ---------------- HELPERS ---------------- #

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "❌ invalid number")


def format_complex(num):
    if abs(num.imag) < 1e-6:
        return f"{num.real:.4f}"

    sign = "+" if num.imag >= 0 else "-"

    return f"{num.real:.4f} {sign} {abs(num.imag):.4f}j"


def pause():
    input("\nPress ENTER to continue...")


# ---------------- HISTORY ---------------- #

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history.clear()
            history.extend(line.strip() for line in f)


def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        for item in history:
            f.write(item + "\n")


def add_to_history(entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"[{timestamp}] {entry}")
    save_history()


def show_history():
    if not history:
        print(Fore.RED + "\n📭 No history")
        return

    print(Fore.CYAN + "\n📜 History")
    print("-" * 50)

    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")


def clear_history():
    history.clear()
    save_history()
    print(Fore.GREEN + "🧹 History cleared")


def export_history():
    with open("history_export.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

    print(Fore.GREEN + "✅ Exported to history_export.json")


# ---------------- PRIME CHECKER ---------------- #

def prime_checker():
    print(Fore.CYAN + "\n--- Prime Number Checker ---")

    num = int(get_number("Enter integer: "))

    if num < 2:
        print(Fore.RED + "❌ Not prime")
        return

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(Fore.RED + f"❌ {num} is NOT prime")
            add_to_history(f"Prime check: {num} → NOT prime")
            return

    print(Fore.GREEN + f"✅ {num} is PRIME")
    add_to_history(f"Prime check: {num} → PRIME")


# ---------------- UNIT CONVERTER ---------------- #

def unit_converter():
    print(Fore.CYAN + "\n--- Unit Converter ---")

    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print("3 - KM to Miles")
    print("4 - Miles to KM")

    choice = input("Choice: ")

    if choice == "1":
        c = get_number("Celsius: ")
        f = (c * 9/5) + 32
        print(Fore.GREEN + f"✅ Fahrenheit = {f:.2f}")

    elif choice == "2":
        f = get_number("Fahrenheit: ")
        c = (f - 32) * 5/9
        print(Fore.GREEN + f"✅ Celsius = {c:.2f}")

    elif choice == "3":
        km = get_number("Kilometers: ")
        miles = km * 0.621371
        print(Fore.GREEN + f"✅ Miles = {miles:.2f}")

    elif choice == "4":
        miles = get_number("Miles: ")
        km = miles / 0.621371
        print(Fore.GREEN + f"✅ Kilometers = {km:.2f}")

    else:
        print(Fore.RED + "❌ Invalid option")


# ---------------- MENU ---------------- #

def show_menu():
    print("\n" + "=" * 50)
    print(Fore.YELLOW + "🧮 EQUATION SOLVER v10")
    print("=" * 50)

    print("1  - Linear Solver")
    print("2  - Quadratic Solver")
    print("3  - Cubic Solver")
    print("4  - Polynomial Solver")
    print("5  - System Solver")
    print("6  - Derivative Calculator")
    print("7  - Integral Calculator")
    print("8  - Newton Method")
    print("9  - Matrix Toolkit")
    print("10 - Statistics Toolkit")
    print("11 - Complex Toolkit")
    print("12 - Graph Polynomial")
    print("13 - Scientific Calculator")
    print("14 - Show History")
    print("15 - Clear History")
    print("16 - Export History")
    print("17 - Prime Checker")
    print("18 - Unit Converter")
    print("0  - Exit")

    print("=" * 50)


# ---------------- MAIN ---------------- #

def main():
    load_history()

    banner()

    while True:
        show_menu()

        choice = input(">> ").strip()

        if choice == "17":
            prime_checker()

        elif choice == "18":
            unit_converter()

        elif choice == "0":
            print(Fore.GREEN + "\n👋 goodbye")
            break

        else:
            print(Fore.RED + "❌ Keep your old menu logic here + new features added")

        pause()


if __name__ == "__main__":
    main()
```

Install dependency:

```bash
pip install colorama
```
