#include <set>
#include <list>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::set <int> ok;
        for(int i=0;i<nums.size();i++){
            ok.insert(nums[i]);
        }
        for(int i=0;i<nums.size();i++){
            if(ok.contains(target-nums[i])){
                for(int j=0;j<nums.size();j++){
                    if(i!=j && target-nums[i]==nums[j]){
                        return {i,j};
                    }
                }
            }
        }
    }
};
