
# Ques : Valud Parenthesis

# Problem Statement
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is balanced.

# An input string is balanced if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

# Logic 

# We will create a stack of characters and visit the whole string starting from index 0 to the end.
# If the character is either of the following (, {, or [, we will push it onto the stack.
# If the character is either of the following ), }, or ], then we will pop from the stack. But we will have a separate check for the validation. Let’s understand it by an example.
# Suppose the character is ), then the stack top must be (.
# And this is to be validated for the rest of the two types of brackets also.



# code 
# class Stack:
#     def is_valid(s):
#         stack=[]
#         n=len(s)
#         for i in range(n):
#             if(s[i]is'('or s[i] is '{' or s[i] is '['):
#                 stack.append(s[i])
#             else:
#                 #Check for stack is empty 
#                 if len(stack)==0:
#                     return False 
#                 # if the pop element and the string element are of same type then return True 
#                 if (Stack.is_matching(stack.pop(),s[i]) is not True):
#                     return False
#         if (len(stack)==0):  #agr sb sahi wale hue toh stack empty ho jaega
#             return True 
#         return False       
    
#     def is_matching(ob,cb):
#         if(ob is '(' and cb is ')'):
#             return True 
#         if(ob is '{' and cb is '}'):
#             return True 
#         if(ob is '[' and cb is ']'):
#             return True
#         else:
#             return False        
                
# s="()[]{}"
# ans=Stack.is_valid(s)
# print(ans)  
                      
                      
                      



# Ques Simplify path

# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:

# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')                      



# Input: path = "/home//movies/.//./bollywood/../../songs/"
# Output: "/home/songs"
# Explanation: First you entered into home directory, then to movies, after that there is no meaning of "." and "//",
# then you further enterned into bollywood directory and then finally returned back twice by using ".." twice and 
# reached in home. And finally enetered into songs. Hence /home/songs is the answer.




# logic
# split the string by'/'
# check by apply loop if i is '.' or "" then aage dh jao
# if ".." then pop otherwise push

# return conanical path by mergethestack in in given order

# code 

# def simpify_path(s):
#        new_path=s.split('/')
#        stack=[]
#        n=len(s)
#        for i in new_path:
#            if i=='.' or i=="":
#                continue
#            elif i =="..":
#                if len(stack)!=0:
                   
#                    stack.pop()
#            else:
#                 stack.append(i) 
#        canonical_path='/'+'/'.join(stack)
#        return canonical_path
   
# s=".//./bollywood/../../songs/"  
# ans=simpify_path(s)
# print(ans)







# Ques Evaluate Reverse Polish Notation



# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Logic if it is element then directly push if it is any pression then perform operation
# # Code 
# def evalRPN(tokens):
#     stack=[]
#     for i in tokens:
#         if i not in ["+","-","*","/"]:
#             stack.append(i)
#         else:
#             a=int(stack.pop())
#             b=int(stack.pop())
#             if i=="+":
#                 stack.append(a+b)
#             elif i=='-':
#                 stack.append(b-a)
#             elif i=='*':
#                 stack.append(a*b)
#             else:
#                 stack.append(int(b/a))
#     return stack.pop()                            
    
# tokens = ["4","13","5","/","+"]    
# ans=evalRPN(tokens)
# print(ans)       




# Ques 
# Remove All Adjacent Duplicates In String  


# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
# The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".             
                         
           
# Logic Make a stack and append all elelement of string and if the element is found in stack then pop

# def removeDuplicates(s):
#     stack=[]
#     for i in s:
#         if len(stack)==0:
#             stack.append(i)   
#         elif i==stack[-1]:
#             stack.pop()
#         else:
#             stack.append(i)
#     res="".join(stack)        
#     return  res  

# s="abbacca"
# ans=removeDuplicates(s)
# print(ans)        


# Ques :Next greater element to the right



# def nextLargerElement(arr,n):
#     # create an empty array an stack
#         res = [-1]*n
#         stack=[0]
#         # traverse it in reverse order
#         for i in range(n-1,-1,-1):
#             # check jb tk len(stack) is not equal to zero aur stack me jo element hagr voh chota h toh loop end ho jaega
#             while (len(stack)!=0 and stack[-1]<=arr[i]):
#                 stack.pop()
#             # agr koi bda element right me nhi mila toh retrun -1 
#             if len(stack)==0:
#                 res[i]=-1
#             # agr stack me koi element h toh voh element se bda hoga then return that 
#             else:
#                 res[i]=stack[-1]
#             # one by one append krate jao stack me 
#             stack.append(arr[i])
#         return res  
        
                     


# arr=[10,7,5,4,9,2,1,6]
# n=len(arr)
# ans=nextLargerElement(arr,n)
# print(ans)





# Ques 1614. Maximum Nesting Depth of the Parentheses

# A string is a valid parentheses string (denoted VPS) if it meets one of the following:

# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

# Given a VPS represented as string s, return the nesting depth of s.

 

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.



# def maxDepth(s):
#     stack=[]
#     n=len(s)
#     count=0
#     for i in range(n):
#         if s[i]=='(':
#             stack.append(s[i])
#         elif s[i]==')':
#             stack.pop()
#         else:
#             continue
#         count=max(count,len(stack))
#     return count         


# s="(1+(2*3)+((8)/4))+1"   
# ans=maxDepth(s)
# print(ans)









# Ques  next greater element to the right 


