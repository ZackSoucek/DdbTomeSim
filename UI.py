from tkinter import *
from Challenge import *
import pickle


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.defaultChal = Challenge("", 0, 0, Side.BOTH, 0, (0, 0), "")\
        #making a default to use in the event of empty
    
    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("DBDTomeSimulator")
        # allowing the widget to take the full space of the root window
        self.pack(fill = BOTH, expand = 1)
        # creating a button instance
        quitButton = Button(self, text = "Quit", command = self.quit_command)
        # placing the button on my window
        quitButton.place(x = 0, y = 0)
       
        tome = 1
        level = 1
        # TODO tome switcher buttons
        # TODO level switcher buttons
        #these will habe to run the button and challenge parseing
        level1 = open("Data\Baseline\Tome1\level1", 'rb')
        challenges = []
        buttons = []
        try:
            while True:
                chal = pickle.load(level1)
                challenges.append(chal)
        except EOFError:
            # i expect an EofError after running out of objects
            # desired behavior is to do nothing and move on
            pass
        
        # TODO actually get the challenges for the tome
        for i in range(len(challenges)):
            buttons.append(Button(self, text = challenges[i].name))
            buttons[i].place(x = challenges[i].position[0], y = challenges[i].position[1],
                             command = self.toggle_type(challenges[i]))
            buttons[i].bind("<Enter>", self.update_hover_text(challenges[i]))
            buttons[i].bind("<Leave>", self.update_hover_text(self.defaultChal))
            # places the button at its x and y pos
            
    def update_hover_text(self, chal: Challenge):
        
        
        pass
    
        
    def toggle_type(self, chal: Challenge):
        chal.increment()
    def quit_command(self):
        quit(0)
