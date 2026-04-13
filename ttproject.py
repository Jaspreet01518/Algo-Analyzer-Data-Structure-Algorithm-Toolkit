import tkinter as tk
from tkinter import messagebox
from collections import deque, OrderedDict

# ---------------- CO1 ----------------
def precedence(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    return 0

def infix_to_postfix(expression):
    stack = []
    output = ""
    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output += stack.pop()
            stack.append(char)
    while stack:
        output += stack.pop()
    return output

# ---------------- CO2 ----------------
def find_duplicates(arr):
    seen = set()
    dup = set()
    for num in arr:
        if num in seen:
            dup.add(num)
        else:
            seen.add(num)
    return list(dup)

# ---------------- CO3 ----------------
class User:
    def role(self):
        return "User"

class Admin(User):
    def role(self):
        return "Admin (Full Access)"

# ---------------- CO4 ----------------
class LRUCache:
    def __init__(self, cap):
        self.cache = OrderedDict()
        self.cap = cap

    def access(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return "Hit"
        else:
            if len(self.cache) >= self.cap:
                self.cache.popitem(last=False)
            self.cache[key] = True
            return "Miss"

# ---------------- CO5 ----------------
graph = {1:[2,3], 2:[4], 3:[], 4:[]}

def bfs(start):
    visited = set()
    q = deque([start])
    res = []
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            res.append(node)
            q.extend(graph[node])
    return res

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    res = [start]
    for n in graph[start]:
        if n not in visited:
            res.extend(dfs(n, visited))
    return res

# ---------------- FUNCTIONS ----------------
def convert():
    try:
        result = infix_to_postfix(entry.get())
        messagebox.showinfo("Result", result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def duplicates():
    try:
        arr = list(map(int, entry.get().split()))
        messagebox.showinfo("Duplicates", find_duplicates(arr))
    except:
        messagebox.showerror("Error", "Enter numbers only")

def lru():
    try:
        items = list(map(int, entry.get().split()))
        cache = LRUCache(3)
        out = ""
        for i in items:
            out += f"{i}: {cache.access(i)}\n"
        messagebox.showinfo("LRU", out)
    except:
        messagebox.showerror("Error", "Enter numbers only")

def do_bfs():
    messagebox.showinfo("BFS", bfs(1))

def do_dfs():
    messagebox.showinfo("DFS", dfs(1))

def role():
    messagebox.showinfo("Role", Admin().role())

# ---------------- COLORFUL UI ----------------
root = tk.Tk()
root.title("AlgoAnalyzer 🎯")
root.geometry("400x500")
root.configure(bg="#1e1e2f")  # dark background

title = tk.Label(root, text="AlgoAnalyzer", font=("Arial", 20, "bold"),
                 bg="#1e1e2f", fg="#00ffcc")
title.pack(pady=10)

tk.Label(root, text="Enter Input:", bg="#1e1e2f",
         fg="white", font=("Arial", 12)).pack()

entry = tk.Entry(root, width=30, font=("Arial", 12),
                 bg="#2e2e3e", fg="white", insertbackground="white")
entry.pack(pady=10)

# Button style
btn_style = {
    "width": 25,
    "font": ("Arial", 10, "bold"),
    "bd": 0,
    "padx": 5,
    "pady": 5
}

tk.Button(root, text="Infix → Postfix", bg="#ff6b6b", fg="white",
          command=convert, **btn_style).pack(pady=5)

tk.Button(root, text="Find Duplicates", bg="#4ecdc4", fg="black",
          command=duplicates, **btn_style).pack(pady=5)

tk.Button(root, text="LRU Cache", bg="#ffd93d", fg="black",
          command=lru, **btn_style).pack(pady=5)

tk.Button(root, text="BFS Traversal", bg="#6c5ce7", fg="white",
          command=do_bfs, **btn_style).pack(pady=5)

tk.Button(root, text="DFS Traversal", bg="#00b894", fg="white",
          command=do_dfs, **btn_style).pack(pady=5)

tk.Button(root, text="User Role (OOP)", bg="#fd79a8", fg="white",
          command=role, **btn_style).pack(pady=5)

root.mainloop()