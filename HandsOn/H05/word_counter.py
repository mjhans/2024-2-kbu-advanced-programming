from collections import Counter

file_name = "Lorem.txt"

#count_dict = {}
count_dict = Counter()

with open(file_name, "r") as fp:
    for line in fp:
        words = line.split(" ")
        count_dict.update(words)
        
        
# with open(file_name, "r") as fp:
#     for line in fp:
#         words = line.split(" ")
#         for word in words:
#             if word in count_dict.keys():
#                 count_dict[word] += 1
#             else:
#                 count_dict[word] = 1


    