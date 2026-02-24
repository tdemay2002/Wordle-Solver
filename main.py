# imports
from viewController import updateFoundBox, solve
from tkinter import scrolledtext
import tkinter as tk

window = None
foundBoxes = []
includeBox = None
excludeBox = None
excludeBoxes = []
output = None

def main():
    global window
    global includeBox
    global excludeBox
    global excludeBoxes
    global output

    window = tk.Tk()
    window.title("Wordle Solver")

    # create boxes for found letters
    label = tk.Label(window, text="Found Letters (e.g. '---n-'): ")
    label.grid(row=0, column=0, columnspan=5, pady=(10,0))
    for i in range(5):
        foundBox = tk.Entry(window, width=3, font=("Arial",18), justify="center", 
                            validate="key", validatecommand=(window.register(lambda char, foundBoxName: updateFoundBox(char, foundBoxName, window)), "%P", "%W"))
        foundBox.grid(row=1, column=i, padx=5, pady=10)
        foundBoxes.append(foundBox)

    label = tk.Label(window, text="Include Anywhere (e.g. 'se'): ")
    label.grid(row=2, column=0, columnspan=5, pady=(10,0))
    includeBox = tk.Entry(window, width=10, font=("Arial",18), justify="center")
    includeBox.grid(row=3, column=0, columnspan=5, pady=10)

    label = tk.Label(window, text="Exclude Entirely (e.g. 'gratphoyblid'): ")
    label.grid(row=4, column=0, columnspan=5, pady=(10,0))
    excludeBox = tk.Entry(window, width=10, font=("Arial",18), justify="center")
    excludeBox.grid(row=5, column=0, columnspan=5, pady=10)

    includeFrame = tk.Frame(window)
    includeFrame.grid(row=6, column=0, columnspan=5, pady=(10,0))
    for i in range(5):
        label = tk.Label(includeFrame, text=f"Exclude from position {i}? ")
        label.grid(row=6+i, column=0, padx=5)
        excludeBox = tk.Entry(includeFrame, width=10, font=("Arial",18), justify="center")
        excludeBox.grid(row=6+i, column=1, padx=5)
        excludeBoxes.append(excludeBox)


    button = tk.Button(window, text="Solve", command=lambda: solve(foundBoxes, includeBox, excludeBox, excludeBoxes, output))
    button.grid(row=11, column=0, columnspan=5, pady=20)
    button.bind("<Return>", lambda event: solve(foundBoxes, includeBox, excludeBox, excludeBoxes, output))

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