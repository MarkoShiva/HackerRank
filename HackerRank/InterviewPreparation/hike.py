# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly steps.
# For every step he took, he noted if it was an uphill, , or a downhill, step. Gary's hikes start and end at sea level and each step up or down represents a
# unit change in altitude. We define the following terms:
#
#    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
#    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

n = int(input())
arr = input()
v = level = 0
for x in arr:
    if x == "D":
        level -= 1
    elif x == "U":
        level += 1
    if level == 0 and x == "U":
        v += 1
print(v)
