# Exercise_4
# ________________________________________________________________

import os
from compas.datastructures import Mesh
from random import choice
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

# get mesh
mesh = Mesh.from_obj(FILE)

# select only vertices on boundaries with degree = 3
vertices = []
vlist = mesh.vertices_on_boundary()
bou = []
for v in vlist:
    dg = mesh.vertex_degree(v)
    if dg == 3:
        bou.append(v)

# pick randomly one boundary vertex with degree = 3
start = choice(bou)
vertices = [start]
nbrs = mesh.vertex_neighbors(start)

# find internal neighbor(or degree=4)
current = start
for nbr in nbrs:
    if not mesh.is_vertex_on_boundary(nbr):
        previous, current = current, nbr
        break

# find next point following the cycle
while True:
    vertices.append(current)
    if mesh.is_vertex_on_boundary(current):
        break
    nbrs = mesh.vertex_neighbors(current, ordered=True)
    i = nbrs.index(previous)
    previous, current = current, nbrs[i - 2]

print(vertices)

plotter = MeshPlotter(mesh)
plotter.draw_vertices(radius=0.2, text='key', keys=vertices, facecolor=(255, 0, 0))
plotter.draw_faces()
plotter.draw_edges()
plotter.show()