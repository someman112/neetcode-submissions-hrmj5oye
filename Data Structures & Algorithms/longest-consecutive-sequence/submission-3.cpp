#include <ranges>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        auto num_set = nums | views::as_rvalue | ranges::to<unordered_set>();
        int ans = 0;
        for (int n: num_set){

            if (!num_set.contains(n-1)){
                int curr_len=1;
                int curr_num = n+1;

                while (num_set.contains(curr_num)){
                    curr_len+=1;
                    curr_num+=1;
                }
                
                ans = max(ans, curr_len);
            }
        }

        return ans;
        
    }
};
