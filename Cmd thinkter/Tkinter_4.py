import tkinter as tk
from tkinter import messagebox

def begroet_student():
    naam = invoer.get()
    if naam:
        messagebox.showinfo("Welkom", f"Hallo {naam}! Welkom bij deze applicatie.")
    else:
        messagebox.showwarning("Waarschuwing", "Voer eerst je naam in.")

# Maak het hoofdvenster van de GUI-toepassing
root = tk.Tk()
root.title("Laurens")

# Set the background color of the window to blue
root.configure(background="blue")

# Voeg een label toe met aangepaste kleuren en tekst
label = tk.Label(root, text="Voer je naam in:", bg="green", fg="white", font=("PiliApp", 12))
label.pack(pady=10)

# Voeg een invoerveld toe met aangepaste kleuren en lettertype
invoer = tk.Entry(root, bg="lightgray", fg="black", font=("PiliApp", 10))
invoer.pack(pady=5)

# Voeg een knop toe om de student te begroeten
knop = tk.Button(root, text="Begroet", command=begroet_student)
knop.pack(pady=5)

# Voer de hoofdgebeurtenislus uit
root.mainloop()