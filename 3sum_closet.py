def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            
            if abs(target - cur_sum) < abs(target - closest_sum):
                closest_sum = cur_sum
            
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return cur_sum
    
    return closest_sum
