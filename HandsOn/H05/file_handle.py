
# f = open("test", "w")
# for i in range(10):
#     f.write(f"Hello, Python {i}\n")
# f.close()

# f = open("test", "r")

# for line in f:  # != f.readline()
#     print(line)
# f.close()

# # result = f.read()
# # print(f"{result = }")
# f.close()


f = open("/Users/mjhans/workspaces/personal/python_class/2024-2-kbu-advanced-programming/HandsOn/H05/test", "r+")
f.write("everyone, hi")
data = f.read()
print(data)

f.close()
