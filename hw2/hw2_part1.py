import math
def volume_prism(length, width,height):
    volume=length*width*height*70*30*3
    return volume
length=float(raw_input("Length of rectangular prism (m) ==> "))
print length
width=float(raw_input("Width of rectangular prism (m) ==> "))
print width
height=float(raw_input("Height of rectangular prism (m) ==> "))
print height
print "Water needed for (%.1fm,%.1fm,%.1fm)"%(length,width,height), "locks is", str(volume_prism(length,width,height))+"m^3."
radius=float(raw_input("Radius of cylinder (m) ==> "))
print int(radius)    
volume= volume_prism(length,width,height)
def find_length(radius, volume):
    depth=volume/(math.pi* radius**2)
    return depth 
print "Lake with radius %.1fm will lose %.1fm depth in three months."%(radius, find_length(radius,volume))