import math
import numpy as np
import os
import json
import random
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)


history = []
HISTORY_FILE = "history.json"

# ===================== HELPERS =====================

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "❌ Invalid number")


def format_complex(num):
    if abs(num.imag) < 1e-6:
        return f"{num.real:.6f}"

    sign = "+" if num.imag >= 0 else "-"

    return f"{num.real:.6f} {sign} {abs(num.imag):.6f}j"


def pause():
    input(Fore.YELLOW + "\nPress ENTER to continue...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")



def banner():
    quotes = [
        "Mathematics is the language of the universe.",
        "Numbers rule everything around us.",
        "Pure mathematics is logical beauty.",
        "Solve problems. Build logic. Repeat."
    ]

    clear()

    print(Fore.CYAN + "=" * 65)
    print(Fore.YELLOW + "🧠 ADVANCED EQUATION SOLVER PRO 2026")
    print(Fore.GREEN + random.choice(quotes))
    print(Fore.CYAN + "=" * 65)



def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                data = json.load(f)
                history.extend(data)
            except:
                pass


def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def add_to_history(entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history.append({
        "time": timestamp,
        "result": entry
    })

    save_history()


def show_history():
    if not history:
        print(Fore.RED + "\n📭 No history")
        return

    print(Fore.CYAN + "\n📜 HISTORY")
    print("-" * 60)

    for i, item in enumerate(history, 1):
        print(f"{i}. [{item['time']}] {item['result']}")


def clear_history():
    history.clear()
    save_history()

    print(Fore.GREEN + "✅ History cleared")



def solve_linear():
    print(Fore.CYAN + "\n--- Linear Equation ---")
    print("ax + b = 0")

    a = get_number("a = ")
    b = get_number("b = ")

    if a == 0:
        print(Fore.RED + "❌ a cannot be 0")
        return

    x = -b / a

    print(Fore.GREEN + f"\n✅ x = {x:.6f}")

    add_to_history(f"Linear: x = {x:.6f}")



def solve_quadratic():
    print(Fore.CYAN + "\n--- Quadratic Equation ---")
    print("ax² + bx + c = 0")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")

    if a == 0:
        print(Fore.RED + "❌ Use linear solver")
        return

    d = b**2 - 4*a*c

    print(Fore.YELLOW + f"\nDiscriminant = {d:.6f}")

    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)

        x1 = complex(real, imag)
        x2 = complex(real, -imag)

    print(Fore.GREEN + f"x1 = {format_complex(x1)}")
    print(Fore.GREEN + f"x2 = {format_complex(x2)}")

    add_to_history(
        f"Quadratic: x1={format_complex(x1)}, x2={format_complex(x2)}"
    )




def solve_cubic():
    print(Fore.CYAN + "\n--- Cubic Equation ---")
    print("ax³ + bx² + cx + d = 0")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")
    d = get_number("d = ")

    roots = np.roots([a, b, c, d])

    print(Fore.GREEN + "\n✅ Roots")

    for i, root in enumerate(roots, 1):
        print(f"x{i} = {format_complex(root)}")

    add_to_history(f"Cubic roots = {roots.tolist()}")


# ===================== POLYNOMIAL =====================

def solve_polynomial():
    print(Fore.CYAN + "\n--- Polynomial Solver ---")
    print("Example: 1 -6 11 -6")

    coeffs = input("\nCoefficients: ").split()

    try:
        coeffs = [float(c) for c in coeffs]
    except:
        print(Fore.RED + "❌ Invalid coefficients")
        return

    roots = np.roots(coeffs)

    print(Fore.GREEN + "\n✅ Roots")

    for i, root in enumerate(roots, 1):
        print(f"x{i} = {format_complex(root)}")

    add_to_history(f"Polynomial roots = {roots.tolist()}")


# ===================== SYSTEM SOLVER =====================

def solve_system():
    print(Fore.CYAN + "\n--- 2x2 System Solver ---")

    print("\na1*x + b1*y = c1")
    print("a2*x + b2*y = c2")

    a1 = get_number("a1 = ")
    b1 = get_number("b1 = ")
    c1 = get_number("c1 = ")

    a2 = get_number("a2 = ")
    b2 = get_number("b2 = ")
    c2 = get_number("c2 = ")

    A = np.array([
        [a1, b1],
        [a2, b2]
    ])

    B = np.array([c1, c2])

    det = np.linalg.det(A)

    if abs(det) < 1e-10:
        print(Fore.RED + "❌ No unique solution")
        return

    x, y = np.linalg.solve(A, B)

    print(Fore.GREEN + f"\n✅ x = {x:.6f}")
    print(Fore.GREEN + f"✅ y = {y:.6f}")

    add_to_history(f"System solution = ({x:.6f}, {y:.6f})")


# ===================== FACTORIAL =====================

def factorial_calculator():
    print(Fore.CYAN + "\n--- Factorial Calculator ---")

    n = int(get_number("n = "))

    if n < 0:
        print(Fore.RED + "❌ Cannot use negative numbers")
        return

    result = math.factorial(n)

    print(Fore.GREEN + f"\n✅ {n}! = {result}")

    add_to_history(f"{n}! = {result}")


# ===================== PRIME CHECKER =====================

def prime_checker():
    print(Fore.CYAN + "\n--- Prime Checker ---")

    n = int(get_number("Number = "))

    if n < 2:
        print(Fore.RED + "❌ Not prime")
        return

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(Fore.RED + f"❌ {n} is NOT prime")
            return

    print(Fore.GREEN + f"✅ {n} is PRIME")

    add_to_history(f"Prime checked = {n}")


# ===================== RANDOM MATH FACT =====================

def math_fact():
    facts = [
        "Zero is the only number that cannot be represented in Roman numerals.",
        "A circle has infinite lines of symmetry.",
        "Pi is irrational.",
        "Prime numbers never end.",
        "The word hundred comes from old Norse meaning 120."
    ]

    print(Fore.MAGENTA + "\n📘 RANDOM MATH FACT")
    print(Fore.YELLOW + random.choice(facts))


# ===================== MENU =====================

def show_menu():
    print("\n" + "=" * 60)

    print("1  - Linear Solver")
    print("2  - Quadratic Solver")
    print("3  - Cubic Solver")
    print("4  - Polynomial Solver")
    print("5  - System Solver")
    print("6  - Factorial Calculator")
    print("7  - Prime Checker")
    print("8  - Show History")
    print("9  - Clear History")
    print("10 - Random Math Fact")
    print("0  - Exit")

    print("=" * 60)


# ===================== MAIN =====================

def main():
    load_history()

    banner()

    while True:
        show_menu()

        choice = input(Fore.CYAN + ">> ").strip()

        if choice == "1":
            solve_linear()

        elif choice == "2":
            solve_quadratic()

        elif choice == "3":
            solve_cubic()

        elif choice == "4":
            solve_polynomial()

        elif choice == "5":
            solve_system()

        elif choice == "6":
            factorial_calculator()

        elif choice == "7":
            prime_checker()

        elif choice == "8":
            show_history()

        elif choice == "9":
            clear_history()

        elif choice == "10":
            math_fact()

        elif choice == "0":
            print(Fore.GREEN + "\n👋 Goodbye")
            break

        else:
            print(Fore.RED + "❌ Invalid option")

        pause()


if __name__ == "__main__":
    main()
