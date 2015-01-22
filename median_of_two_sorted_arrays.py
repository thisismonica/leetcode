class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (len(A) + len(B)) % 2 == 0:
            return (self.fms(A, B, (len(A) + len(B))/2) + self.fms(A, B, (len(A) + len(B))/2 + 1))/2.0
        else:
            return self.fms(A, B, (len(A) + len(B))/2 + 1)
     
    def fms(self, A, B, k):
        if len(A) > len(B):
            return self.fms(B, A, k)
        else:
            if len(A) == 0:
                return B[k-1]
            if k == 1:
                return min(A[0], B[0])
            pa = min(k/2, len(A))
            pb = k - pa
            if A[pa-1] <= B[pb-1]:
                return self.fms(A[pa::], B, k-pa)
            else:
                return self.fms(A, B[pb::], k-pb)
    

            
            