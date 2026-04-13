class Solution:
    def findPeak(self,mountainArr):
        start,end=0,mountainArr.length()-1

        while start<end:
            mid=(start+end)//2

            if mountainArr.get(mid) < mountainArr.get(mid+1):
                start=mid+1
            else:
                end=mid
        return end
    
    def binarySearch(self,mountainArr,start,end,target):
        isAsc = mountainArr.get(start)<mountainArr.get(end)

        while start<=end:
            mid=(start+end)//2

            if mountainArr.get(mid) < target:
                if isAsc:
                    start=mid+1
                else:
                    end=mid-1
            elif mountainArr.get(mid) > target:
                if isAsc:
                    end=mid-1
                else:
                    start=mid+1
            
            else:
                return mid
        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak = self.findPeak(mountainArr)

        asc = self.binarySearch(mountainArr, 0,peak,target)

        if asc!=-1:
            return asc
        
        return self.binarySearch(mountainArr, peak+1,mountainArr.length()-1,target)


        