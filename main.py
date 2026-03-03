# imports
from viewController import updateFoundBox, solve
from tkinter import scrolledtext
import tkinter as tk

window = None
foundBoxes = []
excludeBox = None
excludeAtBoxes = []
output = None

THEME = {
    "bg": "#0f172a",
    "card": "#111827",
    "card2": "#0b1220",
    "text": "#e5e7eb",
    "muted": "#9ca3af",
    "border": "#1f2937",

    "green": "#22c55e",
    "yellow": "#f59e0b",
    "gray": "#6b7280",

    "btn": "#3b82f6",
    "btn_hover": "#2563eb",
    "danger": "#ef4444",
}

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_H2    = ("Segoe UI", 11, "bold")
FONT_BODY  = ("Segoe UI", 10)
FONT_TILE  = ("Segoe UI", 18, "bold")
FONT_MONO  = ("Consolas", 11)





def main():
    global window, excludeBox, excludeAtBoxes, output

    window = tk.Tk()
    window.title("Wordle Solver")
    window.configure(bg=THEME["bg"])
    window.minsize(720, 560)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # outer container
    outer = tk.Frame(window, bg=THEME["bg"])
    outer.grid(row=0, column=0, sticky="nsew")
    outer.grid_rowconfigure(0, weight=1)
    outer.grid_columnconfigure(0, weight=1)

    card = tk.Frame(outer, bg=THEME["card"], padx=20, pady=18)
    card.grid(row=0, column=0, sticky="n", pady=18)
    card.grid_columnconfigure(0, weight=1)

    title = tk.Label(card, text="Wordle Solver", bg=THEME["card"], fg=THEME["text"], font=FONT_TITLE)
    title.grid(row=0, column=0, sticky="w", pady=(0, 4))

    subtitle = tk.Label(
        card,
        text="Green = correct spot • Yellow = in word, wrong spot • Gray = not in word",
        bg=THEME["card"],
        fg=THEME["muted"],
        font=FONT_BODY,
    )
    subtitle.grid(row=1, column=0, sticky="w", pady=(0, 14))

    # create boxes for found letters
    sec1 = tk.Frame(card, bg=THEME["card2"], padx=14, pady=12)
    sec1.grid(row=2, column=0, sticky="ew", pady=(0, 10))
    sec1.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

    label = tk.Label(sec1, text="Found Letters (e.g. '---n-'): ", bg=THEME["card2"], fg=THEME["text"], font=FONT_H2)
    label.grid(row=0, column=0, columnspan=5, sticky="w", pady=(0,8))
    for i in range(5):
        foundBox = tk.Entry(
            sec1,
            width=2,
            font=FONT_TILE,
            justify="center", 
            bg=THEME["green"], 
            bd=0,
            highlightthickness=2,
            highlightbackground=THEME["border"],
            highlightcolor=THEME["btn"],
            validate="key", 
            validatecommand=(
                window.register(lambda char, foundBoxName:
                    updateFoundBox(char, foundBoxName, window)),
                        "%P",
                        "%W"
                )
            )
        foundBox.grid(row=1, column=i, padx=6, pady=(0, 4), ipadx=8, ipady=10, sticky="n")
        foundBoxes.append(foundBox)

    # found but wrong position
    sec2 = tk.Frame(card, bg=THEME["card2"], padx=14, pady=12)
    sec2.grid(row=3, column=0, sticky="ew", pady=(0, 10))
    sec2.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

    label = tk.Label(sec2, text="Found, but wrong position (e.g. '-e--s'): ", bg=THEME["card2"], fg=THEME["text"], font=FONT_H2)
    label.grid(row=0, column=0, columnspan=5, sticky="w", pady=(0,8))
    for i in range(5):
        excludeFromBox = tk.Entry(sec2, width=3, font=FONT_TILE, justify="center", bg=THEME["yellow"], bd=0, highlightthickness=2, highlightbackground=THEME["border"], highlightcolor=THEME["btn"])
        excludeFromBox.grid(row=1, column=i, padx=6, pady=(0, 4), ipadx=8, ipady=10, sticky="n")
        excludeAtBoxes.append(excludeFromBox)

    # exclude
    sec3 = tk.Frame(card, bg=THEME["card2"], padx=14, pady=12)
    sec3.grid(row=4, column=0, sticky="ew", pady=(0, 12))
    sec3.grid_columnconfigure(0, weight=1)

    label = tk.Label(sec3, text="Exclude Entirely (e.g. 'gratphoyblid'): ", bg=THEME["card2"], fg=THEME["text"], font=FONT_H2)
    label.grid(row=0, column=0, sticky="w", pady=(0,8))
    excludeBox = tk.Entry(sec3, width=24, font=("Segoe UI", 14), justify="center", bg=THEME["gray"], bd=0, highlightthickness=2, highlightbackground=THEME["border"], highlightcolor=THEME["btn"])
    excludeBox.grid(row=1, column=0, sticky="ew", ipady=8)

    # submit button
    out_wrap = tk.Frame(card, bg=THEME["card2"], padx=14, pady=12)
    out_wrap.grid(row=6, column=0, sticky="ew")
    out_wrap.grid_columnconfigure(0, weight=1)

    button = tk.Button(
        out_wrap, 
        text="Solve", 
        bg=THEME["bg"],
        fg="white",
        activebackground=THEME["btn_hover"],
        activeforeground="white",
        highlightthickness=2,
        highlightbackground=THEME["border"],
        highlightcolor=THEME["btn"],
        bd=0,
        padx=14,
        pady=10,
        font=("Segoe UI", 11, "bold"),
        command=lambda: 
            solve(foundBoxes, excludeBox, excludeAtBoxes, output))
        
    button.grid(row=0, column=0, sticky="ew", pady=10)
    button.bind("<Return>", lambda event: solve(foundBoxes, excludeBox, excludeAtBoxes, output))

    # output

    tk.Label(out_wrap, text="Results", bg=THEME["card2"], fg=THEME["text"], font=FONT_H2).grid(
        row=1, column=0, sticky="w", pady=(0, 8)
    )
    output = scrolledtext.ScrolledText(
        out_wrap,
        width=60,
        height=12,
        font=FONT_MONO,
        bd=0,
        bg=THEME["card2"],
        fg=THEME["text"],
        highlightthickness=2,
        highlightbackground=THEME["border"],
        highlightcolor=THEME["btn"],
    )
    output.grid(row=2, column=0, sticky="ew")

    foundBoxes[0].focus_set()
    window.mainloop()

if __name__ == "__main__":
    main()