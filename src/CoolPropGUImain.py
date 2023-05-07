import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1123
        height=645
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_845=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#333333"
        GLabel_845["justify"] = "center"
        GLabel_845["text"] = "Fluid-Auswahl:"
        GLabel_845.place(x=50,y=20,width=102,height=30)

        GListBox_542=tk.Listbox(root)
        GListBox_542["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_542["font"] = ft
        GListBox_542["fg"] = "#333333"
        GListBox_542["justify"] = "center"
        GListBox_542.place(x=170,y=20,width=80,height=25)

        GLabel_768=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "Input 1:"
        GLabel_768.place(x=40,y=60,width=70,height=25)

        GLabel_379=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_379["font"] = ft
        GLabel_379["fg"] = "#333333"
        GLabel_379["justify"] = "center"
        GLabel_379["text"] = "Input 2:"
        GLabel_379.place(x=40,y=90,width=70,height=25)

        GLineEdit_563=tk.Entry(root)
        GLineEdit_563["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_563["font"] = ft
        GLineEdit_563["fg"] = "#333333"
        GLineEdit_563["justify"] = "center"
        GLineEdit_563["text"] = "Entry"
        GLineEdit_563.place(x=260,y=60,width=70,height=25)

        GLineEdit_631=tk.Entry(root)
        GLineEdit_631["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_631["font"] = ft
        GLineEdit_631["fg"] = "#333333"
        GLineEdit_631["justify"] = "center"
        GLineEdit_631["text"] = "Entry"
        GLineEdit_631.place(x=260,y=90,width=70,height=25)

        GListBox_187=tk.Listbox(root)
        GListBox_187["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_187["font"] = ft
        GListBox_187["fg"] = "#333333"
        GListBox_187["justify"] = "center"
        GListBox_187.place(x=170,y=60,width=80,height=25)

        GListBox_470=tk.Listbox(root)
        GListBox_470["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_470["font"] = ft
        GListBox_470["fg"] = "#333333"
        GListBox_470["justify"] = "center"
        GListBox_470.place(x=170,y=90,width=80,height=25)

        GLabel_51=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_51["font"] = ft
        GLabel_51["fg"] = "#333333"
        GLabel_51["justify"] = "center"
        GLabel_51["text"] = "label"
        GLabel_51.place(x=340,y=60,width=70,height=25)

        GLabel_713=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_713["font"] = ft
        GLabel_713["fg"] = "#333333"
        GLabel_713["justify"] = "center"
        GLabel_713["text"] = "label"
        GLabel_713.place(x=340,y=90,width=70,height=25)

        GLabel_976=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_976["font"] = ft
        GLabel_976["fg"] = "#333333"
        GLabel_976["justify"] = "center"
        GLabel_976["text"] = "label"
        GLabel_976.place(x=600,y=20,width=70,height=25)

        GLabel_884=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_884["font"] = ft
        GLabel_884["fg"] = "#333333"
        GLabel_884["justify"] = "center"
        GLabel_884["text"] = "label"
        GLabel_884.place(x=600,y=50,width=70,height=25)

        GLabel_623=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_623["font"] = ft
        GLabel_623["fg"] = "#333333"
        GLabel_623["justify"] = "center"
        GLabel_623["text"] = "label"
        GLabel_623.place(x=600,y=80,width=70,height=25)

        GButton_383=tk.Button(root)
        GButton_383["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_383["font"] = ft
        GButton_383["fg"] = "#000000"
        GButton_383["justify"] = "center"
        GButton_383["text"] = "Button"
        GButton_383.place(x=50,y=130,width=232,height=34)
        GButton_383["command"] = self.GButton_383_command

    def GButton_383_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
