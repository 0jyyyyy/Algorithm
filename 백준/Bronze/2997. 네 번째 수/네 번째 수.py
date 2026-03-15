nums = sorted(list(map(int, input().split()))) 

n1 = nums[1] - nums[0]
n2 = nums[2] - nums[1]

if n1 == n2 :
  print(nums[2] + n1)

elif n1 > n2 :
  print(nums[0] + n2)

else:
  print(nums[1] + n1)