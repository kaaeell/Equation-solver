import math
import numpy as np

# 🧠 Equation Solver v4
# solves equations so you survive math exams

history = []


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter a valid number :)")


def add_to_history(entry):
    history.append(entry)


def show_history():
    if not history:
        print("\nno history yet... go do some math first")
        return

    print("\n📜 History:")
    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")


def format_complex(num):
    """Format complex numbers nicely"""
    if abs(num.imag) < 1e-6:
        return f"{num.real:.2f}"
    return f"{num.real:.2f} + {num.imag:.2f}j"


def solve_linear():
    print("\n--- Linear Equation: ax + b = 0 ---")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")

    if a == 0:
        print("no solution (a cannot be 0)")
        return

    x = -b / a
    print(f"Solution: x = {x:.2f}")

    add_to_history(f"Linear → x = {x:.2f}")


def solve_quadratic():
    print("\n--- Quadratic Equation: ax² + bx + c = 0 ---")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")

    if a == 0:
        print("this becomes linear... try again")
        return

    d = b**2 - 4*a*c
    print(f"Discriminant = {d:.2f}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Two solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
        add_to_history(f"Quadratic → x1={x1:.2f}, x2={x2:.2f}")

    elif d == 0:
        x = -b / (2*a)
        print(f"One solution: x = {x:.2f}")
        add_to_history(f"Quadratic → x={x:.2f}")

    else:
        # handle complex roots
        real_part = -b / (2*a)
        imag_part = math.sqrt(-d) / (2*a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)

        print(f"Complex solutions:")
        print(f"x1 = {format_complex(x1)}")
        print(f"x2 = {format_complex(x2)}")

        add_to_history(f"Quadratic → x1={format_complex(x1)}, x2={format_complex(x2)}")


def solve_cubic():
    print("\n--- Cubic Equation: ax³ + bx² + cx + d = 0 ---")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")
    d = get_number("Enter d: ")

    if a == 0:
        print("this is NOT a cubic equation 😭")
        return

    roots = np.roots([a, b, c, d])

    print("Solutions:")
    formatted_roots = []

    for i, r in enumerate(roots, 1):
        clean = format_complex(r)
        formatted_roots.append(clean)
        print(f"x{i} = {clean}")

    add_to_history(f"Cubic → roots = {formatted_roots}")


def show_menu():
    print("\nChoose an option:")
    print("1 - Linear equation")
    print("2 - Quadratic equation")
    print("3 - Cubic equation")
    print("4 - Show history")
    print("5 - Exit")


def main():
    print("🧠 Equation Solver v4")
    print("because math won’t solve itself\n")

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
            show_history()
        elif choice == "5":
            print("done. go touch some grass 🌱")
            break
        else:
            print("invalid choice, try again")


if __name__ == "__main__":
    main()
