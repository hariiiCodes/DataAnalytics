import numpy as np
print(np. __version__)
# arr=np.array([[1,2,4,5],[3,7,8,9]])
# print(arr)
# print(type(arr))

# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.dtype)

# a=np.ones((2,3))
# print(a)
# d=np.arange(0,10,2)
# print(d)
# s=np.linspace(0,1,5)
# print(s)
# e=np.eye(3)
# print(e)
# f=np.random.randint(1,10,(2,3))
# print(f)

# print(arr[1])

# r=np.array([[1,2,3],[4,5,6]])
# print(r[1,2])
# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x[0,:])
# print(x[:,0])
# print(arr[arr>1])
# print(arr[[0,2,3]])

# v=np.array([[10,20,30,40],[1,2,3,4]])
# # print(arr+v)
# # print(arr-v)
# # print(arr*v)
# # print(arr/v)
# print(np.sum(v))
# print(np.mean(v))
# print(np.median(v))
# print(np.std(v))
# print(np.var(v))
# print(np.min(v))
# print(np.max(v))
# print(np.argmin(v))
# print(np.argmax(v))

# new_v=v.reshape(3,2)
# print(v)
# print(v.flatten())
# print(v.ravel())
# print(v.transpose())

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# res=np.matmul(a,b)
# print(res)


# print(np.dot(a,b))
# A=np.array([[1,2],[3,4]])
# print(np.linalg.inv(A))

print(np.random.rand(3))

data=[10,20,30,40,50]
print(np.random.choice(data,3))

print(np.random.normal(loc=0,scale=1,size=5))
rng1=np.random.default_rng(seed=5)
print(rng1.random())