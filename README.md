# Python-Vacuum-Cleaner

The program aims to simulate a robotic vacuum cleaner (omnidirectional service robot). This robot cleans the floor in a given area. Programming will be incremental, starting with a simple project, increasing the difficulty.
The program must use the graphics library provided by authors of the book: Python Programming: An Introduction to Computer Science, 3rd Ed., John M. Zelle, Franklin, Beedle & Associates, 2017.
The various implementations are called in a starting menu and where the program can be closed too. In the end of each implementation the program always return to the menu.

### Implementations

In any of the implementations the robot avoids obstacles and never get's out of the window.

#### First Implementation:

The user can click anywhere in the graphic environment where the dirt must be removed. The robot leaves the dockstation and goes to that point to clean it. 
Cleaning should cover about twice the area of the robot, with the point being clicked in the center of the area to be cleaned. After the cleaning process the point disappears;

#### Second Implementation:

The robot cleans the entire room in a back and forth motion. At the end the user defines some dirt points (given by mouse clicks). As in the first implementation, cleaning at these points should cover about twice the area of ​​the robot.
The robot has a battery that must be charged after traveling twice the area of ​​the room. It will pause the service to return to the docstation and charge the battery (the battery is super-fast charging, taking the same 2 seconds). 
There is a current charge indicator light that changes color when charging, when the battery is running out and when the battery is full.

#### Third Implementation:

In the final implementation, the configuration of obstacles in the room is done in two ways:
* Read from a file;
* Generated randomly by the program (sparse number of objects).

The choice of one or the other form is made in a graphic menu. In case of reading data from a file, the robot reads the size of the simulation window from the Ambiente.txt file, followed by the entries that define the location of the furniture in the room. 
The location of the docstation is also defined by the program.

In the case of random generation, the docstation is pre-defined by the program. The random generator defines the location of furniture, where positions and shapes will be random, but ensuring that there is no overlap and there is room for the robot to pass.
The most dirty points should be introduced in this implementation in two ways:
* Data by a file;
* Data through mouse clicks;

The choice between these two types of orders will be made through a graphic menu.

## Authors

* **Pedro Henrique Santos Sousa**
