import tkinter as tk
from tkinter import ttk
from CoolProp import CoolProp

# Creating tkinter window
window = tk.Tk()
window.title("FluProp")
window.geometry("500x500")

fluid_label = ttk.Label(window, text="Fluid-Auswahl:", background="green", foreground="white")
fluid_label.grid(row=0, column=0)

input1_label = ttk.Label(window, text="Input-Variable 1:", background="green", foreground="white")
input1_label.grid(row=1, column=0)

input2_label = ttk.Label(window, text="Input-Variable 2:", background="green", foreground="white")
input2_label.grid(row=2, column=0)

# Fluid Combobox
selected_fluid = tk.StringVar()
cp_fluids = CoolProp.FluidsList()
fluid_combobox = ttk.Combobox(window, width=40, textvariable=selected_fluid, values=cp_fluids, state="readonly")
fluid_combobox.grid(row=0, column=1, columnspan=2)
fluid_combobox.set("Water")

variables = ["Dichte ρ", "Druck p", "Temperatur T", "Spezifische Enthalpy h", "Spezifische Entropie s", "Dampfqualität x"]


#Input 1
selected_variable1 = tk.StringVar()
input1_combobox = ttk.Combobox(window, width=20, textvariable=selected_variable1, values=variables, state="readonly")
input1_combobox.grid(row=1, column=1)
input1_combobox.set("Druck p")

input1einheit_label = ttk.Label(window, text="Pa", background="green", foreground="white")
input1einheit_label.grid(row=1, column=3)

input1_var = tk.StringVar()
input1_entry = ttk.Entry(window, textvariable=input1_var)
input1_entry.grid(row=1, column=2)

#Input 2
selected_variable2 = tk.StringVar()
input2_combobox = ttk.Combobox(window, width=20, textvariable=selected_variable2, values=variables, state="readonly")
input2_combobox.grid(row=2, column=1)
input2_combobox.set("Temperatur T")

input2einheit_label = ttk.Label(window, text="K", background="green", foreground="white")
input2einheit_label.grid(row=2, column=3)

input2_var = tk.StringVar()
input2_entry = ttk.Entry(window, textvariable=input2_var)
input2_entry.grid(row=2, column=2)

#Infinite Loop
window.mainloop()
