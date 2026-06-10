class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zp = sorted(zip(position,speed),reverse = True)

        st = []

        for pos ,spe in zp:
            t = (target-pos)/spe
            if not st or t>st[-1]:
                st.append(t)
        
        return len(st)