class Solution:
    
    # @return median of a sorted array
    def getMedian(self, a):
        l = len(a)

        if l%2==0:
            return ( float(a[l/2])+ float(a[l/2-1]) )/2.0 
        else:
            return float( a[l/2] )
            
    # @return median of 3 elem        
    def getMedian3(self, a1, a2, a3):
        return a1+a2+a3 - max(a1,a2,a3) - min(a1,a2,a3)
        
    # @return median of 4 elem
    def getMedian4(self, a1, a2, a3, a4):
        return float( a1+a2+a3+a4- max(a1,a2,a3,a4) -min(a1,a2,a3,a4) )/2.0
        
    # @return a float
    def findMedianSortedArrays(self, A, B):
	print "In function: A is ",A," B is ",B
        # Make sure A is shorter array
        if len(A) > len(B):
            temp = A
            A = B
            B = temp
        lenA = len(A)
        lenB = len(B)
        
        # Edge case0: empty array
        if lenA==0:
            return self.getMedian(B)

        # Edge case1: one Array with single element
        if lenA==1 or lenB==1:
            if lenA==1 and lenB!=1:
                finalArray = B
                insertElem = A[0]
            elif lenA!=1 and lenB==1:
                finalArray = A
                insertElem = B[0]
            else:
                return (A[0]+B[0])/2.0
                
            l = len(finalArray)
            if l % 2!=0:
                return (self.getMedian3(  finalArray[l/2-1], insertElem, finalArray[l/2+1] ) + float(finalArray[l/2]) )/2
            else:
                return self.getMedian3( finalArray[l/2-1],finalArray[l/2], insertElem)
        
        # Edge case2: one Array with 2 element
        if lenA==2 and lenB==2:
            return self.getMedian4( A[0], A[1], B[0], B[1] )
            
        elif lenA==2 or lenB==2:
            if lenA==2:
                finalArray = B
                two = A
            if lenB==2:
                finalArray = A
                two = B
            l = len(finalArray)
            if l%2!=0:
                return self.getMedian3( max(two[0],finalArray[l/2-1]), finalArray[l/2], min(two[1], finalArray[l/2+1]) )
            else:
                p1 = max(two[0], finalArray[l/2-2])
                p2 = min(two[1], finalArray[l/2+1])
                return self.getMedian4( p1, finalArray[l/2-1], finalArray[l/2], p2 )
            
        # if middle of A > middle of B, discard the right of median A
        if A[lenA/2] > B[lenB/2]:
            return self.findMedianSortedArrays(A[0:lenA/2+1], B[lenA/2-1:])
 
        # if median of A < median of B, discard the right of median B
        else:
	    print "not sure what happened with -lenA/2 = ",-lenA/2
            return self.findMedianSortedArrays( A[lenA/2:], B[0:-(lenA/2)])

s = Solution()
ans = s.findMedianSortedArrays([1,2,6,4],[3,4,5,8])
print "Answers is: ",ans
