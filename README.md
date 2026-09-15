# CFG String Derivation Simulator

A simple Python-based **Context-Free Grammar (CFG) String Derivation Simulator** that allows users to enter grammar productions and a target string, then automatically checks whether the string can be derived from the given grammar.

The program searches for both **leftmost** and **rightmost derivations** and also displays a **derivation tree** for the resulting derivation.

This project was created as a practical implementation of concepts from **Formal Languages and Automata Theory / Theory of Computation**.

---

## ✨ Features

* Define your own CFG productions
* Support multiple productions using `|`
* Automatically identify uppercase letters as **non-terminals**
* Treat lowercase letters, numbers, and special characters as **terminals**
* Enter any target string to test
* Find a **leftmost derivation**
* Find a **rightmost derivation**
* Show which production was used at every step
* Display the final derivation sequence
* Generate a text-based **derivation tree**
* Inform the user when a string cannot be derived
* Uses BFS-based searching to explore possible derivations
* Simple command-line interface
* No external Python libraries required

---

## 📚 What is a Context-Free Grammar?

A **Context-Free Grammar (CFG)** is a formal system used to describe languages.

A CFG consists of:

* **Non-terminals**
* **Terminals**
* **Productions**
* **Start symbol**

For example:

```text
S → 0S1 | 01
```

Here:

```text
S
```

is the non-terminal.

And:

```text
0
1
```

are terminals.

---

## 🔤 Symbol Rules Used in This Project

This project uses a simple convention:

### Non-terminals

Any uppercase English letter:

```text
A B C D ... Z
```

### Terminals

Anything that is not an uppercase letter is treated as a terminal.

Examples:

```text
a b c
0 1 2
@ # $
+ - *
( )
```

For example:

```text
S → aB
```

means:

```text
S = Non-terminal
a = Terminal
B = Non-terminal
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

## 2. Open the project

```bash
cd YOUR-REPOSITORY
```

## 3. Run the program

```bash
python main.py
```

No additional packages are required.

---

# 📝 How to Enter Productions

Enter productions in this format:

```text
S -> aB | bA
A -> a | aS | bAA
B -> b | bS | aBB
```

You can enter as many productions as required.

When all productions have been entered, type:

```text
DONE
```

---

# 🧪 Example 1 — Simple Recursive Grammar

Consider:

```text
S → 0S1 | 01
```

Target:

```text
000111
```

The program finds the derivation:

```text
S
↓
0S1
↓
00S11
↓
000111
```

The individual production steps are:

```text
S
   -> 0S1    (S -> 0S1)
   -> 00S11  (S -> 0S1)
   -> 000111 (S -> 01)
```

Therefore:

```text
000111
```

**can be derived from the grammar.**

---

# 🌳 Derivation Tree

For the above example, the program generates a tree similar to:

```text
S
├── 0
├── S
│   ├── 0
│   ├── S
│   │   ├── 0
│   │   └── 1
│   └── 1
└── 1
```

This represents the complete derivation of:

```text
000111
```

---

# 🧪 Example 2 — Multiple Productions

Input:

```text
S -> aB | bA
A -> a | aS | bAA
B -> b | bS | aBB
DONE
```

Target:

```text
bbaaba
```

The program searches the available production possibilities and can produce a leftmost derivation such as:

```text
S
   -> bA
   -> bbAA
   -> bbaSA
   -> bbaaBA
   -> bbaabA
   -> bbaaba
```

A rightmost derivation can also be found:

```text
S
   -> bA
   -> bbAA
   -> bbAa
   -> bbaSa
   -> bbaaBa
   -> bbaaba
```

---

# 🔄 Leftmost Derivation

In a **leftmost derivation**, the leftmost non-terminal is replaced first.

For example:

```text
S → bA
```

Then:

```text
bA → bbAA
```

because the leftmost `A` is replaced.

The process continues until no non-terminals remain.

---

# 🔄 Rightmost Derivation

In a **rightmost derivation**, the rightmost non-terminal is replaced first.

For example:

```text
bbAA → bbAa
```

The rightmost `A` is replaced first.

The process continues until the target string is produced.

---

# 🔍 How the Program Works

The program follows these main steps:

```text
User
 │
 ▼
Enter CFG Productions
 │
 ▼
Store Grammar
 │
 ▼
Enter Start Symbol
 │
 ▼
Enter Target String
 │
 ▼
