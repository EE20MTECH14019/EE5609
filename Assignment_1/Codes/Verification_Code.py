import numpy as np
import math
from fractions import Fraction

#points for plotting
A=np.array([-1,1])
B=np.array([5,7])
C=np.array([2,2])
D=np.array([3,1])


#verification

#finding the intersection of AB and CD lines

#finding the point X where CD intersects the line joining A and B
P = np.array([[-1, 1], [1, 1]])
Q = np.array([[2], [4]])
X=np.linalg.inv(P) @ Q

int_X = X.astype(int)
print("Point of Intersection: ",int_X)

#finding the distances AX and XB which in turn gives the ratio
AX=math.sqrt((X[0]-A[0])**2+(X[1]-A[1])**2) #Distance from point A to X
BX=math.sqrt((X[0]-B[0])**2+(X[1]-B[1])**2) #Distance from point B to X

ratio=Fraction(AX/BX)
print("Ratio Line AB divided by CD is: ",ratio)


