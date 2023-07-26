class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for item in nums:
            if item not in counts:
                counts[item] = 1
            else:
                counts[item] += 1

        newlist = [[] for i in range(len(nums)+1)]

        for item, count in counts.items():
            newlist[count].append(item)

        output = []

        for i in range(len(newlist)-1,-1,-1):
            if newlist[i]:
                for j in range(len(newlist[i]) -1, -1, -1):
                    if k < 1:
                        break
                    else:
                        output.append(newlist[i][j])
                        k -= 1

        return output