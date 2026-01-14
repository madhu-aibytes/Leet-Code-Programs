class Solution:
    def trap(self,height):
        heightSize=len(height)
        if heightSize<3:
            return 0
        LM=[0]*heightSize
        RM=[0]*heightSize
        m=0
        for i in range(heightSize):
            m=max(m,height[i])
            LM[i]=m
        m=0
        for i in range(heightSize-1,-1,-1):
            m=max(m,height[i])
            RM[i]=m
        water=0
        for i in range(heightSize):
            water+=min(LM[i],RM[i])-height[i]
        return water
    
n=int(input())
height=list(map(int,input().split()))
s=Solution()
print(s.trap(height))
