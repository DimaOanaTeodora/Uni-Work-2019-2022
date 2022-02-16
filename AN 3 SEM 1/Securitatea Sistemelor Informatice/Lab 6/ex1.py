# seed = (input("introduceti seed "))
seed = 0b100000

# C1
# print("C1")
# try:
#     while True:
#         print(seed)
#         seed = seed ^ seed
# except KeyboardInterrupt:
#     pass

# C2
print("C2")
try:
    while seed != 0:
        print(seed)
        seed = seed >> 2
except KeyboardInterrupt:
    pass

# C3
# print("C3")
# print(seed >> 2)