# logic 
# take a stack and iterate in reverse order and check if the left element is greater or not if greater then push into stack 
# if the element is greater than stack ka top then pop the element until it find greater than it agr nhi mile toh return -1 
# aur agr element mil jae toh usko ek array me store kr denge 



# def Nextgreaterelementtoright(arr):
#     # take a stack
#     n=len(arr)
#     stack=[]
#     ans=[0]*n
#     # iterate in reverse order
#     for i in range(n-1,-1,-1):
#         while len(stack) and stack[-1]==arr[i]: # jb tk len of stack not empty aur stack elmnt is smaller than arr[i]
#             stack.pop()
#         if not len(stack):
#             ans[i]=-1
#         else:
#             ans[i]=stack[-1]
#         stack.append(arr[i])   # aur element toh append krne hi h 
#     return ans 

# arr=[1,3,4,2]
# ans=Nextgreaterelementtoright(arr) 
# print(ans)     


# similar as  ques  next greater element to the left ,Next smaller element to the right,left     




             
             
 
                
# Ques Next greater element I 496



# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.



# Logic find the next greater element to the right first  then usko ek hashmap me store kr lenge as {element:nger}
# fhir ek llop me use check kr lenge ki elememt ki index ka h use ans array me store kra lenge


# def nextGreaterElement(nums1,nums2):
#     # First fing next greater element to the right
#     def nextgreaterright(arr):
#         # take a stack and an array
#         n=len(arr)
#         stack=[]
#         ans=[0]*n
#         for i in range(n-1,-1,-1):
#             while(len(stack) and stack[-1]<=arr[i]):
#                 # jb tk len of stack not empty aur stack elmnt is smaller than arr[i]
#                 stack.pop() 
#             # after while condtion break 
#             # jb koi element greater nhi mile then    
#             if not len(stack):
#                 ans[i]=-1    
#             #mil jae toh  
#             else:
#                 ans[i]=stack[-1]
#             stack.append(arr[i])
#         return ans 
#     n=len(nums1)
#     m=len(nums2)
#     hashmap={}
#     ans=[]
    
#     position=nextgreaterright(nums2)
    
#     # store element and index in hashmap
#     for i in range(m):
#         hashmap[nums2[i]]=position[i]
        
#     # find greater elemtn for nums1 ans store to ans 
#     for i in range(n):
#         ans.append(hashmap[nums1[i]])
#     return ans
    

# nums1 = [4,1,2] 
# nums2 = [1,3,4,2]   
# ans=nextGreaterElement(nums1,nums2)
# print(ans)




# Ques 503. Next Greater Element II

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.
 
 
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.


# Logic Make an copy array of size is double of arr and find next greater element to the right 

# def nextGreaterElements(nums):
#     copynums=nums+nums
#     n=len(copynums)
#     ans=[0]*n
#     stack=[]
#     for i in range(n-1,-1,-1):
#         while len(stack) and stack[-1]<=copynums[i]:
#             stack.pop()
#         if not len(stack):
#             ans[i]=-1 
#         else:
#             ans[i]=stack[-1]
#         stack.append(copynums[i])
#     return ans[0:len(nums)]

# nums=[1,2,1]
# ans=nextGreaterElements(nums)
# print(nums)   






# Ques 84. Largest Rectangle in Histogram


# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.           

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.




# Logic We have to find largest area of rectangle  in the histogram so we can 
# find the next smaller element to the left and next smaller element to the right to the range of,
# which the element lies is nser-nsel-1 so the given range comes  and then multiply with the array of height and find maxarray


# code 
def largestRectangleArea(heights,n):
        
        def nsel(arr):
            n=len(arr)
            stack=[]
            nsel=[0]*n
            for i in range(n):
                
               # find the next smaller element to the left
            
                while (len(stack) and stack[-1][0]>=arr[i]): 
# wwe iterate loop until the smaller elemtn comes we pop the element from stack
                    stack.pop()
               #when the loop ends
               # if smaller element does not found
            
                if not len(stack):
                    nsel[i]=[-1,-1] 
                    
                # if found    
                else:
                    nsel[i]=[stack[-1][0],stack[-1][1]]
            # append all element in the stack    
                stack.append([arr[i],i])
            return nsel
        def nser(arr):
            n=len(arr)
            stack=[]
            nser=[0]*n
            for i in range(n-1,-1,-1):
                
               # find the next smaller element to the right
            
                while (len(stack) and stack[-1][0]>=arr[i]):
                    
# we iterate loop until the smaller elemtn comes we pop the element from stack

                    stack.pop()
                 #when the loop ends
               # if smaller element does not found
               # then append the last element                
            
                if not len(stack):
                    
                    nser[i]=[n,n] 
               # if found    
                else:
                    nser[i]=[stack[-1][0],stack[-1][1]]
                stack.append([arr[i],i])
            return nser   
        nsel_Indx=nsel(heights)
        nser_Indx=nser(heights)
#         print(nser_Indx,nsel_Indx)
        
        maxArea=0
        for i in range(n):
            width = nser_Indx[i][1] - nsel_Indx[i][1] - 1
            height =heights[i]
            
            #find the maximum area
            maxArea=max(maxArea,width*height)
        return maxArea     
            
    
    
      
        



heights=[2,1,5,6,2,3] 
n=len(heights)
ans=largestRectangleArea(heights,n)
print(ans)
      
                
                       

 
 
    
             
        
        
               
        
     
                     