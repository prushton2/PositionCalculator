# Position Calculator
This python script provides documented math to determine the position of an object given it's distance to 4 properly placed points "beacons"

## Beacon Placement

The beacon placement is defined in this code:
```python
#beacon positions
position = [
    [0,10,0],
    [5,0,0],
    [-5,0,0],
    [-1,0,1]
]
```
Each subarray is the coordinates of each beacon. To place the beacons, 3 beacons must be coplanar and noncolinear. The 4th beacon must be noncolinear to the first 2 beacons, and noncoplanar to the third.

An example as follows, where the number is the z position
```
0    0

0   -1
```