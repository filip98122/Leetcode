class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lp=0
        rp=len(matrix)
        if target<matrix[0][0]:
            return False
        if target>matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]:
            return False
        matrix.append([matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]+1])
        while True:
            mp=(lp+rp)//2
            if matrix[mp][0]<=target<matrix[mp+1][0]:
                nums=matrix[mp]
                break
            if matrix[mp][0]<=target>=matrix[mp+1][0]:
                lp=mp
            if matrix[mp][0]>=target<=matrix[mp+1][0]:
                rp=mp
        rp=len(nums)-1
        lp=0
        lmp=0
        mp=0
        if len(nums)<=2:
            for i in range(len(nums)):
                if nums[i]==target:
                    return True
            return False
        while True:
            lmp=mp
            mp=(rp+lp)//2
            if lmp==mp:
                break
            if nums[mp]==target:
                return True
            if nums[mp+1]==target:
                return True
            if nums[mp]<target:
                lp = mp
            if nums[mp]>target:
                rp=mp
        return False
sol=Solution()
print(sol.searchMatrix([[1],[3],[5]],5))