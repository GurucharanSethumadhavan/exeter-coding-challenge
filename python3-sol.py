class Solution:
    def twoSum(nums,target):
       d=dict()
       for i in range(len(nums)):
           if target-nums[i] in d.keys():
               print("Output:",[d[target-nums[i]],i])
           else:
               d[nums[i]]=i
nums=[]
a=int(input("Enter number of elements in nums"))
if a>=2 and a<=104:
    for i in range(a):
        b= int(input("Enter element "+str(i+1)+" of nums"))
        nums.append(b)
    count=0
    for i in nums:
        if i>=-109 and i<=109:
            count+=1
    if count==a:
        target=int(input("Enter target value"))
        if target>=-109 and target<=109:
            s=Solution
            s.twoSum(nums,target)
        else:
            print("Target out of range")
    else:
        print("Element of nums out of range")
else:
    print("Number of elements of nums out of range")
                    
            
        
