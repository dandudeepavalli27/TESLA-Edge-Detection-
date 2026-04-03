# TESLA-Edge-Detection-

Aim
To compute the edge strength using gradient magnitude in image processing.
General Objective
To study edge detection as a key technique in computer vision and understand how gradient-based methods identify object boundaries in images for autonomous systems.
Specific Objective
To compute edge strength using:
∣
∇
∣
=
G
x
2
+
G
y
2
∣∇∣= 
G 
x
2
​	
 +G 
y
2
​	
 
​	
 
Given:
G
x
=
5
G 
x
​	
 =5
G
y
=
12
G 
y
​	
 =12
Dataset
Berkeley Edge Dataset
Source: UC Berkeley
Procedure
Input gradient values 
G
x
G 
x
​	
  and 
G
y
G 
y
​	
 
Square both values
Add the squares
Take square root
Display edge strength
Algorithm
Start
Input 
Compute 
Take square root
Display result
Stop
Code Logic
edge = (Gx**2 + Gy**2) ** 0.5
Output
Edge Strength = 13

Program Executed Successfully
Result
The computed edge strength is:
Edge Strength = 13
Industry Application
Edge detection is used in:
Autonomous driving
Object detection
Lane detection
Image segmentation
Companies like Tesla, Inc. use this in:
Self-driving cars
Computer vision systems
Real-time perception
Conclusion
Gradient-based edge detection helps identify object boundaries effectively, making it essential for computer vision and autonomous navigation systems.
