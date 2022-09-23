#Ques: Target_sum :

# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. 
# Your task is to return the indices of the two numbers (i.e. the pair)  such that they add up to the given target.

# I/p arr=[1,2,3,4,6]
# o/p [1,3]

# def target_sum(arr,target):
#     l=0
#     r=len(arr)-1
#     while l<r:
#         if arr[l]+arr[r]==target:
#             return[l,r]
#         else:
#             if arr[l]+arr[r]>target:
#                 r-=1
#             else:
#                 l+=1
#     return [-1,-1]          


# arr=[1,2,3,4,6]
# target=6
# summ=target_sum(arr,target)
# print(summ)





# Given an array of sorted numbers, Square each number and arrange their squares in sorted order.

# I/n arr=[-1, 0, 1, 2, 3]
# O/p temp=[0 1 1 4 9 ]

# code

# def square_sorted(arr,n):
#     temp=[0]*n
#     low,high,new_len=0,n-1,n-1
#     while low<=high:
#         low_sq=arr[low]*arr[low]
#         high_sq=arr[high]*arr[high]
        
#         # check which is greater so it append into right side
#         if low_sq<high_sq:
#             temp[new_len]=high_sq
#             high-=1
#         else:
#             temp[new_len]=low_sq
#             low+=1
#         new_len-=1
#     return temp   


# arr=[-1, 0, 1, 2, 3]
# n=len(arr)
# sorter=square_sorted(arr,n)   

# for i in sorter:
#     print(i,end=" ")
        
    



# Given an array containing 0’s, 1’s and 2’s, Sort the array inplace. You can’t count the frequency of elements and refill the array.

# The flag of the Netherlands consists of three colors: red, white and blue;
# and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# In-place: Do not use Extra Space.
# and put original numbers init


# Input: arr: [1, 1, 2, 0, 1, 0, 2, 1, 0]
# Output: [0, 0, 0, 1, 1, 1, 1, 2, 2]


# approch

# def dutch(arr):
#         zero, one, two = 0, 0, len(arr) - 1
#         while one <= two:
#             element = arr[one]
#             if element == 0:
#                 arr[zero], arr[one] = arr[one], arr[zero]
#                 zero += 1
#                 one += 1
#             elif element == 1:
#                 one += 1
#             else:
#                 arr[one], arr[two] = arr[two], arr[one]
#                 two -= 1;
            
            
# arr=[1, 1, 2, 0, 1, 0, 2, 1, 0]       
# ans=dutch(arr)
# print(ans)            
            



# Valid Plaindrome
# Ques   A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


# logic: first change to lowercase and then take all alphanumeric values in another string , then check using two pointer 



# def ispalindrome(s):
#     s=s.casefold()    #casefold is used to lowercase
#     newStr=" "
#     for i in s:
#         if i.isalnum():
#             newStr+=i
#     l=0
#     r=len(newStr)-1
#     while l<=r:
#         if newStr[l]==newStr[r]:
#             l+=1
#             r-=1
#         else:
#             return False
#     return True

# s="ar,ra"
# ans=ispalindrome(s)
# print(ans)    




# Duplicate Zero
# Ques  Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. 
# Do the above modifications to the input array in place and do not return anything.  

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

# def duplicateZero(arr):
#     i=0
#     j=len(arr)
#     while i<j:
#         if arr[i]==0:
#             arr.insert(i+1,0)
#             arr.pop()
#             i+=2
#         else:
#             i+=1
#     return arr    

# arr = [1,0,2,3,0,4,5,0]
# ans=duplicateZero(arr)
# print(ans)  





# Ques : 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.     

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.



# Logic 
# Take one variable which is incresing one by one and in other two use two sum method and checksum of all if equal then add to result


# def ThreeSum(arr,n):
#     arr.sort()
#     result=[]
#     for i in range(0,n-1):
#         if i>0 and arr[i]==arr[i-1]:
#             continue
#         twoSum(arr,i,i+1,result)
#     return result    

# def twoSum(arr,i,j,result):
#     k=len(arr)-1
#     while j<k:
#         sum=arr[i]+arr[j]+arr[k]
#         # check sum is equal to zero or not
#         if sum==0:
#             result.append([arr[i],arr[j],arr[k]])
#             j+=1
#             k-=1
#             while j<k and arr[j]==arr[j-1]:
#                 j+=1
#             while j<k and arr[k]==arr[k+1]:
#                 k-=1
#         elif sum>0:
#             k-=1
#         else:
#             j+=1      
            
# arr = [-1,0,1,2,-1,-4]
# n=len(arr)
# ans=ThreeSum(arr,n)  
# print(ans)            
            
            
            
            
      
# Ques Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).         


# Logic the difference between the target and sum abs. is min, then it is their closest to target

# def threesumclose(arr,target):
#     arr.sort()
#     n=len(arr)
#     diff=1111111111
#     for i in range(0,n-1):
#         j=i+1
#         k=len(arr)-1
#         while j<k:
#             sum=arr[i]+arr[j]+arr[k]
#             if sum==target:
#                 return target
#             elif abs(target-sum)<diff:
#                 diff=abs(target-sum)
#                 ans=sum
#             if sum>target:
#                 k-=1
#             else:
#                 j+=1
#     return ans                    
             
             
# arr= [-1,2,1,-4] 
# target=1
# anss=threesumclose(arr,target)
# print(anss)  





