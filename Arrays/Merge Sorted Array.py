nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3

length_ = len(nums2)
nums1 = nums1[:-length_] + nums2
nums1.sort()

# nums1 = nums1[0:m]+nums2[0:n]
# nums1.sort()

# nums1[m:] = nums2
# nums1.sort()
print(nums1)
