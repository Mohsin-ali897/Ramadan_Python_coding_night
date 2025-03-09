# 🌙 CLI Task Manager

This is my **Ramadan Coding Night - Day 1** project. It is a simple yet efficient **CLI Task Manager** built using:

- 🚀 **uv** (Package Manager)
- ⚡ **Click** (For CLI interaction)

## 🛠️ Installation
Make sure you have **uv** installed. If not, install it first:
```bash
pip install uv
```

## 🚀 How to Run
Use the following commands to manage your tasks:

### ✅ Add a Task
To add a new task, run:
```bash
uv run python todo.py add 'Python practice'
```
This will store the task in `todo.json`.

### ❌ Remove a Task
To delete a task, provide its index number:
```bash
uv run python todo.py remove 2
```

### 📌 Mark Task as Completed
To mark a task as completed:
```bash
uv run python todo.py complete 2
```

### 📜 List All Tasks
To view all tasks:
```bash
uv run python todo.py list
```

---
✨ Happy Coding & Ramadan Mubarak! ✨

