import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from CoolProp import CoolProp

# Creating tkinter window
window = tk.Tk()
window.title("FluProp")
window.geometry("1200x800")
window.iconbitmap("fluprop_logo.ico")

# Label
fluid_label = ttk.Label(window, text="Fluid-Auswahl:", background="green", foreground="white")
fluid_label.grid(row=0, column=0)

input1_label = ttk.Label(window, text="Input-Variable 1:", background="green", foreground="white")
input1_label.grid(row=1, column=0)

input2_label = ttk.Label(window, text="Input-Variable 2:", background="green", foreground="white")
input2_label.grid(row=2, column=0)

# Fluid Info Label
fluidinfo_label = ttk.Label(window, text="Fluidinformationen:")
fluidinfo_label.grid(row=0, column=4, columnspan=2)

pure_info_label = ttk.Label(window)
pure_info_label.grid(row=1, column=4)
molarmass_info_label = ttk.Label(window)
molarmass_info_label.grid(row=2, column=4)
gasconstant_info_label = ttk.Label(window)
gasconstant_info_label.grid(row=3, column=4)

#Kritischer Punkt Label
ctp_label = ttk.Label(window, text="Kritischer Punkt:")
ctp_label.grid(row=4, column=4)
ctp_druck_label = ttk.Label(window)
ctp_druck_label.grid(row=4, column=5)
ctp_temp_label = ttk.Label(window)
ctp_temp_label.grid(row=5, column=5)
ctp_dichte_label = ttk.Label(window)
ctp_dichte_label.grid(row=6, column=5)

#Tripelpunkt Label
tp_label = ttk.Label(window, text="Tripelpunkt:")
tp_label.grid(row=7, column=4)
tp_druck_label = ttk.Label(window)
tp_druck_label.grid(row=7, column=5)
tp_temp_label = ttk.Label(window)
tp_temp_label.grid(row=8, column=5)

#Fluidgrenzen Label
limit_label = ttk.Label(window, text="Fluidgrenzen:")
limit_label.grid(row=9, column=4)
maxtemp_label = ttk.Label(window)
maxtemp_label.grid(row=9, column=5)
mfloatemp_label = ttk.Label(window)
mfloatemp_label.grid(row=10, column=5)
maxp_label = ttk.Label(window)
maxp_label.grid(row=11, column=5)
minp_label = ttk.Label(window)
minp_label.grid(row=12, column=5)

#Berechnete Eigenschaften Label
calc_temp_label = ttk.Label(window)
calc_temp_label.grid(row=5, column=1, columnspan=2)
calc_p_label = ttk.Label(window)
calc_p_label.grid(row=6, column=1, columnspan=2)
calc_vq_label = ttk.Label(window)
calc_vq_label.grid(row=7, column=1, columnspan=2)
calc_sound_label = ttk.Label(window)
calc_sound_label.grid(row=8, column=1, columnspan=2)
calc_d_label = ttk.Label(window)
calc_d_label.grid(row=9, column=1, columnspan=2)
calc_h_label = ttk.Label(window)
calc_h_label.grid(row=10, column=1, columnspan=2)
calc_s_label = ttk.Label(window)
calc_s_label.grid(row=11, column=1, columnspan=2)
calc_u_label = ttk.Label(window)
calc_u_label.grid(row=12, column=1, columnspan=2)
calc_v_label = ttk.Label(window)
calc_v_label.grid(row=13, column=1, columnspan=2)
calc_st_label = ttk.Label(window)
calc_st_label.grid(row=14, column=1, columnspan=2)
calc_cp_label = ttk.Label(window)
calc_cp_label.grid(row=15, column=1, columnspan=2)
calc_cv_label = ttk.Label(window)
calc_cv_label.grid(row=16, column=1, columnspan=2)



