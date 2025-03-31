
# 🧮 Week 2 – Arrays

This folder contains C programming projects that explore arrays, loops, and strings. These exercises deepen your understanding of data structures and text manipulation using C.

---

## 📂 Projects Included

### 1. 🔐 Caesar
- **File**: `caesar.c`
- **Description**: Encrypts text using Caesar’s cipher by shifting characters by a given key.
- **Concepts**: command-line arguments, string manipulation, ASCII math, `isalpha`, `isupper`, `islower`.

#### 💡 How to Run:
```bash
gcc -o caesar caesar.c -lm
./caesar 2
```

---

### 2. 📊 Readability
- **File**: `readability.c`
- **Description**: Determines the grade level of a block of text using the Coleman-Liau index.
- **Concepts**: string traversal, counting letters/words/sentences, formulas.

#### 💡 How to Run:
```bash
gcc -o readability readability.c -lm
./readability
```

---

### 3. 🔤 Scrabble
- **File**: `scrabble.c`
- **Description**: Compares two words and scores them using the rules of Scrabble.
- **Concepts**: scoring arrays, loops, character manipulation.

#### 💡 How to Run:
```bash
gcc -o scrabble scrabble.c -lm
./scrabble
```

---

## 🛠️ Tools Used
- C Language
- GCC Compiler
- Standard libraries: `stdio.h`, `cs50.h`, `string.h`, `ctype.h`, `math.h`

---

## 🎯 Learning Objectives
- Mastering `for` loops and arrays
- Character and string manipulation
- Handling command-line arguments
- Writing modular and readable C code

---

## 📎 Notes
To run programs that use `get_string()` or `get_int()` from the CS50 Library, make sure to have `cs50.h` installed and linked properly during compilation.

---

## 🧠 Author
Projects created as part of Harvard University's [CS50x](https://cs50.harvard.edu/x/) Introduction to Computer Science course.
