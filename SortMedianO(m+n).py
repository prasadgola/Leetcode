class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a,b = nums1, nums2
        l = len(a) + len(b)

        if l % 2:
            print (self.get_median(a,b, l//2))
        else:
            print ((self.get_median(a,b,l//2) + self.get_median(a,b,l//2 - 1)) / 2)
        
    def get_median(self, a, b, idx):

        if not a:
            return b[idx]
        if not b:
            return a[idx]

        ai = len(a) // 2
        bi = len(b) // 2
        ma = a[ai]
        mb = b[bi]

        if ma > mb:
            ma, mb = mb, ma
            ai, bi = bi, ai
            a,b = b, a

        max_idx_ma = len(a) // 2 + len(b) // 2

        if max_idx_ma < idx:
            med = self.get_median(a[ai+1:],b, idx - (len(a)//2+1))
        else:
            med = self.get_median(a,b[:bi], idx)
          
        
        return med

object = Solution()
object.findMedianSortedArrays([1,2,3,4,5],[6,7,8,9,10])