import math
import numpy as np

# 🧠 Equation Solver v2
# now with history + cubic equations (yeah we leveling up)

history = []


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("numbers only pls")


def add_to_history(entry):
    history.append(entry)


def show_history():
    if not history:
        print("\nno history yet... go solve something first")
        return

    print("\n📜 History:")
    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")


def solve_linear():
    print("\nSolving: ax + b = 0")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")

    if a == 0:
        print("no solution (a can't be 0)")
        return

    x = -b / a
    result = f"ax + b = 0 → x = {x:.2f}"
    print(f"Solution: x = {x:.2f}")
    add_to_history(result)


def solve_quadratic():
    print("\nSolving: ax² + bx + c = 0")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")

    if a == 0:
        print("this becomes linear... but nah try again")
        return

    discriminant = b**2 - 4*a*c
    print(f"Discriminant = {discriminant}")

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"ax²+bx+c=0 → x1={x1:.2f}, x2={x2:.2f}"
        print(f"Two solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")

    elif discriminant == 0:
        x = -b / (2*a)
        result = f"ax²+bx+c=0 → x={x:.2f}"
        print(f"One solution: x = {x:.2f}")

    else:
        result = "ax²+bx+c=0 → no real solutions"
        print("no real solutions")

    add_to_history(result)


def solve_cubic():
    print("\nSolving: ax³ + bx² + cx + d = 0")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")
    d = get_number("Enter d: ")

    if a == 0:
        print("this is not cubic bro 😭")
        return

    # numpy handles roots (real + complex)
    roots = np.roots([a, b, c, d])

    print("Solutions:")
    for i, r in enumerate(roots, 1):
        print(f"x{i} = {r:.2f}")

    result = f"ax³+bx²+cx+d=0 → roots = {[round(r,2) for r in roots]}"
    add_to_history(result)


def main():
    print("🧠 Equation Solver v2")
    print("still solving your math problems\n")

    while True:
        print("\nChoose what to do:")
        print("1 - Solve a linear equation")
        print("2 - Solve a quadratic equation")
        print("3 - Solve a cubic equation")
        print("4 - Show history")
        print("5 - Exit")

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
            print("invalid choice")


if __name__ == "__main__":
    main()
