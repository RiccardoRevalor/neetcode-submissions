class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) -1

        while index1 < index2:
            if numbers[index1] + numbers[index2] == target: 
                break
            elif numbers[index1] + numbers[index2] < target:
                #too small, add left
                index1 += 1
            else:
                #too big
                index2 -=1
        
        return [index1+1, index2+1]
        