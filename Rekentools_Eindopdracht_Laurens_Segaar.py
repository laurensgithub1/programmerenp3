import tkinter as tk
from tkinter import messagebox
import random
import math

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hoofdpagina")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Homepagina", font=("Arial", 16))
        self.title_label.pack(pady=20)

        self.speed_button = tk.Button(self, text="Bereken Reistijd", command=self.open_travel_time_calculator)
        self.speed_button.pack()

        self.btw_button = tk.Button(self, text="Bereken BTW", command=self.open_btw_calculator)
        self.btw_button.pack()

        self.circle_button = tk.Button(self, text="Bereken Cirkel", command=self.open_circle_calculator)
        self.circle_button.pack()

        self.guess_button = tk.Button(self, text="Getallen Raden", command=self.open_guess_number_game)
        self.guess_button.pack() #Deze methode maakt en plaatst een label en vier knoppen in het hoofdvenster. Elke knop opent een ander venster wanneer erop wordt geklikt.

    def open_travel_time_calculator(self):
        travel_time_window = TravelTimeWindow(self)

    def open_btw_calculator(self):
        btw_window = BTWCalculatorWindow(self)

    def open_circle_calculator(self):
        circle_window = CircleCalculatorWindow(self)

    def open_guess_number_game(self):
        guess_window = GuessNumberWindow(self) #Deze methoden maken een nieuw vensterobject aan voor elke berekening.

class TravelTimeWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Reistijd Berekenen")
        self.geometry("300x200")

        self.master = master

        self.distance_label = tk.Label(self, text="Afstand (in km):")
        self.distance_label.pack()

        self.distance_entry = tk.Entry(self)
        self.distance_entry.pack()

        self.speed_label = tk.Label(self, text="Snelheid (in km/u):")
        self.speed_label.pack()

        self.speed_entry = tk.Entry(self)
        self.speed_entry.pack()

        self.calculate_button = tk.Button(self, text="Bereken", command=self.calculate_travel_time)
        self.calculate_button.pack()

    def calculate_travel_time(self):
        try:
            distance = float(self.distance_entry.get())
            speed = float(self.speed_entry.get())

            time = distance / speed

            messagebox.showinfo("Reistijd", f"Je bent {time:.2f} uur onderweg.")
        except ValueError:
            messagebox.showerror("Fout", "Ongeldige invoer!") #Deze klasse creëert een nieuw venster waar de gebruiker de afstand en snelheid kan invoeren om de reistijd te berekenen.

class BTWCalculatorWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("BTW Calculator")
        self.geometry("300x250")

        self.master = master

        self.amount_label = tk.Label(self, text="Te betalen bedrag:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.btw_label = tk.Label(self, text="BTW percentage:")
        self.btw_label.pack()

        self.btw_var = tk.StringVar(self)
        self.btw_var.set("21%")  # standaard waarde

        self.btw_optionmenu = tk.OptionMenu(self, self.btw_var, "21%", "9%")
        self.btw_optionmenu.pack()

        self.calculate_button = tk.Button(self, text="Bereken BTW", command=self.calculate_btw)
        self.calculate_button.pack()

    def calculate_btw(self):
        try:
            amount = float(self.amount_entry.get())
            btw_choice = self.btw_var.get()

            if btw_choice == "21%":
                btw_percentage = 0.21
            elif btw_choice == "9%":
                btw_percentage = 0.09

            btw_amount = amount * btw_percentage
            total_amount = amount + btw_amount

            messagebox.showinfo("BTW Berekening", f"BTW: €{btw_amount:.2f}\nTotaal bedrag: €{total_amount:.2f}")
        except ValueError:
            messagebox.showerror("Fout", "Verkeerde invoer!") #Deze klasse creëert een nieuw venster waar de gebruiker een bedrag kan invoeren om de BTW en het totale bedrag te berekenen (Als de gebruiker niet op 21% drukt, dan word er eerst 9% BTW uit gerekend).

class CircleCalculatorWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cirkel Calculator")
        self.geometry("300x250")

        self.master = master

        self.diameter_label = tk.Label(self, text="Diameter:")
        self.diameter_label.pack()

        self.diameter_entry = tk.Entry(self)
        self.diameter_entry.pack()

        self.unit_label = tk.Label(self, text="Eenheid (m of cm):")
        self.unit_label.pack()

        self.unit_entry = tk.Entry(self)
        self.unit_entry.pack()

        self.calculate_button = tk.Button(self, text="Bereken", command=self.calculate_circle)
        self.calculate_button.pack()

    def calculate_circle(self):
        try:
            diameter = float(self.diameter_entry.get())
            unit = self.unit_entry.get()

            if unit == "m":
                radius = diameter / 2
            elif unit == "cm":
                radius = diameter / 200  # omzetten naar meter

            circumference = 2 * math.pi * radius
            area = math.pi * (radius ** 2)

            messagebox.showinfo("Cirkel Berekening", f"Omtrek: {circumference:.2f} {unit}\nOppervlakte: {area:.2f} {unit}^2")
        except ValueError:
            messagebox.showerror("Fout", "Ongeldige invoer!") #Deze klasse creëert een nieuw venster waar de gebruiker de diameter van een cirkel kan invoeren om de omtrek en oppervlakte te berekenen.
        
class GuessNumberWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Getallen Raden")
        self.geometry("300x200")

        self.master = master

        self.secret_number = random.randint(1, 15)
        self.guess_label = tk.Label(self, text="Doe een gok (1-15):")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self, text="Gok", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess == self.secret_number:
                messagebox.showinfo("Correct", "Gefeliciteerd, je hebt het juiste nummer geraden!")
                self.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Te laag", "Het nummer is hoger. Probeer opnieuw!")
            else:
                messagebox.showinfo("Te hoog", "Het nummer is lager. Probeer opnieuw!")
        except ValueError:
            messagebox.showerror("Fout", "Ongeldige invoer! Voer een geheel getal in tussen 1 en 15.") #Deze klasse creëert een nieuw venster waar de gebruiker een nummer kan raden tussen 1 en 15. De gebruiker krijgt feedback of het geraden nummer te hoog of te laag is.

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop() #Dit is het startpunt van de toepassing. Het creëert een instantie van MainApplication en start de mainloop, die de GUI actief houdt.