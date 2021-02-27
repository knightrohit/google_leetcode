"""
Time/Space Complexity = O(m+n)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = j = 0
        out = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                out.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                out.append(nums2[j])
                j += 1
                
            else:
                out.append(nums1[i])
                out.append(nums2[j])
                i += 1
                j += 1
                
        if i < len(nums1):
            out.extend(nums1[i:])
        elif j < len(nums2):
            out.extend(nums2[j:])
            
            
        # Return median
        if len(out) % 2:
            return out[len(out)//2]
        
        else:
            mid = (len(out) - 1)//2
            if mid + 1 < len(out):
                return (out[mid] + out[mid+1])/2
            else:
                return out[mid]