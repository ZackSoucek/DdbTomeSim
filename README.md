# DdbTomeSim
Tome simulator for dead by daylight
The plan is to copy the tome pictures, and add buttons over them,
Looking for hover descriptions, and multiple options for:
    Incomplete
    Unclaimed
    Claimed
    Unreachable(maybe(extra maybe pathfind))

use a UI library, some built in buttons
hopefully with hover definitions
each button object should have
    Side:killer, survivor, either
    value
    neighbors
    description
    state
    position
write to a file for saving data probably using pickle module
each button is a line probably


for use in pathfind
    traveling salesman
    minnimum spannign tree
    topological sort
    floyds algorithm
    