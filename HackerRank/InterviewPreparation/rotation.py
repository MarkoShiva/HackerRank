n, rot = (int(v) for v in input().rstrip().split(" "))

arr = [int(v) for v in input().split(" ")]


for v in range(rot):
    arr.append(arr.pop(0))    # left rotation is achieved by removing the first element and appending it to the end.

res = " ".join(str(v) for v in arr)     # reformatting the array as a string space separated
print(res)