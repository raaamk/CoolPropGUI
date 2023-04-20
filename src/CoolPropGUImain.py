import tkinter as tk
import tkinter.font as tkfont


class App:
    def __init__(self, root):
        # setting title
        root.title("GUI für CoolProp")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_32 = tk.Label(root)
        ft = tkfont.Font(family='Times', size=10)
        GLabel_32["font"] = ft
        GLabel_32["fg"] = "#333333"
        GLabel_32["justify"] = "center"
        GLabel_32["text"] = "label"
        GLabel_32.place(x=40, y=30, width=70, height=25)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
