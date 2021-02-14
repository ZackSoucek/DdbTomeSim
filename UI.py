from tkinter import *
from Challenge import *
import pickle
import Tooltip


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.defaultChal = Challenge("", 0, 0, Side.BOTH, 0, State.INCOMPLETE, (0, 0), "default chal description")
        self.init_window()
        
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
        # TODO actually get the challenges for the tome
        
        
        #this part should load the whole current level into memory and create their buttons
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
        
        for i in range(len(challenges)):
            buttons.append(Button(self, text = challenges[i].name, command = lambda: self.toggle_type(challenges[i])))
            buttons[i].place(x = challenges[i].position[0], y = challenges[i].position[1])
            Tooltip.createToolTip(buttons[i], self.tooltipString(challenges[i]))
    def tooltipString(self, chal: Challenge):
        s = "Name: {name}\nSide: {side}\nValue: {value:,}\nState: {state}\nDescription: {descr}".format(
            name = chal.name,
            side = chal.side,
            value = chal.value,
            state = str(chal.state),
            descr = chal.description
        )
        #WARNING_____________________________________________________________________
        #this might end up with locking in the tooltip when placed, will need to change the tooltip or something when state changes
        return s
        
    def toggle_type(self, chal: Challenge):
        chal.increment()
        
    def quit_command(self):
        quit(0)
