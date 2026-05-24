import math
import numpy as np
import os
import json
import sympy as sp
import matplotlib.pyplot as plt
from statistics import mode

history = []
HISTORY_FILE = "history.txt"


# ---------------- HELPERS ---------------- #

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ invalid number")


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
    history.append(entry)
    save_history()


def show_history():
    if not history:
        print("\n📭 No history")
        return

    print("\n📜 History")
    print("-" * 50)

    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")


def clear_history():
    history.clear()
    save_history()
    print("🧹 History cleared")


def export_history():
    with open("history_export.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

    print("✅ Exported to history_export.json")


# ---------------- EQUATION SOLVERS ---------------- #

def solve_linear():
    print("\n--- Linear Equation ---")
    print("ax + b = 0")

    a = get_number("a = ")
    b = get_number("b = ")

    if a == 0:
        print("❌ a cannot be 0")
        return

    x = -b / a

    print(f"\n✅ x = {x:.4f}")

    add_to_history(f"Linear: {a}x + {b} = 0 → x = {x:.4f}")


def solve_quadratic():
    print("\n--- Quadratic Equation ---")
    print("ax² + bx + c = 0")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")

    if a == 0:
        print("❌ Use linear solver")
        return

    d = b**2 - 4*a*c

    print(f"\nDiscriminant = {d:.4f}")

    if d > 0:
        print("Two real roots")

    elif d == 0:
        print("One repeated root")

    else:
        print("Complex roots")

    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)

    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)

        x1 = complex(real, imag)
        x2 = complex(real, -imag)

    print(f"x1 = {format_complex(x1)}")
    print(f"x2 = {format_complex(x2)}")

    add_to_history(
        f"Quadratic: {a}x² + {b}x + {c} = 0 → "
        f"x1={format_complex(x1)}, x2={format_complex(x2)}"
    )


def solve_cubic():
    print("\n--- Cubic Equation Solver ---")
    print("ax³ + bx² + cx + d = 0")

    a = get_number("a = ")
    b = get_number("b = ")
    c = get_number("c = ")
    d = get_number("d = ")

    coeffs = [a, b, c, d]

    roots = np.roots(coeffs)

    print("\n✅ Roots")

    formatted = []

    for i, root in enumerate(roots, 1):
        clean = format_complex(root)
        formatted.append(clean)

        print(f"x{i} = {clean}")

    add_to_history(f"Cubic {coeffs} → {formatted}")


def solve_polynomial():
    print("\n--- Polynomial Solver ---")
    print("Example:")
    print("2x² + 3x + 1 → 2 3 1")

    coeffs = input("\nCoefficients: ").split()

    try:
        coeffs = [float(x) for x in coeffs]

    except ValueError:
        print("❌ numbers only")
        return

    roots = np.roots(coeffs)

    print("\n✅ Roots")

    formatted = []

    for i, root in enumerate(roots, 1):
        clean = format_complex(root)

        formatted.append(clean)

        print(f"x{i} = {clean}")

    add_to_history(f"Polynomial {coeffs} → {formatted}")


def solve_system():
    print("\n--- 2x2 System Solver ---")

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
        print("❌ No unique solution")
        return

    solution = np.linalg.solve(A, B)

    x, y = solution

    print(f"\n✅ x = {x:.4f}")
    print(f"✅ y = {y:.4f}")

    add_to_history(f"System → x={x:.4f}, y={y:.4f}")


# ---------------- CALCULUS ---------------- #

def derivative_checker():
    print("\n--- Derivative Calculator ---")

    coeffs = input(
        "Enter polynomial coefficients: "
    ).split()

    try:
        coeffs = [float(c) for c in coeffs]

    except ValueError:
        print("❌ invalid input")
        return

    poly = np.poly1d(coeffs)
    deriv = np.polyder(poly)

    print(f"\n✅ Derivative:\n{deriv}")

    add_to_history(f"Derivative of {coeffs} → {deriv}")


def integral_calculator():
    print("\n--- Integral Calculator ---")

    coeffs = input(
        "Enter polynomial coefficients: "
    ).split()

    try:
        coeffs = [float(c) for c in coeffs]

    except ValueError:
        print("❌ invalid input")
        return

    poly = np.poly1d(coeffs)
    integ = np.polyint(poly)

    print(f"\n✅ Integral:\n{integ}")

    add_to_history(f"Integral of {coeffs} → {integ}")


def newton_method():
    print("\n--- Newton Method ---")

    expr = input("f(x) = ")

    x = sp.Symbol('x')

    try:
        f = sp.sympify(expr)

    except Exception:
        print("❌ invalid expression")
        return

    derivative = sp.diff(f, x)

    guess = get_number("Initial guess: ")

    for _ in range(10):
        fx = float(f.subs(x, guess))
        dfx = float(derivative.subs(x, guess))

        if dfx == 0:
            print("❌ derivative became zero")
            return

        guess = guess - fx / dfx

    print(f"\n✅ Root ≈ {guess}")

    add_to_history(f"Newton method on {expr} → {guess}")


