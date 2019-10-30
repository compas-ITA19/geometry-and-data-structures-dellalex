# Exercise_3
# ________________________________________________________________

from compas.geometry import cross_vectors
# input arrays
a1 = [[0.0,1.0,1.0],[1.0,1.0,0.0],[1.0,1.0,1.0],[0.0,0.0,1.0]]
a2 = [[2.0,1.0,1.0],[1.0,1.0,3.0],[2.0,0.0,1.0],[3.0,2.0,0.0]]

# pure_python
def cross_u_v(u,v):
    c = [u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]]
    return c

c_v = []
if len(a1)==len(a2):
    for i,n in enumerate(a1):
        c = cross_u_v(a1[i],a2[i])
        c_v.append(c)
    print ('a',c_v)
else:
    print ('arrays with different length')




# compas
vec = []
if len(a1)==len(a2):
    for i,l in zip(a1,a2):

        v = cross_vectors(i,l)
        vec.append(v)
    print ('b',vec)
else:
    print ('arrays with different length')





# numpy
import numpy
if len(a1)==len(a2):
    vect = numpy.cross(a1,a2)
    print ('c',vect)
else:
    print ('arrays with different length')