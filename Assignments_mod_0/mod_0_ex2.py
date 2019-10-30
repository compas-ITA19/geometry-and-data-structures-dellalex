# Exercise_2
# ________________________________________________________________

from compas.geometry import Polygon

def poly_area(polygon):
    # find polygon's centroid
    cen = polygon.centroid

    # create vectors between the centroid and each vertex of the polygon
    vectors = []
    for i in polygon:
        v = cen - i 
        vectors.append(v)
    # calculate cross product and magnitude between each couple of vectors
    length = []
    # cross product and magnitude between first and last vector
    L0 = vectors[-1].cross(vectors[0]).length
    length.append(L0)
    # cross product and magnitude between the other vectors    
    for i in range(0,len(vectors)-1):
        L = vectors[i].cross(vectors[i+1]).length
        length.append(L)
    # area
    area = (sum(length)/2)
    return area 



polygon = Polygon([[0,0,0], [6,0,0], [6,6,0], [0,6,0]])
area = poly_area(polygon)
print (area)