# Ques  Triplet sum less than zero
# Given an array of unsorted numbers and an integer target, find total number of triplets in it that add up to smaller than target.



# Input: arr: [-1, 2, 3, 0], target = 3
# Output: 2

# Explanation: There are only two triplets with sum less than 3, [-1, 0, -3] and [-1, 0, 2]
# class Twopointer:
#     def find_triplet(arr,target):
#         arr.sort()
#         n=len(arr)
#         res=0
#         for i in range(0,n-1):
#             res+=Twopointer.less_sum(arr,i,i+1,target)
#         return res              
                
#     def less_sum(arr,i,j,target):
#         k=len(arr)-1
#         res=0
#         while j<k:
#             sum=arr[i]+arr[j]+arr[k]
#             if sum<0:
#                 res+=(k-j)
#                 j+=1
#             else:
#                 k-=1
#         return res

                            
# arr=[-1, 2, 3, 0]
# target=3
# ans=Twopointer.find_triplet(arr,target)
# print(ans)   




# Ques Count triplet sum  with in range

# Given an array of unsorted numbers and a range [a, b],
# find total number of triplets in it that add up int the range a to b, such that a <= sum <= b.


# Input: arr: [0, -1, -3, 2, 7], a = 6, b = 9
# Output: 4
# Explanation: Only triplets having sum greater than or equal to 6 and less than or equal to 9 are [-3, 2, 7], [-1, 0, 7], [-1, 2, 7] and [0, 2, 7].
  
  
               
# def count_range_sum(arr,a,b):
#     arr.sort()
#     return count_triplt(arr,b)-count_triplt(arr,a-1)
# def count_triplt(arr,target):
#     res=0
#     n=len(arr)
#     for  i in range(0,n-1):
#         res+=less_sum(arr,i,i+1,target,n)
#     return res    
# def less_sum(arr,i,j,target,n):
#     k=n-1
#     res=0
#     while j<k:
#         sum=arr[i]+arr[j]+arr[k]
#         if sum<target:
#             res+=k-j
#             j+=1
#         else:
#             k-=1
#     return res        
                
# arr=[0, -1, -3, 2, 7]
# a = 6
# b = 9 
 
# ans=count_range_sum(arr,a,b)
# print(ans)        
          
          
          
          
          
          
          
# Ques 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.  


# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]  

#  Logic:
# We solve it like three Sum technique  in this hm ek aur loop chalaenge jo phele 3Sum me callhoga fhir 2nd 
# aur first value jaake two Sum me call hogi and condition check kareng😁




# def four_sum(arr,target):
#         arr.sort()
#         result=[]
#         n=len(arr)
#         for i in range(0,n-2):     #first value
#             if i>0 and arr[i]==arr[i-1]:
#                 continue
#             for j in range(i+1,n-1):  2nd value
#                 if j>i+1 and arr[j]==arr[j-1]:
#                     continue
#                 k=j+1                 3rd value
#                 l=n-1                 fourth value
#                 # sum_target=target-arr[i]-arr[j]
#                 while(k<l):
#                     Sum=arr[i]+arr[j]+arr[k]+arr[l]
#                     if Sum==target:
#                         result.append([arr[i],arr[j],arr[k],arr[l]])
#                         k+=1
#                         l-=1
#                         while k<l and arr[k]==arr[k-1]:
#                             k+=1
#                         while k<l and arr[l]==arr[l+1]:
#                             l-=1
#                     elif Sum>target:
#                         l-=1
#                     else:
#                         k+=1
                                    
#         return result 
            
            
# arr = [1,0,-1,0,-2,2] 
# target = 0
# ans=four_sum(arr,target)
# print(ans)




# Ques:   Backspace  string compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.


# Note: backspace se piche wali value ht jaegi 

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
       
       
# Logic :
#   Ek fun. bnaenge jo valid valuewale ka indx return karega string me aur un dono index wali value pe condtion check karenge ki qual h ki nhi
 
# Condtion in function
# check karenge agr value # h toh ek backspace varible ko bdha denge aur fhir utne element ki indx hta denge loop me se 


# code

def backspaceCompare(self, s: str, t: str) -> bool:
        def getValidIndex(s, i):
            cnt = 0
            
            while i >= 0:
                if s[i] == '#': cnt += 1
                elif cnt > 0: cnt -= 1 #Not the # but the cnt is present
                else: break
                
                # Reucing index in every call
                i-= 1
            
            return i
                    
        
        
        ################ Primary Fctn Here ##########
        
        p1, p2 = len(s)-1, len(t)-1
        
        while p1 >= 0 or p2 >= 0:
            v1 = getValidIndex(s, p1)
            v2 = getValidIndex(t, p2)
            
            if v1 < 0 and v2 < 0:
                return True
            
            if v1 < 0 or v2 < 0:
                return False
        
            if s[v1] != t[v2]:
                return False
            
            if v1 == 0 and v2 == 0:
                return True
            
            

            p1 = v1-1
            p2 = v2-1
        


s = "ab#c"
t = "ad#c"  
ans=backspace_compare(s,t)    
print(ans)           
        
       
                          
    
        
             
   
            
            
                              