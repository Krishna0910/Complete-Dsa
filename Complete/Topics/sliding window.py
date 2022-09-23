
import math


# Sliding Window



# Ques
# Let’s say, Given an arreay of size “n” we ar supposed to find the sum of all subarrays of size “k” in it.


# ip:
#arr : [2, 6, 9, -2, -1, 5, 4]
# k : 3

# O/p:
# [17, 13, 6, 2, 8]

# This is sliding window concept ques

# def sliding_window(arr,k):
#     ans=[]
#     wsum=0
#     ws=0
#     n=len(arr)
#     for we in range(n):
#         wsum+=arr[we]
#         if we>=k-1:
#             ans.append(wsum)
#             wsum-=arr[ws]
#             ws+=1
#     return ans 
# arr=[2, 6, 9, -2, -1, 5, 4]
# k=3
# ans=sliding_window(arr,k)
# print(ans)



# def maxSumSubarray(arr,k):
#     ans=-math.inf
#     wsum=0
#     ws=0
#     n=len(arr)
#     for we in range(n):
#         wsum+=arr[we]
#         if we<=k-1:
#             ans=max(ans,wsum)
#             wsum-=arr[ws]
#             ws+=1
#     return ans    


# arr=[2, 6, -9, 7, -1, 5, 4]N = 4, K = 2
# arr = [100, 200, 300, 400]
# k=2
# ans=maxSumSubarray(arr,k)
# print(ans)





# Ques:

# avgmaximumof kth Element

# def avgmax(arr,k):
#     wsum=0
#     ws=0
#     n=len(arr)
#     avgg=-111111
#     for we in range(n):
#         wsum+=arr[we]
#         if we>=k-1:
#             m=abs((wsum)/k)
#             avgg=max(m,avgg)
#             wsum-=arr[ws]
#             ws+=1
#     return avgg   


# arr = [1,12,-5,-6,50,3]
# k = 4
# ans=avgmax(arr,k)
# print(ans)

    
            
#  QUESTION           
# Minimum Difference Between Highest and Lowest of K Scores


# def minimumDiff(arr,k):
#     # ws=0
#     # wdiff=0
#     arr.sort(reverse=True   )
#     n=len(arr)
#     m=11111111
#     if n==1:
#         return 0
#     for we in range(n-k+1):
#         m=min(m,(arr[we]-arr[we-k+1]))
#     return m
# arr= [9]
# k=1
# ans=minimumDiff(arr,k)
# print(ans)    






# QUESTION
# Longest Substring With No More Than K Distinct Characters

# Given a string and an integer k, find the length of the longest substring with no more than k distinct characters.

# Input: "araabdda", k = 3
# Output: 6
# Explanation: araabdda, length of the longest substring with no more than 3 distinct characters {a, b, d}

# In this we using dictionary to check no of element count upto len k 

# to create a hash map
# s="avdhhgdffabcd
# # hashmap={} or hashmap=dict()
# for char in s:
#     hashmap[char]=hashmap.get(char,0)+1
# print(hashmap)    


#  Given a string and an integer k, find the length of the longest substring with no more than k distinct characters.

# Code

# def longestSubstringWithNoKDistinct(str,k):
#     ws=0
#     n=len(str)
#     m=0    #or -math.inf to check maximum
#     di={}
#     #iterate the loop
#     for we in range(n):
#         # right charc to check in dic
        
#         right_char=str[we]
#         # if right_char in di :
#         #     di[right_char]+=1    #if element there then add in dict +1
#         # else:
#         #     di[right_char]=1
#         di[right_char]=di.get(right_char,0)+1
#         while len(di)>k:    #check  jb tk element size jb tk km n ho jae
#             #minus the ws element 
#             left_char=str[ws]
#             di[left_char]-=1  #subtract the fisrt elemnt  unit its len is ==k
#             if di[left_char]==0:
#                 del di[left_char]
#             ws+=1
#         m=max(m,we-ws+1)
#     return m  

# str="avdhhgdffabcd" 
# k=3
# ans=longestSubstringWithNoKDistinct(str,k)
# print(ans)
         
         
         

# QUESTION  

# Given an integer array nums and an integer k, return true
# if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.    

# Input: nums = [1,2,3,1], k = 3
# Output: true   
                    
# Statement :
# if the same element found then check if first inx-lastindx is <=k return true else:false

                   
# Logic :
# store all element in dict
# check all the element in the dictinary if the same element found in dict. then swap the index of element with ws 

