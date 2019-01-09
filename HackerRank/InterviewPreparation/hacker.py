
# Complete the sockMerchant function below.
def sockMerchant(n, ar):            # this tasks can be done differently with itterators and tuples
                                    # I am doing here a bit harder to track array version
    p = 0
    while ar:                       # while still there is something in array
        v = ar[0]                   # we declare v to first item in array
        try:
            ar.pop(ar.index(v))     # we pop up the first value of v which is current first
            ar.pop(ar.index(v))     # if there is another one value like that its a matching par and we poped it out
            p += 1                  # if removing element didnt raise an exception we increment the p
        except (IndexError, ValueError):
            continue                # we just keep going here in a loop as long as there is something in array

    return p                        # finally we return value

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

