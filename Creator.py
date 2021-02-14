from Challenge import *
import pickle
#Tome 1 default generation
#level 1
level1 = open("Data\Baseline\Tome1\level1", 'wb')
challenges = []
challenges.append( Challenge("Test", tome = 1, level = 1, side = Side.KILLER, value = 2500, state = State.INCOMPLETE,
                  position = (200, 100), description = "kill 5 survivors 11 times"))
challenges.append(Challenge("Fire", tome = 1, level = 1, side = Side.SURVIVOR, value = 60000, state = State.COMPLETE,
                  position = (200, 200), description = "live once"))

for c in challenges:
    pickle.dump(c, level1)
level1.close()
'''
plan for this file
write to the defaults files(probably not needed)
copy from defaults file to save file
    this could be doable with a button as well, or two, or three
probably dont actually need this one in full release

'''

