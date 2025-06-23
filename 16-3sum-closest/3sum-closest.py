class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            # Early pruning
            if nums[i] + nums[left] + nums[left + 1] > target:
                # sum too big even with smallest two numbers, break
                if abs(nums[i] + nums[left] + nums[left + 1] - target) < abs(closest_sum - target):
                    closest_sum = nums[i] + nums[left] + nums[left + 1]
                break

            if nums[i] + nums[right] + nums[right - 1] < target:
                # sum too small even with largest two numbers, continue
                if abs(nums[i] + nums[right] + nums[right - 1] - target) < abs(closest_sum - target):
                    closest_sum = nums[i] + nums[right] + nums[right - 1]
                continue

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff_current = abs(current_sum - target)
                diff_closest = abs(closest_sum - target)

                if diff_current == 0:
                    return current_sum  # exact match

                if diff_current < diff_closest:
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
        