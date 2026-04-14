# 🧠 Equation Solver CLI

A powerful Python command-line tool that solves **linear, quadratic, cubic, and polynomial equations**.

Built as a learning project to practice Python, math, and clean program structure — while making something actually useful.

---

## 🧠 What it does

* Solves **linear equations**
  `ax + b = 0`

* Solves **quadratic equations**
  `ax² + bx + c = 0`

* Solves **cubic equations**
  `ax³ + bx² + cx + d = 0`

* Solves **polynomials of any degree**
  (using NumPy)

---

## ⚙️ Features

* 🖥️ Simple and interactive CLI
* 🧠 Supports multiple equation types
* 📜 **Persistent history** (saved to file)
* 🧹 Clear history option
* 🔢 Handles **real and complex solutions**
* ✅ Input validation (no crashes on bad input)
* 📊 Clean and formatted output

---

## ▶️ How to run

1. Make sure Python 3 is installed
2. Install required dependency:

```bash
pip install numpy
```

3. Run the program:

```bash
python equation_solver.py
```

---

## 🧪 Example

```
Choose an option:
1 - Linear equation
2 - Quadratic equation
3 - Cubic equation
4 - Polynomial (any degree)
5 - Show history
6 - Clear history
7 - Exit

Your choice: 2

--- Quadratic Equation: ax² + bx + c = 0 ---

Enter a: 1
Enter b: -3
Enter c: 2

Discriminant = 1.00
✅ x1 = 2.00, x2 = 1.00
```

---

## 📌 Notes

* Complex numbers are supported when needed
* History is saved automatically in `history.txt`
* Designed for learning, clarity, and practical use

---

## 🚀 Future Improvements

* 📈 Graphing equations
* 🧩 Step-by-step solution explanations
* 🖥️ GUI version (Tkinter or web app)
* 📦 Package as a reusable Python module

---

## 👨‍💻 Author

Computer Science student exploring Python through small, practical projects.

Focused on building clean, simple, and useful tools 🚀
