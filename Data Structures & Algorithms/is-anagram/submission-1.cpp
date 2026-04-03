#include <set>
#include <string>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()){
            return false;
        }
        int hast[27] = {0};
        for(int i=0;i<s.length();i++){
            int x = s[i]-'a';
            hast[x] += 1;
        }
        for(int i=0;i<t.length();i++){
            int y = t[i]-'a';
            hast[y] -= 1;
        }
        for(int i=0;i<27;i++){
            if(hast[i]!=0){
                return false;
            }
        }
        return true;
    }
};