# ---------------- MATRIX TOOLKIT ---------------- #

def matrix_toolkit():
    print("\n--- Matrix Toolkit ---")

    print("Enter a 2x2 matrix")

    matrix = []

    for i in range(2):
        row = list(map(float, input(f"Row {i+1}: ").split()))

        if len(row) != 2:
            print("❌ Must enter 2 numbers")
            return

        matrix.append(row)

    matrix = np.array(matrix)

    print("\nMatrix:")
    print(matrix)

    det = np.linalg.det(matrix)

    print(f"\n✅ Determinant = {det:.4f}")

    if det != 0:
        inv = np.linalg.inv(matrix)

        print("\n✅ Inverse:")
        print(inv)

    print("\n✅ Transpose:")
    print(matrix.T)

    eigen = np.linalg.eigvals(matrix)

    print("\n✅ Eigenvalues:")
    print(eigen)

    add_to_history(f"Matrix toolkit used on {matrix.tolist()}")


# ---------------- STATISTICS ---------------- #

def statistics_tool():
    print("\n--- Statistics Toolkit ---")

    try:
        nums = list(map(float, input("Numbers: ").split()))

    except ValueError:
        print("❌ invalid numbers")
        return

    print(f"\nMean = {np.mean(nums):.4f}")
    print(f"Median = {np.median(nums):.4f}")

    try:
        print(f"Mode = {mode(nums)}")

    except:
        print("Mode = none")

    print(f"Variance = {np.var(nums):.4f}")
    print(f"Std Dev = {np.std(nums):.4f}")

    add_to_history(f"Statistics on {nums}")


# ---------------- COMPLEX NUMBERS ---------------- #

def complex_toolkit():
    print("\n--- Complex Number Toolkit ---")

    real = get_number("Real part: ")
    imag = get_number("Imaginary part: ")

    z = complex(real, imag)

    print(f"\nComplex Number = {z}")
    print(f"Magnitude = {abs(z):.4f}")
    print(f"Conjugate = {z.conjugate()}")

    angle = math.degrees(math.atan2(z.imag, z.real))

    print(f"Phase Angle = {angle:.4f}°")

    add_to_history(f"Complex toolkit used on {z}")


# ---------------- GRAPHING ---------------- #

def graph_polynomial():
    print("\n--- Polynomial Grapher ---")

    coeffs = input(
        "Enter coefficients: "
    ).split()

    try:
        coeffs = [float(c) for c in coeffs]

    except ValueError:
        print("❌ invalid input")
        return

    poly = np.poly1d(coeffs)

    x = np.linspace(-20, 20, 1000)
    y = poly(x)

    plt.style.use("ggplot")

    plt.figure(figsize=(8, 5))

    plt.plot(x, y, linewidth=2)

    roots = np.roots(coeffs)

    for r in roots:
        if abs(r.imag) < 1e-6:
            plt.plot(r.real, 0, 'ro')

    plt.axhline(0)
    plt.axvline(0)

    plt.title("Polynomial Graph")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)

    save = input("Save graph? (y/n): ")

    if save.lower() == "y":
        plt.savefig("graph.png")
        print("✅ Saved as graph.png")

    plt.show()

    add_to_history(f"Graphed polynomial {coeffs}")


# ---------------- SCIENTIFIC CALCULATOR ---------------- #

def scientific_calculator():
    print("\n--- Scientific Calculator ---")

    print("Examples:")
    print("sin(pi/2)")
    print("sqrt(25)")
    print("2**8 + log(100,10)")

    expr = input("\nExpression: ")

    allowed = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "log": math.log,
        "pi": math.pi,
        "e": math.e
    }

    try:
        result = eval(expr, {"__builtins__": {}}, allowed)

        print(f"\n✅ Result = {result}")

        add_to_history(f"Calc: {expr} = {result}")

    except Exception:
        print("❌ invalid expression")


# ---------------- MENU ---------------- #

def show_menu():
    print("\n" + "=" * 50)
    print("🧮 EQUATION SOLVER v9")
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
    print("0  - Exit")

    print("=" * 50)


# ---------------- MAIN ---------------- #

def main():
    load_history()

    print("🧠 Advanced Math Utility Toolkit")

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
            derivative_checker()

        elif choice == "7":
            integral_calculator()

        elif choice == "8":
            newton_method()

        elif choice == "9":
            matrix_toolkit()

        elif choice == "10":
            statistics_tool()

        elif choice == "11":
            complex_toolkit()

        elif choice == "12":
            graph_polynomial()

        elif choice == "13":
            scientific_calculator()

        elif choice == "14":
            show_history()

        elif choice == "15":
            clear_history()

        elif choice == "16":
            export_history()

        elif choice == "0":
            print("\n👋 goodbye")
            break

        else:
            print("❌ invalid option")

        pause()


if __name__ == "__main__":
    main()
