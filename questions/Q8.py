# function which return reverse of a string

def isPalindrome(n):
	return n == n[::-1]

n = "radar"
result = isPalindrome(n)

if result:
	print("Yes")
else:
	print("No")
