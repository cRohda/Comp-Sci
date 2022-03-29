import webbrowser as wb
import tkinter as tk

# Opens github repository for my project
wb.open("https://github.com/cRohda/Comp-Sci/tree/main/Assignments/Final%20Projects/Tic%20Tac%20Toe%20Pygame")

# Opens instructions window
window = tk.Tk()

# Sets instructions
window.title("DOWNLOAD INSTRUCTIONS")
instructions1 = tk.Label(text="1) Download all files here", font=("Ariel", 50))
instructions2 = tk.Label(text="2) Store them all in the same new folder", font=("Ariel", 50))
instructions3 = tk.Label(text="3) Run the file 'main_p.py'", font=("Ariel", 50))
instructions1.pack()
instructions2.pack()
instructions3.pack()

window.mainloop()