# def containDuplicate(arr,k):
#     ws=0
#     di={}
#     n=len(arr)
#     for we in range(n):
#         ele=arr[we]
#         if ele in di:
#             ws=di[ele]
#             if abs(ws-we)<=k:
#                 return True
#         di[ele]=we 
#     return False
# # arr=[1,2,3,1]
# arr=[1,2,3,1,2,3]
# k=2
# ans=containDuplicate(arr,k)
# print(ans)




# Ques :
# Substrings of Size Three with Distinct Characters

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".



# logic
# take an list append we element and check condtion if list  size jb tk equal n ho jae we+=1 uske naad condtion check kr unique char ki 
# if size of new string is equal to 3 then count+=1
# else array me ws ko remove kr do 

# def countGoodSubstring(s):
#     ws=0
#     temp=[]
#     count=0
#     n=len(s)
#     for we in range(n):
#         temp.append(s[we])
#         wlen=we-ws+1
#         if wlen<3:
#             we+=1
#         if wlen==3:
#             uniq=set(temp)
#             if len(uniq)==3:
#                 count+=1
#             temp.remove(s[ws])
#             ws+=1
#             we+=1
#     return count 
   
# s = "xyzzaz"
# ans=countGoodSubstring(s)
# print(ans)                
                    


# Ques 
# 3. Longest Substring Without Repeating Characters 
       
# Given a string s, find the length of the longest substring without repeating characters.


# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.        


# Logic  
# Put all The element in the hashmap if the repeated element occur toh ws ki index ko update kr denge we+1 element se 
# check  karenenge ki agr we wali elemtn ki index badi h ws wali se toh prev_element +1
# then check kr lenge  ki maxxx se 
# aur agr elemtn present nhi h hashmap me toh hashmap ki index ko we ki index bna denge



# def lengthOfLongestSubstring(s):
#     ws=0
#     hashmap={}
#     n=len(s)
#     maxm=0
#     for we in range(n):
#         r_char=s[we]
#         if r_char in hashmap:
#            ws = max(ws,hashmap[r_char] + 1)  // hashmap[char]+1  isliye kiya kyu ki hme elemnt ko ek aage wali posiotn se check krna h baad me n ki pichli position se  
#         maxm=max(maxm,we-ws+1)        
#         hashmap[r_char]=we 
#     return maxm  


# s="abcabcbb"
# ans=lengthOfLongestSubstring(s)
# print(ans)         

# # o/p: 3
        
        


# You are given an array of characters, representing the toys in the store. You have two bags to put toys in such a way that you put a maximum number of toys in each bag. But there is a restriction that each bag can only have one type of toy. You can start picking any toy but once you started you cannot skip any toy in between. 
# You can continue picking toys until you reached 3rd type of toy.        



# def toysIntoBag(s):
#     ws=0
#     hashmap={}
#     maxlen=0
#     for we in range(len(s)):
#         r_char=s[we]
#         if r_char in hashmap:
#             hashmap.get(r_char,0)+1
#         while len(hashmap)>2:
#             l_char=s[ws]
#             hashmap[l_char]-=1
#             if hashmap[l_char]==0:
#                 del hashmap[l_char]
#             ws+=1    
#         maxlen=max(maxlen,we-ws+1)
        
#     return maxlen

# s=['A','R','A','A','B','D','D','A']
# ans=toysIntoBag(s)
# print(ans)              
            
                
             
    
        
# Ques:
# 2260. Minimum Consecutive Cards to Pick Up

# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
               
               
# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. 
# Note that picking up the cards [4,2,3,4] is also optimal.               


# Logic :
# Using hashing and sliding window pattern and we check if the element come in hashmap 2 time then we find min of that length


# def minimumCardPickup(self, cards: List[int]) -> int:
#         ws=0
#         hashmap={}
#         minlen=math.inf
#         for we in range(len(cards)):
#             r_char=cards[we]
#             if r_char in hashmap:
#                 hashmap[r_char]+=1
#             else:
#                 hashmap[r_char]=1   
# #                 
#             while hashmap[r_char]==2:
#                 l_char=cards[ws]
#                 minlen=min(minlen,we-ws+1)
#                 hashmap[l_char]-=1
#                 if hashmap[l_char]==0:
#                     del hashmap[l_char] 
#                 ws+=1    
                
#         if minlen==math.inf:
#             return -1
#         else:
#             return minlen