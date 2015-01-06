class Solution:
    def compareVersion(self, version1, version2):
        version_num1 = version1.split('.')
        version_num2 = version2.split('.')
        diff = len(version_num1) - len(version_num2)
        
        version_num1 = [int(v) for v in version_num1]
        version_num2 = [int(v) for v in version_num2]
        
        if diff > 0:
            for d in range(diff):
                version_num2.append(0)
        elif diff < 0:
            for d in range(-diff):
                version_num1.append(0)
    
        for i in range( len(version_num1) ):
            if version_num1[i] > version_num2[i]:
                return 1
            elif version_num2[i] > version_num1[i]:
                return -1

        return 0

s = Solution()
test1 = "01"
test2 = "1"
print "Test: ",test1,test2," Answer: ",s.compareVersion(test1,test2)
