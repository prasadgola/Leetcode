def twoSum(nums, target):
  hash = {}
  for i in range(len(nums)):
      if nums[i] in hash:
          return [hash[nums[i]],i]
      else:
          hash[target -  nums[i]] = i
  

print(twoSum([2,7,11,15],9))