Search Possible Derivations
 │
 ├───────────────┐
 ▼               ▼
Leftmost       Rightmost
Derivation     Derivation
 │               │
 └───────┬───────┘
         ▼
   String Found?
      /      \
    Yes       No
     │         │
     ▼         ▼
 Derivation   Cannot
   Tree        Derive
```

---

# ⚙️ Search Algorithm

The program uses **Breadth-First Search (BFS)** to explore possible derivation states.

For example:

```text
S
├── 0S1
└── 01
```

From:

```text
0S1
```

the program explores:

```text
00S11
```

and continues until it either reaches the target string or exhausts the possible states within the configured search limit.

Using BFS helps the program find a derivation without simply selecting the first production and potentially getting stuck in an unnecessary recursive path.

---

# 🧠 Why BFS?

A CFG may contain several possible productions.

For example:

```text
S → aS | bA | c
```

The program should not assume that the first production is always correct.

Instead, it explores possible states:

```text
S
├── aS
├── bA
└── c
```

and continues searching for a path that reaches the requested target.

---

# 📂 Project Structure

A simple version of the project can use:

```text
CFG-String-Derivation/
│
├── main.py
│
└── README.md
```

### `main.py`

Contains:

* Grammar input
* Production parsing
* CFG validation
* Leftmost derivation search
* Rightmost derivation search
* Derivation display
* Derivation tree generation
* Main program interface

---

# 💻 Example Program Session

```text
======================================================================
       CONTEXT FREE GRAMMAR DERIVATION TOOL
======================================================================

Rules:
• Uppercase letters = Non-terminals
• Everything else = Terminal
• Numbers are terminals
• Special characters are terminals

Enter productions one by one.

Production: S -> 0S1 | 01
Production: done

Your Grammar:
----------------------------------------
S -> 0S1 | 01

Enter start symbol [default S]: S
Enter string to derive: 000111

Searching for derivations...

======================================================================
RESULT
======================================================================

The string "000111" CAN be derived from the given productions.
```

---

# 🛠️ Technologies Used

| Technology             | Purpose                        |
| ---------------------- | ------------------------------ |
| Python                 | Main programming language      |
| `collections.deque`    | BFS queue                      |
| Classes                | Derivation tree representation |
| Command Line Interface | User interaction               |

No external dependencies are required.

---

# 🎯 Learning Objectives

This project helps demonstrate practical implementation of:

* Context-Free Grammars
* Formal Languages
* Production rules
* Terminals and non-terminals
* Sentential forms
* Leftmost derivation
* Rightmost derivation
* Derivation trees
* Grammar-based string generation
* Breadth-First Search
* State-space exploration
* Recursive grammar handling

---

# ⚠️ Limitations

This project is intentionally designed to be simple and educational.

Some complex CFGs can have a very large number of possible derivation states.

Recursive grammars can also generate infinitely many possibilities.

Therefore, the program uses a search-length limitation to prevent infinite computation.

The current implementation is primarily intended for **learning and experimentation**, rather than being a complete industrial CFG parser.

---

# 🔮 Future Improvements

Possible future versions could include:

* [ ] Graphical user interface
* [ ] Interactive derivation tree
* [ ] Graphical CFG visualization
* [ ] Step-by-step derivation controls
* [ ] Multiple derivation trees
* [ ] Export derivation to PDF
* [ ] Save/load grammar files
* [ ] Support for epsilon (`ε`) productions
* [ ] Better grammar validation
* [ ] CYK parsing algorithm
* [ ] Parse-tree generation
* [ ] Ambiguous grammar detection
* [ ] Derivation depth controls
* [ ] Production-rule highlighting
* [ ] Web-based version

---

# 🎓 Academic Use

This project can be used as a practical demonstration for subjects such as:

**Theory of Computation**

**Formal Languages and Automata Theory**

**Compiler Design**

**Discrete Mathematics**

It demonstrates how theoretical grammar concepts can be implemented using a programming language.

---

# 🤝 Contributing

Contributions and improvements are welcome.

You can:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Create a Pull Request

---

# 📄 License

This project is available for educational and learning purposes.

---

## ⭐ If You Find This Useful

If this project helped you understand CFG derivations or you found it useful for your Theory of Computation practice, consider giving the repository a ⭐.

---

### Author

**Dipak Sonawane**

Python • AI/ML • Software Development • Computer Science