def fluid_info(fluidselected):
    pure_info = CoolProp.get_fluid_param_string(fluidselected, "pure")
    if pure_info == "true":
        pure_info_label["text"] = "Reines Fluid: Ja"
    elif pure_info == "false":
        pure_info_label["text"] = "Reines Fluid: Nein"

    # Molare Masse
    molarmass_info = CoolProp.PropsSI("M", fluidselected)
    molarmass_info_label["text"] = "Molare Masse: " + str(round(molarmass_info * 1000, 4)) + " g/mol"
    gascostant = CoolProp.PropsSI("gas_constant", fluidselected)
    gasconstant_info_label["text"] = "Spezifische Gaskonstante: " + str(
        round(gascostant / molarmass_info, 1)) + " J/kg/K"

    # Kritischer Punkt
    ctp_druck = CoolProp.PropsSI("pcrit", fluidselected)
    ctp_druck_label["text"] = "Druck: " + str(ctp_druck) + " Pa"
    ctp_temp = CoolProp.PropsSI("Tcrit", fluidselected)
    ctp_temp_label["text"] = "Temperatur: " + str(ctp_temp) + " K"
    ctp_dichte = CoolProp.PropsSI("rhocrit", fluidselected)
    ctp_dichte_label["text"] = "Dichte: " + str(round(ctp_dichte, 1)) + " kg/m^3"

    # Tripelpunkt
    tp_druck = CoolProp.PropsSI("ptriple", fluidselected)
    tp_druck_label["text"] = "Druck: " + str(tp_druck) + " Pa"
    tp_temp = CoolProp.PropsSI("Ttriple", fluidselected)
    tp_temp_label["text"] = "Temperatur: " + str(tp_temp) + " K"

    # Fluidgrenzen
    maxp = CoolProp.PropsSI("pmax", fluidselected)
    maxp_label["text"] = "Max. Druck: " + str(maxp) + " Pa"
    maxtemp = CoolProp.PropsSI("Tmax", fluidselected)
    maxtemp_label["text"] = "Max. Temperatur: " + str(maxtemp) + " K"
    minp = CoolProp.PropsSI("pmin", fluidselected)
    minp_label["text"] = "Min. Druck: " + str(round(minp, 2)) + " Pa"
    mfloatemp = CoolProp.PropsSI("Tmin", fluidselected)
    mfloatemp_label["text"] = "Min. Temperatur: " + str(round(mfloatemp, 3)) + " K"


def on_select_fluid(event):
    fluid_info(event.widget.get())


# Fluidinfos am Anfang einmal ausgeben
fluid_info("water")

# Fluid Combobox
selected_fluid = tk.StringVar()
cp_fluids = CoolProp.FluidsList()
fluid_combobox = ttk.Combobox(window, width=40, textvariable=selected_fluid, values=cp_fluids, state="readonly")
fluid_combobox.grid(row=0, column=1, columnspan=2)
fluid_combobox.set("Water")
fluid_combobox.bind("<<ComboboxSelected>>", on_select_fluid)

# Input Variablen
variables = ["Dichte ρ", "Druck p", "Temperatur T", "Spezifische Enthalpy h", "Spezifische Entropie s",
             "Dampfqualität x"]


# Input 1
def on_select_inpu1(event):
    selected_input1 = event.widget.get()
    if selected_input1 == "Dichte ρ":
        input1einheit_label["text"] = "kg/m^3"
    elif selected_input1 == "Druck p":
        input1einheit_label["text"] = "Pa"
    elif selected_input1 == "Temperatur T":
        input1einheit_label["text"] = "K"
    elif selected_input1 == "Spezifische Enthalpy h":
        input1einheit_label["text"] = "J/kg"
    elif selected_input1 == "Spezifische Entropie s":
        input1einheit_label["text"] = "J/(kg·K)"
    elif selected_input1 == "Dampfqualität x":
        input1einheit_label["text"] = "kg/kg)"


selected_variable1 = tk.StringVar()
input1_combobox = ttk.Combobox(window, width=20, textvariable=selected_variable1, values=variables, state="readonly")
input1_combobox.grid(row=1, column=1)
input1_combobox.set("Druck p")
input1_combobox.bind("<<ComboboxSelected>>", on_select_inpu1)

input1einheit_label = ttk.Label(window, text="Pa", background="green", foreground="white")
input1einheit_label.grid(row=1, column=3)

input1_var = tk.StringVar()
input1_entry = ttk.Entry(window, textvariable=input1_var)
input1_entry.grid(row=1, column=2)


# Input 2
def on_select_inpu2(event):
    selected_input2 = event.widget.get()
    if selected_input2 == "Dichte ρ":
        input2einheit_label["text"] = "kg/m^3"
    elif selected_input2 == "Druck p":
        input2einheit_label["text"] = "Pa"
    elif selected_input2 == "Temperatur T":
        input2einheit_label["text"] = "K"
    elif selected_input2 == "Spezifische Enthalpy h":
        input2einheit_label["text"] = "J/kg"
    elif selected_input2 == "Spezifische Entropie s":
        input2einheit_label["text"] = "J/(kg·K)"
    elif selected_input2 == "Dampfqualität x":
        input2einheit_label["text"] = "kg/kg)"


