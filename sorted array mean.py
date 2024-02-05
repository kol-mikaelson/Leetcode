nums1 = [1, 3]
nums2 = [2, 7]
# comment out the array declaration for leetcode

num = nums1 + nums2
num.sort()
sum = 0
if len(num) % 2 == 0:
    median = (num[int(len(num) / 2)] + num[int((len(num) / 2) - 1)]) / 2
else:
    median = num[len(num) / 2]
print(median)
