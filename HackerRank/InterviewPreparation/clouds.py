n = int(input())
arr = "".join(input().split(" "))
def clouds(arr):
    hops = 0
    # arr = "Hello World"
    while arr:
        try:
            if arr[2] == "0":
                hops += 1
                arr = arr[2:]
            elif arr[1] == "0":
                hops += 1
                arr = arr[1:]
        except IndexError:
            if len(arr) > 1:
                if arr[1] == "0":
                    hops += 1
                    arr = arr[1:]
                    continue
            else:
                break
    return hops

print(clouds(arr))