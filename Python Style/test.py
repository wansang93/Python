import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer)
print(max(answer))


my_str = 'dfdefdgf'

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def top_counts(count_dict):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    answer = ''
    temp = 0
    for i, j in value_key_pairs:
        if i > temp:
            temp = i
            answer += j
        elif i == temp:
            answer += j
    answer = ''.join(sorted(list(answer)))
    return answer

print(top_counts(get_counts(my_str)))