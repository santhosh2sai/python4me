def find_uniq(arr):
  i = sorted(arr)
  return i[len(i)-1]
print(find_uniq([1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3 ]))
