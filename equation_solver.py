import math
import numpy as np

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


# ---------------- LINEAR SOLVER ---------------- #

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


# ---------------- QUADRATIC SOLVER ---------------- #

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


# ---------------- CUBIC SOLVER ---------------- #

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

    for i, root in enumerate(roots, 1):
        clean = format_complex(root)
        print(f"x{i} = {clean}")


# ---------------- POLYNOMIAL SOLVER ---------------- #

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

    for i, root in enumerate(roots, 1):
        clean = format_complex(root)
        print(f"x{i} = {clean}")


# ---------------- SYSTEM SOLVER ---------------- #

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


# ---------------- MENU ---------------- #

def show_menu():
    print("\n" + "=" * 50)
    print("🧮 EQUATION SOLVER")
    print("=" * 50)

    print("1 - Linear Solver")
    print("2 - Quadratic Solver")
    print("3 - Cubic Solver")
    print("4 - Polynomial Solver")
    print("5 - System Solver")
    print("0 - Exit")

    print("=" * 50)


# ---------------- MAIN ---------------- #

def main():
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

        elif choice == "0":
            print("\n👋 goodbye")
            break

        else:
            print("❌ invalid option")


if __name__ == "__main__":
    main()
