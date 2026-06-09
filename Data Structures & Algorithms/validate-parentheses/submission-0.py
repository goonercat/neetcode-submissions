class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic =  {"(":")",
                "[":"]",
                "{":"}"}

        for ch in s:
            if ch in dic:
                st.append(ch)
            else:
                if not st:
                    return False

                top = st.pop()

                if dic[top] != ch:
                    return False

        return len(st) == 0