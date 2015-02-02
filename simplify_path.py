DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, path):
    	path_ori = path.split('/')
    	path_red = []
    	for p in path_ori:
    		if p!='' and p!='.':
    			path_red.append(p)

    	# Check for '..'
    	path_list = []
    	for i in range(len(path_red)):
    		if path_red[i] == ".." :
    			if len(path_list)>0:
    				del path_list[-1]
    			continue
    		path_list.append( path_red[i] )

    	# Output
    	res = "/"
    	if path_list == []:
    		return res
    	for p in path_list[:-1]:
    		res= res+p+'/'
    	res+=path_list[-1]
    	return res


# Testing
s = Solution()
test = "/home//foo/"
print "Tesing: ",test
print "Answers: ",s.answer(test)     
