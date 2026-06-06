from collections import defaultdict


n, k, m = map(int, input().split())
gems = []
best_by_color = {}

for _ in range(n):
    color, value = map(int, input().split())
    gems.append((value, color))
    if color not in best_by_color or best_by_color[color] < value:
        best_by_color[color] = value

gems.sort(reverse=True)
selected = gems[:k]
selected_sum = sum(value for value, _ in selected)

selected_count = defaultdict(int)
selected_values = defaultdict(list)
for value, color in selected:
    selected_count[color] += 1
    selected_values[color].append(value)

distinct = len(selected_count)
if distinct >= m:
    print(selected_sum)
    exit()

need = m - distinct

removable = []
for color, values in selected_values.items():
    if len(values) >= 2:
        values.sort()
        removable.extend(values[: len(values) - 1])

addable = []
for color, value in best_by_color.items():
    if color not in selected_count:
        addable.append(value)

removable.sort()
addable.sort(reverse=True)

answer = selected_sum - sum(removable[:need]) + sum(addable[:need])
print(answer)

