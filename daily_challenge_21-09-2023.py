class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l=[]
        i=0
        j=0
        a=len(nums1)
        b=len(nums2)
        # c=math.floor((a+b)/2)+1
        while i<a and j<b:
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        if j<b:
            l.extend(nums2[j:])
        if i<a:
            l.extend(nums1[i:])
        print(l,a,b)
        if (a+b)%2==0:
            return ((float(l[(a+b)/2])+float(l[(a+b)/2-1]))/2)
        else:
            return l[len(l)//2]