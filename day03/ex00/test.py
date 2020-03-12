from NumPyCreator import NumPyCreator

npc = NumPyCreator()

t = npc.from_list([[1, 2, 3], [6, 3, 4]])
print(t)
# array([[1, 2, 3],
#    [6, 3, 4]])

t = npc.from_tuple(("a", "b", "c"))
print(t)
# array(['a', 'b', 'c'])

t = npc.from_iterable(range(5))
print(t)
# # array([0, 1, 2, 3, 4])

shape = (3, 5)
t = npc.from_shape(shape)
print(t)
# # array([[0, 0, 0, 0, 0],
# #    [0, 0, 0, 0, 0],
# #    [0, 0, 0, 0, 0]])

t = npc.random(shape)
print(t)
# # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768],
# #    [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# #    [0.79585328, 0.00660962, 0.92910958, 0.9905421, 0.05244791]])

t = npc.identity(4)
print(t)
# # array([[1., 0., 0., 0.],
# #    [0., 1., 0., 0.],
# #    [0., 0., 1., 0.],
# #    [0., 0., 0., 1.]])
