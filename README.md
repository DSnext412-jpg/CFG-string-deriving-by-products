# ⚡ CFG Derivation Simulator

> A lightweight Python tool for exploring **Context-Free Grammar (CFG)** derivations.

Enter your grammar + target string and get **Leftmost Derivation**, **Rightmost Derivation**, and a **Derivation Tree** automatically.

---

## ✨ Features

| 🧩 Grammar                | 🔍 Derivation | 🌳 Visualization    |
| ------------------------- | ------------- | ------------------- |
| Custom productions        | Leftmost      | Derivation tree     |
| Multiple rules            | Rightmost     | Step-by-step output |
| Terminals & non-terminals | BFS search    | CLI visualization   |

---

## 🚀 How It Works

```text
      📥 Grammar
          │
          ▼
    🎯 Target String
          │
          ▼
    🔎 BFS Search
       ↙       ↘
 Leftmost    Rightmost
    │            │
    └─────┬──────┘
          ▼
      🌳 Tree
```

---

## 🧪 Example

### Grammar

```text
S → 0S1 | 01
```

### Target

```text
000111
```

### Derivation

```text
S
↓ S → 0S1
0S1
↓ S → 0S1
00S11
↓ S → 01
000111
```

### Tree

```text
          S
       /  |  \
      0   S   1
         /|\
        0 S 1
          / \
         0   1
```

---

## 🛠️ Tech Stack

```text
🐍 Python
🔎 Breadth-First Search
🌳 Tree Traversal
💻 Command Line Interface
```

**No external dependencies required.**

---

## ▶️ Run

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
python main.py
```

Then enter:

```text
Production: S -> 0S1 | 01
Production: DONE

Start symbol: S
Target string: 000111
```

---

## 🎓 Built For

**Theory of Computation • Formal Languages • CFG Practice**

---

### ⭐ Like the project?

Give it a star if it helped you understand CFG derivations.

**Made with 🐍 Python by Dipak Sonawane**
