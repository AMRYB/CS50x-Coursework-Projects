
# 📘 Week 1 – C Basics

This folder contains beginner-level projects written in C as part of Week 1 of the CS50x course. These exercises help build a foundation in C programming, covering syntax, conditionals, loops, and basic algorithms.

---

## 📂 Projects Included

### 1. 💰 Cash
- **File**: `cash.c`
- **Description**: Implements a greedy algorithm to determine the minimum number of coins needed to make a given amount of change.
- **Concepts**: `float`, `round`, `int`, loops, conditionals.

#### 💡 How to Run:
```bash
gcc -o cash cash.c -lm
./cash
```

---

### 2. 👋 Hello, It's Me
- **File**: `hello.c`
- **Description**: A simple program that prints `hello, world`. It's the classic first program used to introduce syntax and compiling.
- **Concepts**: `#include`, `main()`, `printf`.

#### 💡 How to Run:
```bash
gcc -o hello hello.c
./hello
```

---

### 3. 🧱 Mario (Less)
- **File**: `mario.c`
- **Description**: Prints a left-aligned pyramid of hashes `#` based on user input height (from 1 to 8).
- **Concepts**: `for` loops, `printf`, nested iteration, user input.

#### 💡 How to Run:
```bash
gcc -o mario mario.c
./mario
```

---

## 🛠️ Tools Used
- C Language (compiled with `gcc`)
- CS50 Library (`cs50.h`) where required
- Command-line for input/output

---

## 🎯 Learning Objectives
- Understanding data types (`int`, `float`, `char`)
- Using `printf()` and user input
- Basic control flow: `if`, `else`, `while`, `for`
- Working with functions and compilation using `gcc`

---

## 📎 Notes
Make sure you have the CS50 library installed if you're compiling code that uses `get_int()` or similar functions. You can install it from [cs50.io](https://cs50.readthedocs.io/).

---

## 🧠 Author
Projects written as part of Harvard's [CS50x](https://cs50.harvard.edu/x/) Introduction to Computer Science course.
