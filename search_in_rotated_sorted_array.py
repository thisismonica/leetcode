class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right =0, len(A)-1
        while left <= right:
            mid = (left + right)/2
            if A[mid] == target:
                return mid
            if A[mid] >= A[left]:
                if target >= A[left] and target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > A[mid] and target <= A[right]:
                    left = mid +1
                else:
                    right = mid - 1
        return -1