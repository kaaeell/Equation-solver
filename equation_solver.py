# ===================== EXTRA FEATURES PACK =====================

import string
import time

# ===================== PASSWORD GENERATOR =====================

def password_generator():
    print(Fore.CYAN + "\n--- Password Generator ---")

    length = int(get_number("Password length: "))

    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choice(chars) for _ in range(length))

    print(Fore.GREEN + f"\n✅ Generated Password:\n{password}")

    add_to_history(f"Generated password of length {length}")

# ===================== RANDOM NUMBER GENERATOR =====================

def random_number_generator():
    print(Fore.CYAN + "\n--- Random Number Generator ---")

    start = int(get_number("Start: "))
    end = int(get_number("End: "))

    number = random.randint(start, end)

    print(Fore.GREEN + f"\n🎲 Random Number = {number}")

    add_to_history(f"Random number between {start}-{end} → {number}")

# ===================== STOPWATCH =====================

def stopwatch():
    print(Fore.CYAN + "\n--- Stopwatch ---")

    input("Press ENTER to start...")

    start = time.time()

    input("Press ENTER to stop...")

    end = time.time()

    elapsed = end - start

    print(Fore.GREEN + f"\n⏱ Time: {elapsed:.2f} seconds")

    add_to_history(f"Stopwatch used → {elapsed:.2f}s")

# ===================== BMI CALCULATOR =====================

def bmi_calculator():
    print(Fore.CYAN + "\n--- BMI Calculator ---")

    weight = get_number("Weight (kg): ")
    height = get_number("Height (meters): ")

    bmi = weight / (height ** 2)

    print(Fore.GREEN + f"\n✅ BMI = {bmi:.2f}")

    if bmi < 18.5:
        print(Fore.YELLOW + "Underweight")

    elif bmi < 25:
        print(Fore.GREEN + "Normal weight")

    elif bmi < 30:
        print(Fore.YELLOW + "Overweight")

    else:
        print(Fore.RED + "Obese")

    add_to_history(f"BMI calculated → {bmi:.2f}")

# ===================== AGE CALCULATOR =====================

def age_calculator():
    print(Fore.CYAN + "\n--- Age Calculator ---")

    birth_year = int(get_number("Birth year: "))

    current_year = datetime.now().year

    age = current_year - birth_year

    print(Fore.GREEN + f"\n🎂 You are {age} years old")

    add_to_history(f"Age calculated → {age}")

# ===================== COUNTDOWN TIMER =====================

def countdown_timer():
    print(Fore.CYAN + "\n--- Countdown Timer ---")

    seconds = int(get_number("Seconds: "))

    while seconds > 0:
        print(f"\r⏳ {seconds} seconds remaining...", end="")
        time.sleep(1)
        seconds -= 1

    print(Fore.GREEN + "\n\n⏰ TIME'S UP!")

    add_to_history("Countdown timer completed")

# ===================== DICE ROLLER =====================

def dice_roller():
    print(Fore.CYAN + "\n--- Dice Roller ---")

    dice = random.randint(1, 6)

    print(Fore.GREEN + f"\n🎲 You rolled: {dice}")

    add_to_history(f"Dice rolled → {dice}")

# ===================== COIN FLIP =====================

def coin_flip():
    print(Fore.CYAN + "\n--- Coin Flip ---")

    result = random.choice(["Heads", "Tails"])

    print(Fore.GREEN + f"\n🪙 {result}")

    add_to_history(f"Coin flip → {result}")

# ===================== ADD THESE TO MENU =====================

print("19 - Password Generator")
print("20 - Random Number Generator")
print("21 - Stopwatch")
print("22 - BMI Calculator")
print("23 - Age Calculator")
print("24 - Countdown Timer")
print("25 - Dice Roller")
print("26 - Coin Flip")

# ===================== ADD THESE TO main() =====================

elif choice == "19":
    password_generator()

elif choice == "20":
    random_number_generator()

elif choice == "21":
    stopwatch()

elif choice == "22":
    bmi_calculator()

elif choice == "23":
    age_calculator()

elif choice == "24":
    countdown_timer()

elif choice == "25":
    dice_roller()

elif choice == "26":
    coin_flip()
