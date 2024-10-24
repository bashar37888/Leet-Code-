nums = [1, 2, 3, 4]
print(nums)
Target = int(input("Target:"))


for i in range(len(nums)):
  for k in range(i, len(nums)):
    if i == k:
      continue
      
    if nums[i] + nums[k] == Target:
      print([i, k])
      break
