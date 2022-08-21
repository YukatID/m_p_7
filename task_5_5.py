A = np.array([1,5,0])
B = np.array([2,8,7])
C = np.array([7,1.5,3])
#1
D = np.array([A,B,C])
print("матрица D",D)
print("Определитель матрицы D:", np.linalg.det(D))
#2
m1 = np.cross(A,B)
print("Векторное произведение A и B:",m1)
print("Векторное произведение A и B, умноженное скалярно на C:",np.dot(m1,C))