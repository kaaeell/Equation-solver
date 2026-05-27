import math
import numpy as np
import os
import json
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ===================== HISTORY =====================

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


def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "🧠 ADVANCED EQUATION SOLVER 2026")
    print(Fore.GREEN + "Linear • Quadratic • Cubic • Polynomial • Systems")
    print(Fore.CYAN + "=" * 60)

# ===================== HISTORY FUNCTIONS =====================

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

    print(Fore.CYAN + "\n📜 History")
    print("-" * 50)

    for i, item in enumerate(history, 1):
        print(f"{i}. [{item['time']}] {item['result']}")

# ===================== LINEAR SOLVER =====================

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

    add_to_history(f"Linear → x = {x:.6f}")

# ===================== QUADRATIC SOLVER =====================

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
        f"Quadratic → x1={format_complex(x1)}, x2={format_complex(x2)}"
    )

# ===================== CUBIC SOLVER =====================

def solve_cubic():
    print(Fore.CYAN + "\n--- Cubic Equation Solver ---")
    print("ax³ + bx² + cx + d = 0")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")
    d = get_number("d = ")

    coeffs = [a, b, c, d]

    roots = np.roots(coeffs)

    print(Fore.GREEN + "\n✅ Roots")

    for i, root in enumerate(roots, 1):
        print(f"x{i} = {format_complex(root)}")

    add_to_history(f"Cubic → {roots.tolist()}")

# ===================== POLYNOMIAL SOLVER =====================

def solve_polynomial():
    print(Fore.CYAN + "\n--- Polynomial Solver ---")
    print("Example: 2x² + 3x + 1 → 2 3 1")

    coeffs = input("\nCoefficients: ").split()

    try:
        coeffs = [float(x) for x in coeffs]
    except ValueError:
        print(Fore.RED + "❌ Numbers only")
        return

    roots = np.roots(coeffs)

    print(Fore.GREEN + "\n✅ Roots")

    for i, root in enumerate(roots, 1):
        print(f"x{i} = {format_complex(root)}")

    add_to_history(f"Polynomial → {roots.tolist()}")

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

    solution = np.linalg.solve(A, B)

    x, y = solution

    print(Fore.GREEN + f"\n✅ x = {x:.6f}")
    print(Fore.GREEN + f"✅ y = {y:.6f}")

    add_to_history(f"System → x={x:.6f}, y={y:.6f}")

# ===================== MENU =====================

def show_menu():
    print("\n" + "=" * 50)
    print(Fore.YELLOW + "🧮 EQUATION SOLVER MENU")
    print("=" * 50)

    print("1 - Linear Solver")
    print("2 - Quadratic Solver")
    print("3 - Cubic Solver")
    print("4 - Polynomial Solver")
    print("5 - System Solver")
    print("6 - Show History")
    print("0 - Exit")

    print("=" * 50)

# ===================== MAIN =====================

def main():
    load_history()

    banner()

    while True:
        show_menu()

        choice = input(">> ").strip()

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
            show_history()

        elif choice == "0":
            print(Fore.GREEN + "\n👋 Goodbye")
            break

        else:
            print(Fore.RED + "❌ Invalid option")

        pause()


if __name__ == "__main__":
    main()
