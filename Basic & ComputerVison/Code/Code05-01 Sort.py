import random

data_list = [random.randint(1, 99) for _ in range(20)]  # 1부터 99까지
print(data_list)

# # Selection Sort
# for i in range(0, len(data_list)-1):
#     for j in range(i+1, len(data_list)):
#         if data_list[i] > data_list[j]:
#             data_list[i], data_list[j] = data_list[j], data_list[i]

# Bubble Sort
for i in range(len(data_list)-1):
    change = False
    for j in range(len(data_list)-i-1):
        if data_list[j] > data_list[j+1]:
            data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
            change = True
    if change == False:
        break

print(data_list)