import math
import numpy as np
import os

# equation solver v7 - for math homework
# saves equations so i don't have to retype everything

history = []
HISTORY_FILE = "history.txt"


# ---------------- HELPER STUFF ---------------- #

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ not a number")


def format_complex(num):
    if abs(num.imag) < 1e-6:
        return f"{num.real:.2f}"
    return f"{num.real:.2f} + {num.imag:.2f}j"


# ---------------- HISTORY ---------------- #

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history.clear()
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
        print("\n📭 no history yet")
        return

    print("\n📜 Past equations:")
    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")


def clear_history():
    history.clear()
    save_history()
    print("🧹 cleared")


# ---------------- MATH ---------------- #

def solve_linear():
    print("\n--- Linear: ax + b = 0 ---")

    a = get_number("a = ")
    b = get_number("b = ")

    if a == 0:
        print("❌ a can't be 0")
        return

    x = -b / a
    print(f"✅ x = {x:.2f}")
    add_to_history(f"Linear {a}x + {b} = 0  →  x = {x:.2f}")


def solve_quadratic():
    print("\n--- Quadratic: ax² + bx + c = 0 ---")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")

    if a == 0:
        print("❌ that's linear, use option 1")
        return

    d = b**2 - 4*a*c
    print(f"Discriminant = {d:.2f}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"✅ x1 = {x1:.2f}, x2 = {x2:.2f}")
        add_to_history(f"Quadratic {a}x²+{b}x+{c}=0 → x1={x1:.2f}, x2={x2:.2f}")

    elif d == 0:
        x = -b / (2*a)
        print(f"✅ x = {x:.2f} (double root)")
        add_to_history(f"Quadratic {a}x²+{b}x+{c}=0 → x={x:.2f}")

    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)

        x1 = complex(real, imag)
        x2 = complex(real, -imag)

        print("✅ Complex roots:")
        print(f"x1 = {format_complex(x1)}")
        print(f"x2 = {format_complex(x2)}")

        add_to_history(
            f"Quadratic {a}x²+{b}x+{c}=0 → x1={format_complex(x1)}, x2={format_complex(x2)}"
        )


def solve_cubic():
    print("\n--- Cubic: ax³ + bx² + cx + d = 0 ---")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")
    d = get_number("d = ")

    if a == 0:
        print("❌ that's not cubic, try option 2")
        return

    roots = np.roots([a, b, c, d])

    print("✅ Roots:")
    formatted = []

    for i, r in enumerate(roots, 1):
        clean = format_complex(r)
        formatted.append(clean)
        print(f"x{i} = {clean}")

    add_to_history(f"Cubic → {formatted}")


def solve_polynomial():
    print("\n--- Polynomial Solver ---")
    print("Example: 2x² + 3x + 1 → type: 2 3 1")
    print("For 4x³ - 2x + 7 → type: 4 0 -2 7 (include zeros)")

    coeffs = input("Enter coefficients (space separated): ").strip().split()

    try:
        coeffs = [float(c) for c in coeffs]
    except ValueError:
        print("❌ numbers only")
        return

    if len(coeffs) < 2:
        print("❌ need at least 2 numbers")
        return

    roots = np.roots(coeffs)

    print("✅ Solutions:")
    formatted = []

    for i, r in enumerate(roots, 1):
        clean = format_complex(r)
        formatted.append(clean)
        print(f"x{i} = {clean}")

    add_to_history(f"Polynomial {coeffs} → {formatted}")


def solve_system():
    print("\n--- System of 2 Equations ---")
    print("Form: a1*x + b1*y = c1")
    print("      a2*x + b2*y = c2")
    
    a1 = get_number("a1 = ")
    b1 = get_number("b1 = ")
    c1 = get_number("c1 = ")
    
    a2 = get_number("a2 = ")
    b2 = get_number("b2 = ")
    c2 = get_number("c2 = ")
    
    det = a1*b2 - a2*b1
    
    if det == 0:
        print("❌ No unique solution (parallel lines)")
        return
    
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    
    print(f"✅ x = {x:.2f}, y = {y:.2f}")
    add_to_history(f"System: x={x:.2f}, y={y:.2f}")


def derivative_check():
    print("\n--- Derivative Checker ---")
    print("Polynomial like: 3x² + 2x + 1")
    
    coeffs = input("Enter coefficients (highest degree first): ").strip().split()
    
    try:
        coeffs = [float(c) for c in coeffs]
    except ValueError:
        print("❌ numbers only")
        return
    
    if len(coeffs) < 2:
        print("❌ need at least 2 coefficients")
        return
    
    deriv = []
    degree = len(coeffs) - 1
    
    for i in range(degree):
        deriv.append(coeffs[i] * (degree - i))
    
    print("Derivative: ", end="")
    for i, coef in enumerate(deriv):
        power = degree - i - 1
        if power > 1:
            print(f"{coef:.2f}x^{power}", end="")
        elif power == 1:
            print(f"{coef:.2f}x", end="")
        else:
            print(f"{coef:.2f}", end="")
        
        if i < len(deriv)-1 and deriv[i+1] >= 0:
            print(" + ", end="")
        elif i < len(deriv)-1:
            print(" - ", end="")
    
    print("\n")


# ---------------- MENU ---------------- #

def show_menu():
    print("\n" + "="*40)
    print("1 - Linear (ax + b = 0)")
    print("2 - Quadratic (ax² + bx + c = 0)")
    print("3 - Cubic (ax³ + bx² + cx + d = 0)")
    print("4 - Polynomial (any degree)")
    print("5 - System of 2 equations")
    print("6 - Derivative checker")
    print("7 - Show history")
    print("8 - Clear history")
    print("9 - Exit")
    print("="*40)


def main():
    load_history()

    print("🧮 Equation Solver v7")
    print("for when you're too lazy to do math by hand")

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
            derivative_check()
        elif choice == "7":
            show_history()
        elif choice == "8":
            clear_history()
        elif choice == "9":
            print("\n👋 bye")
            break
        else:
            print("❌ not an option")


if __name__ == "__main__":
    main()
