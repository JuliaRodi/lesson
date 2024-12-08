from itertools import combinations

def all_variants(text):
    for i in range(1, len(text) + 1):
        list_1 = []
        b = combinations(text, i)
        list_1.extend(b)
        for j in list_1:
            j = list(j)
            yield (''.join(j))

a = all_variants("abc")

for i in a:
    if i == 'ac':
        continue
    print(i)