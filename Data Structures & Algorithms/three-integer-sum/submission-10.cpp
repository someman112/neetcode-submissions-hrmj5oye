class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;


        for (int i=0; i<nums.size(); i++){
            if (i>0 && nums[i]==nums[i-1]) continue;

            int target = -nums[i];
            int p1 = i+1, p2 = nums.size()-1;

            while (p1 < p2){
                int curr = nums[p1] + nums[p2]; 
                if (curr < target) p1++;
                else if (curr > target) p2--;
                else {
                    ans.push_back(vector{nums[i], nums[p1], nums[p2]});

                    p1++;
                    while (p1<nums.size() && nums[p1]==nums[p1-1]) p1++;
                    p2--;
                    while (p2>=0 && nums[p2] == nums[p2+1]) p2--;
                }
            }
        }

        return ans;

        
    }
};