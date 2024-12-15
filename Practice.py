import numpy as np
import pandas as pd

array1 = np.array([1,2,3,4,5])
array2 = np.array([1,2,3,4,5])

# rows, cols = array2.shape
# for i in range(rows):
#     for j in range(cols):
#         pass
#         # print(array2[i, j])

# data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(data)

# data2 = pd.Series([1, 2, 3, 4])
# print(data2)

# data4 = {
#     'Name' : ['Alice', 'Bob', 'Charlie'],
#     'Age' : [25, 30, 35],
#     'City': ['New York', 'San Francisco', 'Los Angeles']
# }

# df = pd.DataFrame(data4, index =['a', 'b', 'c'])
# print(df)

# filtered = df[df['Age']> 30]
# print(filtered)


# Merge two DataFrames
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Salary': [50000, 60000]})
merged = pd.merge(df1, df2, on='ID')
print(merged)
