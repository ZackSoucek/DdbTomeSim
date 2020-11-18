import Challenge
class Tome:
    def __init__(self, pages):
        self.levels = pages
class Page:
    def __init__(self, level, tome):
        self.level = level
        self.tome = tome
        self.challenges = []
    
    
