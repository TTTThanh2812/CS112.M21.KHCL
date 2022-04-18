# Import các thư viện cần thiết
import math as m
import numpy as np
import collections as clt

# Khởi tạo ngẫu nhiên kích thước mảng và các phần tử trong mảng.
sizeOfArray = np.random.randint(1, 10 ** 5 + 1)
array = np.random.randint(1, 10 ** 5 + 1, sizeOfArray)

# Chuyển đồi mảng đã tạo thành chuỗi để đúng định dạng input.
strArray = ''
for number in array:
    strArray += str(number)
    strArray += ' '

# Dùng hàm Counter để đếm số lần xuất hiện của từng phần tử trong list.
appear = clt.Counter(array)

# Xét mỗi phần tử, số cặp bằng nhau của 1 số sẽ là tổ hợp chập 2 của số lần xuất hiện của phần tử đó.
count = 0
for key in appear:
    count += m.comb(appear[key], 2)

print('Input:')
print(sizeOfArray)
print(strArray[:-1])

print('Output:')
print(count)
