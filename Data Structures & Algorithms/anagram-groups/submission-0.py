class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unik = []
        for i in range(len(strs)):
            if sorted(strs[i]) not in unik:
                unik.append(sorted(strs[i]))
        
        lst = [[]for i in range(len(unik))]

        for i in range(len(unik)):
            for j in range(len(strs)):
                if unik[i] == sorted(strs[j]):
                    lst[i].append(strs[j])
        
        return lst