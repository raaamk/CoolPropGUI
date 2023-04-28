import tkinter as tk
import tkinter.font as tkfont


class App:
    def __init__(self, window):
        # setting title
        window.title("GUI für CoolProp")
        # setting window size
        width = 600
        height = 500
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window.geometry(alignstr)
        window.resizable(width=False, height=False)

        GLabel_32 = tk.Label(window)
        ft = tkfont.Font(family='Times', size=10)
        GLabel_32["font"] = ft
        GLabel_32["fg"] = "#333333"
        GLabel_32["justify"] = "center"
        GLabel_32["text"] = "label"
        GLabel_32.place(x=40, y=30, width=70, height=25)


if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()
