class Solution:
	def evalRPN(self, tokens):
		stack = []
		i = 0
		while i < len(tokens):
			if tokens[i] not in "+-*/":
				try:
					stack.append( int(tokens[i]) )
				except ValueError:
					print "Invalid Polish Notation"
			else:
				try:
					num2 = stack.pop()
					num1 = stack.pop()
					if tokens[i] == "+":
						stack.append( num1+num2 )
					elif tokens[i] == "-":
						stack.append( num1-num2 )
					elif tokens[i] == "*":
						stack.append( num1*num2 )
					elif tokens[i] == "/":
						print "Dividing: ","num1 = ",num1," num2= ",num2
						stack.append( num1/num2 )
				except IndexError:
					print "Invalid Polish Notation"
			i = i+1
			print "Stack: ",stack
		return stack[-1]

s = Solution()
rpn = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print "RPN: ",rpn," Value is: ",s.evalRPN(rpn)
