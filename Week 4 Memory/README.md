
# 💾 Week 4 – Memory

In Week 4 of CS50x, the focus is on memory management in C, including pointers, memory allocation, and manipulating binary data. These projects explore how to work directly with memory and files.

---

## 📂 Projects Included

### 1. 🧃 Volume
- **File**: `volume.c`
- **Description**: Changes the volume of an audio file by scaling the amplitude of its samples.
- **Concepts**: Pointers, structs, reading/writing binary data.

#### 💡 How to Run:
```bash
gcc -o volume volume.c -lm
./volume input.wav output.wav 2.0
```

---

### 2. 📸 Filter
- **File**: `helpers.c`
- **Description**: Applies various image filters like grayscale, sepia, reflection, and blur to BMP images.
- **Concepts**: 2D arrays, RGB color manipulation, matrix operations.

#### 💡 How to Run:
```bash
make filter
./filter -g input.bmp output.bmp
```

---

### 3. 🧼 Recover
- **File**: `recover.c`
- **Description**: Recovers JPEG files from a forensic image by detecting JPEG signatures in memory.
- **Concepts**: Pointers, file I/O, byte operations.

#### 💡 How to Run:
```bash
gcc -o recover recover.c
./recover card.raw
```

---

## 🛠️ Tools Used
- C Language
- GCC Compiler
- Standard libraries: `stdio.h`, `stdlib.h`, `stdint.h`, `math.h`

---

## 🎯 Learning Objectives
- Understand pointers and pointer arithmetic
- Work with binary files (audio/images)
- Apply filters and manipulate pixels
- File handling and data recovery techniques

---

## 📎 Notes
Working with raw memory and file data can be error-prone. Use tools like `valgrind` to check for memory leaks and invalid access.

---

## 🧠 Author
Projects developed as part of Harvard’s [CS50x](https://cs50.harvard.edu/x/) Introduction to Computer Science course.
