# Code04-10 과제 Sort 들

def bubble_sort(data):
    new_data = data[:]
    for i in range(len(new_data)-1):
        for j in range(len(new_data)-i-1):
            if new_data[j] > new_data[j+1]:
                new_data[j], new_data[j+1] = new_data[j+1], new_data[j]
    return new_data


def select_sort(data):
    new_data = data[:]
    for i in range(len(new_data)-1):
        min_idx = i
        for j in range(i, len(new_data)):
            if new_data[min_idx] > new_data[j]:
                min_idx = j
        new_data[i], new_data[min_idx] = new_data[min_idx], new_data[i]
    return new_data



def quick_sort(data):
    new_data = data[:]
    if len(new_data) <= 1:
        return new_data
    
    pivot = new_data[len(new_data)//2]
    left_data, middle_data, right_data = [], [], []
    for i in new_data:
        if i < pivot:
            left_data.append(i)
        elif i > pivot:
            right_data.append(i)
        else:
            middle_data.append(i)
    
    return quick_sort(left_data) + middle_data + quick_sort(right_data)

import random

data = [0] * 10
for i in range(10):
    data[i] = random.randrange(100000)

print([i[2:] for i in map(hex, data)])
print([i[2:] for i in map(hex, select_sort(data))])
print([i[2:] for i in map(hex, bubble_sort(data))])
print([i[2:] for i in map(hex, quick_sort(data))])
print([i[2:] for i in map(hex, data)])
