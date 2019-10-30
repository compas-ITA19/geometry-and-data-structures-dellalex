# Exercise_1
# ________________________________________________________________

from compas.geometry import cross_vectors
from compas.geometry import normalize_vector

def orthonormal_vectors(vector_a, vector_b):
    a = normalize_vector(vector_a)
    b = normalize_vector(cross_vectors(vector_a,vector_b))
    c = normalize_vector(cross_vectors(b,vector_a))
    return a,b,c

# vectors
vector_a = [3.0, 4.0, 2.0]
vector_b = [1.0, 2.0, 6.0]

a, b, c = orthonormal_vectors(vector_a, vector_b)

print (a,b,c)