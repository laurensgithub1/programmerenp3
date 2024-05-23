import tkinter as tk

# Maak het hoofdvenster van de GUI-toepassing
root = tk.Tk()
root.title("Mijn eerste GUI-toepassing")
root.geometry("400x300")

# Voeg een label toe
label = tk.Label(root, text="Hallo, wereld!")
label.pack(pady=10)

# Functie die wordt aangeroepen wanneer de knop wordt geklikt
def knop_klik():
    label.config(text="Knop geklikt!")

# Voeg een knop toe
knop = tk.Button(root, text="Klik mij", command=knop_klik)
knop.pack(pady=10)

# Voer de hoofdgebeurtenislus uit
root.mainloop()