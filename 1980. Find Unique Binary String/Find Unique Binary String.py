nums = ["111","011","001"]
ans = []
for i in range(len(nums)):
    curr = nums[i][i]
    ans.append("1" if curr == "0" else "0")

print("".join(ans))