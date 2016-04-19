# rover
Python Code and other info for a 4 wheeled robot controlled by a Raspberry Pi.

I'm new to robotics and Python, but not to computers and programming. I'm definitely learning a lot.

##Updates
__October 29, 2015__
- Rover now uses `move2.py` to move forward and backward 2 seconds using 4 wheels. An improvement over `move.py`
which is monolithic, move2.py includes functions `moveForward(intTime)` and `moveBackward(intTime)` to move the rover for a period of seconds. My first Python functions!

__November 7, 2015__
- wrote `moveturn.py` to test turning
- purchased a Mental Beats battery back for untethered greatness!
- seems not to have enough power to turn
- added `turnLeft(intTime)` but it is actually a right turn. Will fix it later.
- Pin 7 controls left motors in forward direction
- Pin 11 - Left motors in backward direction
- Pin 15 - Right side motors forward
- Pin 13 - right side motors backwards

__April 18, 2016__
* Fixed left/right turn function names
* Turns appear underpowered on carpet, but probably need to by a Pi Servo Hat as the Raspberry Pi is known to have inaccurate PWM signals.
* Created `rover.py` as a module to store movement functions.
* Wrote `backforth.py` to use command line argument for number of repetitions and it imports `rover.py`
* `square2.py` moves the rover in a square where the robot travels 2 seconds in each direction. Slight problem with turns but may be fixed with Pi Servo Hat.

