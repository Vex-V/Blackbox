# Blackbox

[link to video](https://youtu.be/UXGwKEIs1ts)
<h2>INTRODUCTION</h2>

A python recreation of the 1970s boardgame by Eric Solomon, it is an abstract strategy game where players must shoot a ray into a black box and deduce the locations of atoms inside it based on deflections and exit squares, [Wikipedia link](https://en.wikipedia.org/wiki/Black_Box_(game)). 
<br>
The game utilizes Pygame to render all graphics, and a recursive function is implemented to move the ray around the box, calculating its path and any deflections
<br>
The number of atoms consecutively increase every round and the player must finish 5 rounds to win, the player loses if the exceed the total number of allowed guesses for that round
<br>

<h2>REQUIREMENTS</h2>

- PYTHON 3.X
- PYGAME

install with 
```
pip install pygame
```

<h2>WORKING</h2>
The Player must click on an exterior square from where the ray is shot in, the clicked on square turns green to indicate so, the player can do this an indefinite number of times
if the player hits a corner of an atom, the ray is deflected based on the angle at which it hits,

- if a ray moving rightwards hits an upper corner it is deflected upwards, and downwards if it hits a lower corner
- if a ray moving leftwards hits an upper corner it is deflected upwards, and downwards if it hits a lower corner
- if a ray moving upwardswards hits a right corner it is deflected rightwards, and leftwards if it hits a left corner
- if a ray moving downwardswards hits a right corner it is deflected rightwards, and leftwards if it hits a left corner

after this, 3 possibilites can occur,

- Another exterior square turns green, this means the ray exited here, either directly or after a deflection
- The clicked on square turns dark green, this means the ray exited on the entry square initially clicked on 
- No exit square occurs, this means the ray directly hit an atom and not any of its edges

A "How to Play" Button contains all neccesary information that a new player would need 
<br>
There are also in-built button to let a user try to play the game again should they lose, resetting the game entirely
<br>
A quit button provides an easy way to directly quit
<br>
Thanks to [Himashree](https://github.com/hperumalla-oops) For QA testing and feedback.
