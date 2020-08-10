class elements:
    def sums(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

print("index1=%d, index2=%d" % elements().sums((10, 20, 10, 40, 50, 60, 70), 50))