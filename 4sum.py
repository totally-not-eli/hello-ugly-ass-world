class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #so not from leetcode right? kek
    
    #thought process go brr, here it comes lad
    #create a pointer for the first index, second index and simultaneous pointers for left and right, basically just 3 loops with 1 loop as binary search :p 
    #NO IM NOT GONNA MAKE A HELPER FUNCTION
    
    lenOfNums = len(nums)
    ans = []
    
    for i in range(lenOfNums-3):
      #-3, since u want it to point at the last first element that would have 4 elements exact, no errors fam.
      #the problem wants no duplicates so :p here's a way to do that
      if i > 0 and nums[i] == nums[i-1]:
        #basically if i is greater than 0, meaning after the first element, u wanna check if the next few elements are new or the same, if same, continue the stupid iteration.
        continue
      for j in range(i+1,lenOfNums-2):
        #i+1, ofcourse, it would be the next pointer after i, wdyt? :/, lenOfNums == last element, lenOfNums -1 = second to the last, you know what's next :p.
        # same reason for the i loop.
        if j > i+1 and nums[j] == nums[j-1]:
          continue
        #same reasoning as the earlier :p
        #NOW ITS TIME FOR THE ALL TIME FAVORITEEE, BINARY SEARCH KEKW ;-;
        totallyNotLeft, totallyNotRight = j+1, lenOfNums-1
        while totallyNotLeft < totallyNotRight:
          summ = nums[i] + nums[j] + nums[totallyNotLeft] + nums[totallyNotRight]
          if summ == target:
            # yey append dat sht
            ans.append([nums[i], nums[j], nums[totallyNotLeft], nums[totallyNotRight]])
            #check for possible duplicates fam,
            totallyNotLeft += 1
            totallyNotRight -= 1
            while totallyNotLeft < totallyNotRight and nums[totallyNotLeft] == nums[totallyNotLeft-1]:
              totallyNotLeft += 1
            while totallyNotLeft < totallyNotRight and nums[totallyNotRight] == nums[totallyNotRight+1]:
              totallyNotRight -= 1
          elif summ > target:
            totallyNotRight -= 1
          else:
            totallyNotLeft += 1
    return ans     
              
              
        
     
    
    
