# 🧠 Speller

## 📁 Files
- `speller.c`: Main driver program that handles user input and interfaces with the dictionary.
- `dictionary.c`: Implements core functions for loading, checking, and unloading the dictionary.

## 📝 Description
Speller is a program that checks the spelling of words in a text file using a dictionary. It loads the dictionary into a hash table and then compares each word in the input file to the loaded words.

## 🚀 How to Run
```bash
make speller
./speller text.txt
```

## 🧠 Concepts
- Hash table implementation
- File reading and parsing
- Use of pointers and dynamic memory
- Handling large datasets efficiently
- Counting misspelled words, total words, and dictionary loading time

## 🔍 Functions Implemented
In `dictionary.c`:
- `bool check(const char *word)`
- `bool load(const char *dictionary)`
- `unsigned int size(void)`
- `bool unload(void)`

These are called from `speller.c` to perform the spelling check and print summary statistics.

---

Project created as part of [CS50x](https://cs50.harvard.edu/x/) by Harvard University.