selected_variable2 = tk.StringVar()
input2_combobox = ttk.Combobox(window, width=20, textvariable=selected_variable2, values=variables, state="readonly")
input2_combobox.grid(row=2, column=1)
input2_combobox.set("Temperatur T")
input2_combobox.bind("<<ComboboxSelected>>", on_select_inpu2)

input2einheit_label = ttk.Label(window, text="K", background="green", foreground="white")
input2einheit_label.grid(row=2, column=3)

input2_var = tk.StringVar()
input2_entry = ttk.Entry(window, textvariable=input2_var)
input2_entry.grid(row=2, column=2)


#Berechnungsfunktion
def calc():
    if selected_variable1.get() == "Dichte ρ":
        if selected_variable2.get() == "Dichte ρ":
            tkinter.messagebox.showwarning("Warnung", "Bitte zwei unterschiedliche Variablen zur Berechnung wählen!")
        elif selected_variable2.get() == "Druck p":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")
        elif selected_variable2.get() == "Temperatur T":
            prop_ausgabe("D", "T")
        elif selected_variable2.get() == "Spezifische Enthalpy h":
            prop_ausgabe("D", "H")
        elif selected_variable2.get() == "Spezifische Entropie s":
            prop_ausgabe("D", "S")
        elif selected_variable2.get() == "Dampfqualität x":
            prop_ausgabe("D", "Q")

    if selected_variable1.get() == "Druck p":
        if selected_variable2.get() == "Dichte ρ":
           prop_ausgabe("P", "D")
        elif selected_variable2.get() == "Druck p":
            tkinter.messagebox.showwarning("Warnung", "Bitte zwei unterschiedliche Variablen zur Berechnung wählen!")
        elif selected_variable2.get() == "Temperatur T":
            prop_ausgabe("P", "T")
        elif selected_variable2.get() == "Spezifische Enthalpy h":
            prop_ausgabe("P", "H")
        elif selected_variable2.get() == "Spezifische Entropie s":
            prop_ausgabe("P", "S")
        elif selected_variable2.get() == "Dampfqualität x":
            prop_ausgabe("P", "Q")

    if selected_variable1.get() == "Temperatur T":
        if selected_variable2.get() == "Dichte ρ":
            prop_ausgabe("T", "D")
        elif selected_variable2.get() == "Druck p":
            prop_ausgabe("T", "P")
        elif selected_variable2.get() == "Temperatur T":
            tkinter.messagebox.showwarning("Warnung", "Bitte zwei unterschiedliche Variablen zur Berechnung wählen!")
        elif selected_variable2.get() == "Spezifische Enthalpy h":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")
        elif selected_variable2.get() == "Spezifische Entropie s":
            prop_ausgabe("T", "S")
        elif selected_variable2.get() == "Dampfqualität x":
            prop_ausgabe("T", "Q")

    if selected_variable1.get() == "Spezifische Enthalpy h":
        if selected_variable2.get() == "Dichte ρ":
            prop_ausgabe("H", "D")
        elif selected_variable2.get() == "Druck p":
            prop_ausgabe("H", "P")
        elif selected_variable2.get() == "Temperatur T":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")
        elif selected_variable2.get() == "Spezifische Enthalpy h":
            tkinter.messagebox.showwarning("Warnung", "Bitte zwei unterschiedliche Variablen zur Berechnung wählen!")
        elif selected_variable2.get() == "Spezifische Entropie s":
            prop_ausgabe("H", "S")
        elif selected_variable2.get() == "Dampfqualität x":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")

    if selected_variable1.get() == "Spezifische Entropie s":
        if selected_variable2.get() == "Dichte ρ":
            prop_ausgabe("S", "D")
        elif selected_variable2.get() == "Druck p":
            prop_ausgabe("S", "P")
        elif selected_variable2.get() == "Temperatur T":
            prop_ausgabe("S", "T")
        elif selected_variable2.get() == "Spezifische Enthalpy h":
            prop_ausgabe("S", "H")
        elif selected_variable2.get() == "Spezifische Entropie s":
            tkinter.messagebox.showwarning("Warnung", "Bitte zwei unterschiedliche Variablen zur Berechnung wählen!")
        elif selected_variable2.get() == "Dampfqualität x":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")

    if selected_variable1.get() == "Dampfqualität x":
        if selected_variable2.get() == "Dichte ρ":
            prop_ausgabe("Q", "D")
        elif selected_variable2.get() == "Druck p":
            prop_ausgabe("Q", "P")
        elif selected_variable2.get() == "Temperatur T":
            prop_ausgabe("Q", "T")
        elif selected_variable2.get() == "Spezifische Enthalpy h":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")
        elif selected_variable2.get() == "Spezifische Entropie s":
            tkinter.messagebox.showwarning("Warnung", "Dieses Paar von Eingabevariablen ist nicht möglich! Bitte eine andere Kombination wählen.")
        elif selected_variable2.get() == "Dampfqualität x":
            tkinter.messagebox.showwarning("Warnung", "Bitte zwei unterschiedliche Variablen zur Berechnung wählen!")



