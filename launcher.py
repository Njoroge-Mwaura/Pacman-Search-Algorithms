import subprocess
import sys
import os
import tkinter as tk
from tkinter import ttk

# Available options
LAYOUTS = [
    "Tiny Maze",
    "Medium Maze",
    "visual Showcase",
    "visual Showcase Large",
    "Halloween Showcase",
]
AGENTS = [
    "Search Agent",
]
SEARCH_FUNCS = [
    "Breadth First Search",
    "Depth First Search",
    "Uniform Cost Search",
    "A Star Search",
]

# Defaults
DEFAULT_LAYOUT = " "
DEFAULT_AGENT = " "
DEFAULT_SEARCH = " "

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PYTHON_BIN = sys.executable or "python3"


def run_game(layout, agent, fn):
    args = [
        PYTHON_BIN,
        os.path.join(PROJECT_ROOT, "pacman.py"),
        "-l",
        layout,
        "-p",
        agent,
        "-a",
        f"fn={fn},prob=PositionSearchProblem",
        "-z",
        "0.9",
        "--frameTime",
        "0.08",
    ]
    try:
        subprocess.Popen(args, cwd=PROJECT_ROOT)
    except Exception as e:
        print("Failed to launch:", e)


class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pacman Arcade Launcher")
        self.configure(bg="#0b122b")
        self.resizable(False, False)
        self.geometry("720x600")

        container = tk.Frame(self, bg="#0b122b")
        container.pack(padx=30, pady=30)

        title = tk.Label(
            container,
            text="PAC-MAN",
            font=("Helvetica", 28, "bold"),
            fg="#f9b233",
            bg="#0b122b",
        )
        title.pack(pady=(0, 10))

        # Layout dropdown
        lab1 = tk.Label(
            container,
            text="Select Layout:",
            fg="#20e3ff",
            bg="#0b122b",
            font=("Helvetica", 12, "bold"),
        )
        lab1.pack(anchor="w")
        self.layout_var = tk.StringVar(value=DEFAULT_LAYOUT)
        dd1 = ttk.Combobox(
            container, textvariable=self.layout_var, values=LAYOUTS, state="readonly"
        )
        dd1.pack(fill="x", pady=(0, 10))

        # Agent dropdown (fixed to SearchAgent)
        lab2 = tk.Label(
            container,
            text="Select Agent:",
            fg="#ff33cc",
            bg="#0b122b",
            font=("Helvetica", 12, "bold"),
        )
        lab2.pack(anchor="w")
        self.agent_var = tk.StringVar(value=DEFAULT_AGENT)
        dd2 = ttk.Combobox(
            container, textvariable=self.agent_var, values=AGENTS, state="readonly"
        )
        dd2.pack(fill="x", pady=(0, 10))

        # Search function dropdown
        lab3 = tk.Label(
            container,
            text="Select Search Function:",
            fg="#4cff4c",
            bg="#0b122b",
            font=("Helvetica", 12, "bold"),
        )
        lab3.pack(anchor="w")
        self.fn_var = tk.StringVar(value=DEFAULT_SEARCH)
        dd3 = ttk.Combobox(
            container, textvariable=self.fn_var, values=SEARCH_FUNCS, state="readonly"
        )
        dd3.pack(fill="x", pady=(0, 18))

        # Start button
        start_btn = tk.Button(
            container,
            text="START GAME",
            font=("Helvetica", 16, "bold"),
            bg="#ffd200",
            activebackground="#ffdd55",
            command=self.on_start,
        )
        start_btn.pack(fill="x")

    def on_start(self):
        layout = self.layout_var.get()
        agent = self.agent_var.get()
        fn = self.fn_var.get()
        run_game(layout, agent, fn)


if __name__ == "__main__":
    app = Launcher()
    app.mainloop()
