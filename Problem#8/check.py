'''
name: Emma Verdugo
lab:@2pm

'''

def in_order(nums):
    # Type your code here.
     a = [nums[i-1] <= nums[i] for i in range(1, len(nums))]
     return all(x == a[0] for x in a)
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
