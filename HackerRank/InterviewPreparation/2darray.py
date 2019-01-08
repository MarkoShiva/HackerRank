# You are given a square of matrix values and the result should be the hourglass that contain largest sum
# matrix values are in range from -9 to 9
arr = [[int(v) for v in input().split(" ")] for _ in range(6)]  # input is given as a 2dMatrix and it is processed as
                                                                # array of arryays
var = 6                         # just a placeholder in case I want a larger square matrix

ret = -99999                    # value need to be set under the 7 * -9 = -63
for n in range(var - 2):
    for p in range(var - 2):
        # sum of the hourglass
        sums = arr[n][p] + arr[n][p+1] + arr[n][p+2] + arr[n+1][p+1] + arr[n+2][p] + arr[n+2][p+1] + arr[n+2][p+2]
        if sums > ret:
            ret = sums

print(ret)