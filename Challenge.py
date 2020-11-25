from enum import Enum, auto


class State(Enum):
    INCOMPLETE = auto()
    COMPLETE = auto()
    CLAIMED = auto()


class Side(Enum):
    SURVIVOR = auto()
    KILLER = auto()
    BOTH = auto()


class Challenge:
    def __init__(self, name: str, tome: int, level: int, side: Side, value: int, state: State, position: tuple, description: str):
        self.name = name
        self.tome = tome
        self.level = level
        self.side = side
        self.value = value
        self.state = state
        self.position = position
        self.neighbors = []
        self.description = description
    
    '''comparisons based on value'''
    def increment(self):
        if self.state == State.INCOMPLETE:
            self.state = State.COMPLETE
        if self.state == State.COMPLETE:
            self.state = State.CLAIMED
        if self.state == State.CLAIMED:
            self.state = State.INCOMPLETE

    def __lt__(self, other) -> bool:
        return self.value < other.value
    
    def __gt__(self, other) -> bool:
        return self.value > other.value
    
    def __eq__(self, other) -> bool:
        return self.value == other.value
    
    def __add__(self, other) -> int:
        return self.value + other.value
    
    def __ne__(self, o) -> bool:
        return not self == o
    
    def __str__(self) -> str:
        return "Name: " + self.name + \
               " Side: " + str(self.side) + \
               " Value: " + str(self.value) + \
               " State: " + str(self.state) + \
               " Position: " + str(self.position) + \
               " Description"
    
    '''takes in a string line and build the Challenge from it'''

# #not usr eif gonna use these, using pickle more likely
# def parse_line(line: str) -> Challenge:
#     args = line.split("---")
#     return Challenge(args[0], Side(args[1]), int(args[2]), State(args[3]), (int(args[4]), int(args[5])), args[6])
#
#
# def save_line(chal: Challenge) -> str:
#     line = ""
#     sep = "---"
#     line += chal.name + sep + str(chal.side) + sep + str(chal.value) + sep + str(chal.state) + sep + \
#             str(chal.position[0]) + sep + str(chal.position[1]) + sep + chal.description
#     return line
