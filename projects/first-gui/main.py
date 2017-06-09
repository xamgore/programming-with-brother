from tkinter import Tk , BOTH, Button, Frame
from tkinter.ttk import Style


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.initUI()

    def centerWindow(self):
        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = sw / 2 - w / 2
        y = sh / 2 - h / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def initUI(self):
        self.parent.title("Quit button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",
                            command=self.quit)
        quitButton.place(x=50, y=50)

        centrateButton = Button(self, text="Centrate", command=self.centerWindow)
        centrateButton.place(x=100, y = 50)
        # centrateButton.

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()