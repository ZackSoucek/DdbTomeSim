from Challenge import *
import pickle

level1 = open("Data\Baseline\Tome1\level1", 'wb')
chal1 = Challenge("Test", tome = 1, level = 1, side = Side.KILLER, value = 2500, state = State.INCOMPLETE,
                  position = (200, 100), description = "kill 5 survivors 11 times")
print(chal1)
pickle.dump(chal1, level1)
level1.close()
level1 = open("Data\Baseline\Tome1\level1", 'rb')
unpickled = pickle.load(level1)
level1.close()
print(unpickled)
