from matrix import Matrix

# liste = ([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
# print(type(liste))
# print("------")
# data = []
# num_list= 3
# num_elem= 4
# for i in range (num_list):
# 	col = []
# 	for j in range (num_elem):
# 		col.append(0.0)
# 	data.append(col)
# print(data)
# print("------")
# for i in liste:
# 	print(type(i))
# print(len(liste))
# print("------")
# print(len(liste[0]))
# print("------")
# tutu = ()
# tutu = (0, 1, 45)
# print(type(tutu))
# print(len(tutu))
# print(tutu[2])
# print("------")
# lolo = [[]]
# print(type(lolo))
# print(len(lolo))

print("1st initialization")
m1 = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0], [9.0, 10.0, 11.0]])
print(m1.shape)
print(m1.data)
print("------")
print("2nd initialization")
m2 = Matrix((2, 4))
print(m2.shape)
print(m2.data)
print("------")
print("3d initialization")
m3 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]], (3, 2))
print(m3.shape)
print(m3.data)
print("------")
m4 = Matrix((1, 3),(2, 5))

