a = [3, 10, -11]

a.append(1)
print(a)
a.append("hello")
a.append([5, 6, 9])
print(a)
a.pop()
print(a)
print(a[0])
print(a[+1])

b = ["banana", "oranges", "apples"]

# swap
# b[0], b[2] = b[2], b[0]
b[0] = b[2]
b[2] = b[0]
print(b)
