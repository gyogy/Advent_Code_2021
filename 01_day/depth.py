with open('../inputs/01', 'r') as f:
    raw_string = f.read()

str_values = raw_string.split('\n')

for i in range(str_values.count('')):
    str_values.remove('')

values = list(map(int, str_values))

sums = []
for i in range(len(values)-2):
    sums.append(sum(values[i:i+3]))

count_of_increased_values = sum(a < b for a, b in zip(values[:-1], values[1:]))
count_of_increased_sums = sum(a < b for a, b in zip(sums[:-1], sums[1:]))
print(count_of_increased_sums)
