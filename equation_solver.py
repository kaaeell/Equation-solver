import math
import numpy as np
import os

# 🧠 Equation Solver v6
# clean, persistent, and actually useful

history = []
HISTORY_FILE = "history.txt"


# ---------------- UTILITIES ---------------- #

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ please enter a valid number")


def format_complex(num):
    if abs(num.imag) < 1e-6:
        return f"{num.real:.2f}"
    return f"{num.real:.2f} + {num.imag:.2f}j"


# ---------------- HISTORY ---------------- #

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history.clear()  # prevent duplicates
            history.extend(line.strip() for line in f)


def save_history():
    with open(HISTORY_FILE, "w") as f:
        for item in history:
            f.write(item + "\n")


def add_to_history(entry):
    history.append(entry)
    save_history()


def show_history():
    if not history:
        print("\n📭 no history yet...")
        return

    print("\n📜 History:")
    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")


def clear_history():
    history.clear()
    save_history()
    print("🧹 history cleared!")


# ---------------- SOLVERS ---------------- #

def solve_linear():
    print("\n--- Linear Equation: ax + b = 0 ---")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")

    if a == 0:
        print("❌ no solution (a cannot be 0)")
        return

    x = -b / a
    print(f"✅ Solution: x = {x:.2f}")
    add_to_history(f"Linear → x = {x:.2f}")


def solve_quadratic():
    print("\n--- Quadratic Equation: ax² + bx + c = 0 ---")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")

    if a == 0:
        print("❌ this becomes linear... try again")
        return

    d = b**2 - 4*a*c
    print(f"Discriminant = {d:.2f}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"✅ x1 = {x1:.2f}, x2 = {x2:.2f}")
        add_to_history(f"Quadratic → x1={x1:.2f}, x2={x2:.2f}")

    elif d == 0:
        x = -b / (2*a)
        print(f"✅ x = {x:.2f}")
        add_to_history(f"Quadratic → x={x:.2f}")

    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)

        x1 = complex(real, imag)
        x2 = complex(real, -imag)

        print("✅ Complex solutions:")
        print(f"x1 = {format_complex(x1)}")
        print(f"x2 = {format_complex(x2)}")

        add_to_history(
            f"Quadratic → x1={format_complex(x1)}, x2={format_complex(x2)}"
        )


def solve_cubic():
    print("\n--- Cubic Equation: ax³ + bx² + cx + d = 0 ---")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")
    d = get_number("Enter d: ")

    if a == 0:
        print("❌ this is NOT a cubic equation")
        return

    roots = np.roots([a, b, c, d])

    print("✅ Solutions:")
    formatted = []

    for i, r in enumerate(roots, 1):
        clean = format_complex(r)
        formatted.append(clean)
        print(f"x{i} = {clean}")

    add_to_history(f"Cubic → {formatted}")


def solve_polynomial():
    print("\n--- Polynomial Solver (any degree) ---")
    print("Example: 2x² + 3x + 1 → enter: 2 3 1")

    coeffs = input("Enter coefficients: ").strip().split()

    try:
        coeffs = [float(c) for c in coeffs]
    except ValueError:
        print("❌ invalid input")
        return

    if len(coeffs) < 2:
        print("❌ need at least 2 coefficients")
        return

    roots = np.roots(coeffs)

    print("✅ Solutions:")
    formatted = []

    for i, r in enumerate(roots, 1):
        clean = format_complex(r)
        formatted.append(clean)
        print(f"x{i} = {clean}")

    add_to_history(f"Polynomial → {formatted}")


# ---------------- MENU ---------------- #

def show_menu():
    print("\nChoose an option:")
    print("1 - Linear equation")
    print("2 - Quadratic equation")
    print("3 - Cubic equation")
    print("4 - Polynomial (any degree)")
    print("5 - Show history")
    print("6 - Clear history")
    print("7 - Exit")


def main():
    load_history()

    print("🧠 Equation Solver v6")
    print("clean, smart, and remembers everything 😎\n")

    while True:
        show_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            solve_linear()
        elif choice == "2":
            solve_quadratic()
        elif choice == "3":
            solve_cubic()
        elif choice == "4":
            solve_polynomial()
        elif choice == "5":
            show_history()
        elif choice == "6":
            clear_history()
        elif choice == "7":
            print("👋 done. go touch some grass 🌱")
            break
        else:
            print("❌ invalid choice")


if __name__ == "__main__":
    main()
