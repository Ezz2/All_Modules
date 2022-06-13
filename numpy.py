By Ezz

import numpy as np
# print(np.__version__) If I Neeed The Version I Use

# array()
print("\n_________array()_________\n")

a = np.array([1, 2, 3], dtype=int) # One Dimentinal
print(a) # Type: Numpy.ndarray

print("-" * 10)

b = np.array([[4, 5, 6], [7, 8, 9]], dtype=int) # Two Dimentinal, I Can Add More Dimentions
print(b)

# arange()
print("\n_________arange()_________\n")

arr = np.arange(5)
print(arr)

arr = np.arange(0, 11, 2)
print(arr)

# zeros()
print("\n_________zeros()_________\n")

arr = np.zeros((3, 4), dtype=int)
print(arr)

# ones()
print("\n________ones()_________\n")

arr = np.ones((3, 4), dtype=int)
print(arr)

# linspace()
print("\n_________linspace()_________\n")

arr = np.linspace(1, 2, 5, dtype=float)
print(arr)

# random.randint(), rand(), shuffle()
print("\n_________random.randint(), rand(), shuffle()_________\n")

arr = np.random.randint(1, 10, 2) # 2 Means Two Random Numbers
print(arr)

arr = np.random.randint(100, 200, (3, 2)) # Get It With Matrix
print(arr)

arr = np.random.rand(3, 3) # Rand Means: 3 * 3 Random Decimal Number
print(arr)

numbers = np.arange(10)
np.random.shuffle(numbers) # Shuffle Means Unarrange Array
print(numbers)

print("-" * 10)

l = np.random.randint(1, 50, (30, 5))
l2 = enumerate(l, 1)

for m in l2:
   print(*m)


# Inspecting Numpy Arrays, Inspecting: يتفقد
print("\n_________Inspecting Numpy Arrays_________")

# Shape
print("_________.Shape_________\n")

print(b.shape)

sha = np.random.randint(1, 20, (3, 4))
print(sha)

shape = sha.shape[0] # To Get How Many Row, Column In Matrix | row[0], column[1]
print(shape)

# len()
print("\n_________len()_________\n")

print(len(a))

# ndim
print("\n_________.ndim_________\n")

print(a.ndim) # To Get How Many Dimention In Array

# size
print("\n_________.size_________\n")

print(b.size) # How many Numbers In Array

# dtype
print("\n_________.dtype_________\n")

print(a.dtype.name) # To Know What Data Type In This Array

print("\n_________.astype_________\n")

print(a.astype(int))


# Manipluting Numpy Array, Manipluting: تلاعب
print("\n_________Manipluting Numpy Array_________")

# insert()
print("_________insert()_________\n")

print(np.insert(b, 1, 5))
print(b)

# delete()
print("\n_________delete()_________\n")

print(np.delete(b, 1))
print(b)

# reshape()
print("\n_________reshape()_________\n")

print(b.reshape(3, 2)) # Original 2, 3
print(b)

xx = np.random.randint(100, 200, 10)
xx2 = xx.reshape(10, 1)
print(xx2)

# append()
print("\n_________append()_________\n")

print(np.append(a, b))


# Subsetting, Slicing, Indexing
print("\n_________Subsetting, Slicing, Indexing_________")

# Indexing In Array
print("_________Indexing In Array_________\n")

print(a[1])
print(b[1, 2])

# Slicing In Array
print("\n_________Slicing In Array_________\n")

print(a[0:3])
print(b[1, 0:3]) # In Dimention Two And Get [7 8 9]
print(b[:, 0:3]) # Get One And Two Dimentions [4 5 6 7 8 9]
print(a[a < 3])  # To Get The Numbers Less Than 3


# Numpy Array Mathematics & Arthmetic Operations
print("\n____Numpy Array Mathematics & Arthmetic Operations____")

# add()
print("_________.add()_________\n".center(35, "_"), '\n')

# print(a + b)
print(np.add(a, b))

add_matrix = np.array([[1, 2, 3, 4], [2, 4, 5, 6]])
print(np.add(add_matrix, 2))

# subtract()
print("\n_________.subtract()_________\n")

# print(a - b)
print(np.subtract(a, b))

subtract_matrix = np.array([[1, 2, 3, 4], [2, 4, 5, 6]])
print(np.subtract(subtract_matrix, 2))

# multiply()
print("\n_________.multiply()_________\n")

# print(a * b)
print(np.multiply(a, b))

multiply_matrix = np.array([[1, 2, 3, 4], [2, 4, 5, 6]])
print(np.multiply(multiply_matrix, 2))

# divide()
print("\n_________.divide()_________\n")

# print(a / b)
print(np.divide(a, b))

divide_matrix = np.array([[1, 2, 3, 4], [2, 4, 5, 6]])
print(np.divide(divide_matrix, 2))

# sqrt()
print("\n_________.sqrt()_________\n")

print(np.sqrt(a))

# .ceil(), .floor(), .round()
print("\n_________.ceil(), .floor(), .round()_________\n")

c = np.ceil(3.2)
print(c)

f = np.floor(3.2)
print(f)

r1 = np.round(3.4)
r2 = np.round(3.5)
r3 = np.round(3.6)

print(r1)
print(r2)
print(r3)

# sin(), cos(), tan(), log()
print("\n_________.sin(), .cos(), .tan(), .log()_________\n")

print(np.sin(a))
print(np.log(a))


# Numpy Statistical Operations
print("\n_________Numpy Statistical Operations_________")

# sum()
print("_________.sum()_________\n")

print(b.sum()) # np.sum()

# max(), min(), argmax(),argmin()
print("\n_________.min(), .max(), .argmax(), .argmin()_________\n")

print(a.min())  # np.min(a)
print(b.max()) # np.max(b)

num = np.random.randint(1, 21, (5, 5))
print(num)

max_index = num.argmax()
min_index = num.argmin()

print(f"Maximun Number Is: {str(max_index)}")
print(f"Minimum Number Is: {str(min_index)}")

# median, mean, std
print("\n_________median, mean, std_________\n")

print(np.median(a)) # a.median()
print(np.mean(b))   # b.mean()
print(np.std(b))    # b.std()


# Functions I Get It Alone
print("\n_________Functions I Get It Alone_________")

# .mat()
print("_________.mat()_________\n")

mat = np.array(np.mat('1 2; 3 4'), subok = True)
print(mat)

# arange() & reshape()
print("\n_________arange() & reshape()_________\n")

ar_re = np.arange(12).reshape(4, 3)
ar_re2= np.arange(24).reshape(2, 3, 4)

print(ar_re)
print(ar_re2)
