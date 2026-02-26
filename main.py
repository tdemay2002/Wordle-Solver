# imports
from viewController import updateFoundBox, solve
from tkinter import scrolledtext
import tkinter as tk

window = None
foundBoxes = []
excludeBox = None
excludeAtBoxes = []
output = None

def main():
    global window
    global excludeBox
    global excludeAtBoxes
    global output

    window = tk.Tk()
    window.title("Wordle Solver")

    # create boxes for found letters
    label = tk.Label(window, text="Found Letters (e.g. '---n-'): ")
    label.grid(row=0, column=0, columnspan=5, pady=(10,0))
    for i in range(5):
        foundBox = tk.Entry(window, width=3, font=("Arial",18), justify="center", bg="green",
                            validate="key", validatecommand=(window.register(lambda char, foundBoxName: updateFoundBox(char, foundBoxName, window)), "%P", "%W"))
        foundBox.grid(row=1, column=i, padx=5, pady=10)
        foundBoxes.append(foundBox)

    label = tk.Label(window, text=f"Found, but wrong position (e.g. '-e--s'): ")
    label.grid(row=4, column=0, columnspan=5, padx=5)
    for i in range(5):
        excludeFromBox = tk.Entry(window, width=3, font=("Arial",18), justify="center", bg="yellow")
        excludeFromBox.grid(row=5, column=i, padx=5)
        excludeAtBoxes.append(excludeFromBox)

    label = tk.Label(window, text="Exclude Entirely (e.g. 'gratphoyblid'): ")
    label.grid(row=4+5, column=0, columnspan=5, pady=(10,0))
    excludeBox = tk.Entry(window, width=10, font=("Arial",18), justify="center", bg="darkgrey")
    excludeBox.grid(row=5+5, column=0, columnspan=5, pady=10)


    button = tk.Button(window, text="Solve", command=lambda: solve(foundBoxes, excludeBox, excludeAtBoxes, output))
    button.grid(row=11, column=0, columnspan=5, pady=20)
    button.bind("<Return>", lambda event: solve(foundBoxes, excludeBox, excludeAtBoxes, output))

    output = scrolledtext.ScrolledText(
        window,
        width=50,
        height=15,
        font=("Consolas", 12)
    )
    output.grid(row=12, column=0, columnspan=5, padx=10, pady=(0,10))

    window.mainloop()

if __name__ == "__main__":
    main()