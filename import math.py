import math

print ("(x , y) coordinates for point P : ")
x1 = float(input()) ; y1 = float(input())
print ("(x , y) coordinates for point Q : ")
x2 = float(input()) ; y2 = float(input())

x_diff_sq = (x2 - x1)**2.0 ; y_diff_sq = (y2 - y1)**2.0

d = math.sqrt(x_diff_sq + y_diff_sq)
print ("distance between P and Q : ", format(d, "0.2f"))
# output: ?
