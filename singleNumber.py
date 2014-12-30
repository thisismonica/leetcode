def single( S ):
	N = len(S)
	if N == 1: return [ S[0] ]
	if N == 2: return S if S[0]!=S[1] else None
	left = single(S[:N/2])
	right = single(S[N/2:])
	if left and right:
		if left == right:
			return None
		else:
			return list(set(right)-set(left) | set(left)-set(right) )
		
	if left==None and right==None:
		return None
	return right if left==None else left

def singleSlow( S ):
	if S == []:
		return None
	prev = S[0]
	i = 1
	while i+1 < len(S):
		if S[i] != prev:
			return S[i]
		prev = S[i+1]
		i = i+2	
	return None

S = [1,1,2,2,3,3,4,4,6,6,7,7,8]
import time
start1 = time.clock()
print "Single number is ", single(S), " For: ",time.clock()-start1
start2 = time.clock()
print "Single number is ", singleSlow(S)," For: ",time.clock()-start2

