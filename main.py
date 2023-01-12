import math

#This is built to calculate position based on the distance to 4 known positions

#beacon positions
position = [
    [0,10,0],
    [5,0,0],
    [-5,0,0],
    [-1,0,1]
]
#destination point
destination = [6,8,0]

#givens (distances to each beacon) (no i dont care enough or want to learn about .map or whatever it is in python)
distances = [
    math.sqrt((abs(position[0][0] - destination[0]))**2 + (abs(position[0][1] - destination[1]))**2 + (abs(position[0][2] - destination[2]))**2),
    math.sqrt((abs(position[1][0] - destination[0]))**2 + (abs(position[1][1] - destination[1]))**2 + (abs(position[1][2] - destination[2]))**2),
    math.sqrt((abs(position[2][0] - destination[0]))**2 + (abs(position[2][1] - destination[1]))**2 + (abs(position[2][2] - destination[2]))**2),
    math.sqrt((abs(position[3][0] - destination[0]))**2 + (abs(position[3][1] - destination[1]))**2 + (abs(position[3][2] - destination[2]))**2)
]

print(distances)
print(distances[0]**2, distances[1]**2, distances[2]**2, distances[3]**2)

#ok so these alogrithms can be generated based on the given stuff. These are used for my personal reference

# x^2 + (y-10)^2 + z^2    = dist[0]**2 | 40;
# (x-5)^2 + y^2 + z^2     = dist[1]**2 | 65;
# (x+5)^2 + y^2 + z^2     = dist[2]**2 | 185;
# (x+1)^2 + y^2 + (z-1)^2 = dist[3]**2 | 114;

#heres the algorithms with variables

# (x-position[0][0])^2 + (y-position[0][1])^2 + (z-position[0][2])^2 = dist[0]**2;
# (x-position[1][0])^2 + (y-position[1][1])^2 + (z-position[1][2])^2 = dist[1]**2;
# (x-position[2][0])^2 + (y-position[2][1])^2 + (z-position[2][2])^2 = dist[2]**2;
# (x-position[3][0])^2 + (y-position[3][1])^2 + (z-position[3][2])^2 = dist[3]**2;

#so now we solve in place of z in the first algorithm and place it into z on the second algorithm

