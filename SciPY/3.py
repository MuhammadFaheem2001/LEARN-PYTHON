# GRAPHS

# Graphs are an essential data structure.
# SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.


from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import dijkstra
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import breadth_first_order
import numpy as np

arr = np.array([
    [0,1,2],
    [1,0,2],
    [0,0,3]
])

var = csr_matrix(arr)
# print(connected_components(var))
# print(dijkstra(var, indices=0, return_predecessors=True))
# print(floyd_warshall(var, return_predecessors=True))
# print(bellman_ford(var, return_predecessors=True, indices=0))
print(breadth_first_order(var, 1))





# SPATIAL DATA


# Spatial data refers to data that is represented in a geometric space.
# E.g. points on a coordinate system.
# We deal with spatial data problems on many tasks.
# E.g. finding if a point is inside a boundary or not.
# SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.


import numpy as np # for arrays
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import matplotlib.pyplot as mt  # For ploting graph

arr1 = np.array([
    [1,2,3],
    [0,4,5],
    [6,0,7],
    [8,9,0],
    [3,0,0],
    [0,0,1]
])

var1 = Delaunay(arr1).simplices

mt.triplot(arr1[:, 0], arr1[:, 1],color="red")
mt.triplot(arr1[:, 0], arr1[:, 1],color="purple")

mt.show()




points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

mt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

mt.show()



from scipy.spatial import kdtree

points1 = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtre = kdtree(points)
res = kdtre.query((1, 1))

print(res)


