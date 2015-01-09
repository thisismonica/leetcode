def combination( s ):
    if s == "": return 0
    if len(s) == 1: 
    
        if s[0]!='0': return 1
        # '0'
        else: return 0
   
   # 123
    if s[0]!= '0':
        # 123
        if int(s[0:2])<=26 and int(s[0:2])>=10:
            # 12+ 3, 1, 23
            res = combination( s[1:] ) + combination( s[2:] ) 
        # 273
        else:
            res = combination( s[1:] )
    return res

s = "11"
print "Combination for : ",s," is ", combination(s)
