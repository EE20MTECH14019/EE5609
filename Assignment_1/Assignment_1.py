#Assignment_1
#In what ratio is the line joining (x1,y1) and (x2,y2) divided by the line (xcoeff ycoeff) X = Constant


import numpy as np
import math
from fractions import Fraction

#Taking inputs for two points and line
print("Give points (x1,y1) and (x2,y2)")
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
print("Enter x_coeff , y_coeff and constant of given line")
line2_xcoeff=int(input("Enter x_coeff: "))
line2_ycoeff=int(input("Enter y_coeff: "))
line2_const=int(input("Enter constant: "))

#lst1 has the coefficients of the line equation joining given two points
lst1=[-(y2-y1),x2-x1,(x2-x1)*y1-(y2-y1)*x1]
lst2=[line2_xcoeff,line2_ycoeff,line2_const]
#print(lst1)
#print(lst2)

#Solving the two equations using matrix inversion method A=XC => X=Ainv*C
A=np.array([[lst1[0],lst1[1]],[lst2[0],lst2[1]]])
#print(A)

#Finding the inverse of matrix A
Ainv=np.linalg.inv(A)
#print(Ainv)
##print(Ainv.dot(A))

#C Matrix
C=np.array([[lst1[2]],[lst2[2]]])
#print(C)

# Calculating X=Ainv*C
X=np.matmul(Ainv,C)
#print(X)

## Finding the RATIO

#distance d1 from pt A1(x1,y1) and intersection pt X

A1=np.array([x1,y1])
d1=math.sqrt((X[0]-A1[0])**2+(X[1]-A1[1])**2)
#print(d1)

#distance d1 from pt A2(x2,y2) and intersection pt X

A2=np.array([x2,y2])
d2=math.sqrt((X[0]-A2[0])**2+(X[1]-A2[1])**2)
#print(d2)

#Printing the final Ratio
ratio=Fraction(d1/d2)
print(ratio)


