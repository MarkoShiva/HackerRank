# You are given the integer N and array with 1 and 0 you should find the smalest amount of hops from starting 0 to last 0
# considered that can move 2 or 1 places in a row and cannot get into position of num 1.

n = int(input())
arr = "".join(input().split(" "))
def clouds(arr):
    hops = 0
    # arr = "Hello World"
    while arr:
        try:
            if arr[2] == "0":
                hops += 1
                arr = arr[2:]           # pretty much the same as previous only here done with a string slicing
            elif arr[1] == "0":
                hops += 1
                arr = arr[1:]
        except IndexError:
            if len(arr) > 1:
                if arr[1] == "0":       # We need to check here again for arr[1]
                    hops += 1
                    arr = arr[1:]
                    continue
            else:
                break
    return hops

print(clouds(arr))