def prop_ausgabe(input1, input2):
    try:
        calc_temp_label["text"] = "Temperatur T= " + str(CoolProp.PropsSI("T", input1, float(input1_var.get()),
                                                                          input2, float(input2_var.get()),
                                                                          selected_fluid.get())) + " K"
    except:
        calc_temp_label["text"] = "Temperatur T="
    try:
        calc_p_label["text"] = "Druck p= " + str(CoolProp.PropsSI("P", input1, float(input1_var.get()), input2,
                                                                  float(input2_var.get()), selected_fluid.get())) + " Pa"
    except:
        calc_p_label["text"] = "Druck p="
    try:
        calc_vq_label["text"] = "Dampfqualität x= " + str(round(CoolProp.PropsSI("Q", input1,
                                                                                 float(input1_var.get()), input2,
                                                                                 float(input2_var.get()), selected_fluid.get()), 6)) + " kg/kg"
    except:
        calc_vq_label["text"] = "Dampfqualität x="
    try:
        calc_sound_label["text"] = "Schallgeschwindigkeit c= " + str(round(CoolProp.PropsSI("A", input1,
                                                                                            float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " m/s"
    except:
        calc_sound_label["text"] = "Schallgeschwindigkeit c="
    try:
        calc_d_label["text"] = "Dichte ρ= " + str(round(CoolProp.PropsSI("D", input1, float(input1_var.get()),
                                                                         input2, float(input2_var.get()), selected_fluid.get()), 6)) + " kg/m^3"
    except:
        calc_d_label["text"] = "Dichte ρ="
    try:
        calc_h_label["text"] = "Spezifische Enthalpie h= " + str(round(CoolProp.PropsSI("H", input1,
                                                                                        float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " J/kg"
    except:
        calc_h_label["text"] = "Spezifische Enthalpie h="
    try:
        calc_s_label["text"] = "Spezifische Entropie s= " + str(round(CoolProp.PropsSI("S", input1,
                                                                                       float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " J/kg/K"
    except:
        calc_s_label["text"] = "Spezifische Entropie s="
    try:
        calc_u_label["text"] = "Spezifische innere Energie u= " + str(round(CoolProp.PropsSI("U", input1,
                                                                                             float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " J/kg"
    except:
        calc_u_label["text"] = "Spezifische innere Energie u="
    try:
        calc_v_label["text"] = "Viskosität η= " + str(round(CoolProp.PropsSI("V", input1, float(input1_var.get()),
                                                                             input2, float(input2_var.get()), selected_fluid.get()), 6)) + " Pa·s"
    except:
        calc_v_label["text"] = "Viskosität η="
    try:
        calc_st_label["text"] = "Oberflächenspannung σ= " + str(round(CoolProp.PropsSI("surface_tension",
                                                                                       input1, float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " N/m"
    except:
        calc_st_label["text"] = "Oberflächenspannung σ="
    try:
        calc_cp_label["text"] = "Spezifische Wärmekapazität (Druck konstant) cp= " + str(round(
            CoolProp.PropsSI("Cpmass", input1, float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " J/kg/K"
    except:
        calc_cp_label["text"] = "Spezifische Wärmekapazität (Druck konstant) cp="
    try:
        calc_cv_label["text"] = "Spezifische Wärmekapazität (Volumen konstant) cv= " + str(round(
            CoolProp.PropsSI("Cvmass", input1, float(input1_var.get()), input2, float(input2_var.get()), selected_fluid.get()), 6)) + " J/kg/K"
    except:
        calc_cv_label["text"] = "Spezifische Wärmekapazität (Volumen konstant) cv="


# Berechnen Button
calc_btn = ttk.Button(window, text="Berechnen", command=calc)
calc_btn.grid(row=3, column=0)

# Infinite Loop
window.mainloop()
