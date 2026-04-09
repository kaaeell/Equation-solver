import math

# 🧠 Equation Solver v1
# solve equations so you don’t have to (or because you have to)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("numbers only pls")


def solve_linear():
    print("\nSolving: ax + b = 0")

    a = get_number("Enter a: ")
    b = get_number("Enter b: ")

    if a == 0:
        print("no solution (a can't be 0)")
        return

    x = -b / a
    print(f"Solution: x = {x:.2f}")


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
        print(f"Two solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")

    elif discriminant == 0:
        x = -b / (2*a)
        print(f"One solution: x = {x:.2f}")

    else:
        print("no real solutions")


def main():
    print("🧠 Equation Solver")
    print("solve math quickly\n")

    while True:
        print("\nChoose what to do:")
        print("1 - Solve a linear equation")
        print("2 - Solve a quadratic equation")
        print("3 - Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            solve_linear()
        elif choice == "2":
            solve_quadratic()
        elif choice == "3":
            print("done. go touch some grass 🌱")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()