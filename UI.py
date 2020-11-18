from tkinter import *
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("DBDTomeSimulator")
        # allowing the widget to take the full space of the root window
        self.pack(fill = BOTH, expand = 1)
        # creating a button instance
        quitButton = Button(self, text = "Quit", command=self.quit_command)
        # placing the button on my window
        quitButton.place(x = 0, y = 0)
        
    def quit_command(self):
        quit(0)