from Challenge import *
import pickle

level1 = open("Data\Baseline\Tome1\level1", 'wb')
chal1 = Challenge("Test", tome = 1, level = 1, side = Side.KILLER, value = 2500, state = State.INCOMPLETE,
                  position = (200, 100), description = "kill 5 survivors 11 times")
chal2 = Challenge("Fire", tome = 1, level = 1, side = Side.SURVIVOR, value = 60000, state = State.COMPLETE,
                  position = (200, 200), description = "live once")
print(chal1)
print(chal2)
pickle.dump(chal1, level1)
pickle.dump(chal2, level1)
level1.close()
level1 = open("Data\Baseline\Tome1\level1", 'rb')
unpickled1 = pickle.load(level1)
unpickled2 = pickle.load(level1)
level1.close()
print(unpickled1)
print(unpickled2)
