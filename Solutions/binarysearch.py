class Solution:
    def search(self, nums: list[int], target: int) -> int:
        rp=len(nums)-1
        lp=0
        lmp=0
        mp=0
        if len(nums)<=2:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
            return -1
        while True:
            lmp=mp
            mp=(rp+lp)//2
            if lmp==mp:
                break
            if nums[mp]==target:
                return mp
            if nums[mp+1]==target:
                return mp+1
            if nums[mp]<target:
                lp = mp
            if nums[mp]>target:
                rp=mp
        return -1
sol=Solution()
print(sol.search(list(map(int,input().split())),int(input())))