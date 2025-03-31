
# ⚙️ Week 3 – Algorithms

This folder includes projects that dive into basic algorithms and voting systems. You'll explore searching, sorting, and implementing logic-based algorithms in C.

---

## 📂 Projects Included

### 1. 🗳️ Plurality
- **File**: `plurality.c`
- **Description**: Simulates a simple plurality vote election where the candidate with the most votes wins.
- **Concepts**: structs, arrays, string comparison, input parsing.

#### 💡 How to Run:
```bash
gcc -o plurality plurality.c -lm
./plurality Alice Bob Charlie
```

---

### 2. 🧠 Tideman
- **File**: `tideman.c`
- **Description**: Implements the Tideman voting algorithm (ranked pairs), a more complex and fair election system.
- **Concepts**: graph cycles, sorting pairs, ranking preferences, recursion.

#### 💡 How to Run:
```bash
gcc -o tideman tideman.c -lm
./tideman Alice Bob Charlie
```

---

## 🛠️ Tools Used
- C Language
- GCC Compiler
- Standard libraries: `cs50.h`, `stdio.h`, `string.h`, `stdbool.h`

---

## 🎯 Learning Objectives
- Understanding data structures like structs
- Building sorting and ranking logic
- Applying graph theory (Tideman)
- Command-line arguments and input validation

---

## 📎 Notes
Some logic, especially in Tideman, requires careful debugging to avoid introducing cycles in the graph. Make use of print statements to trace your algorithm.

---

## 🧠 Author
Projects developed as part of [CS50x](https://cs50.harvard.edu/x/) – Harvard's Introduction to Computer Science.
