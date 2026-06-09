class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        x=0
        lst = [0]*len(temperatures)
        st.append(0)
        for i in range(1,len(temperatures)):
            while x>=0 and temperatures[st[x]] < temperatures[i]:
                lst[st[x]] = i-st[x]
                x-=1
            x+=1
            if x<len(st):
                st[x] = i
            else:
                st.append(i)
        return lst