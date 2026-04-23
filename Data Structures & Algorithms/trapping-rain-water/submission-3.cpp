class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> max_right(n,0);
        vector<int> max_left; 

        int curr = 0;
        for (int i=0; i<n-1; i++){
            curr=max(curr, height[i]);
            max_left.push_back(curr);
        }

        curr=0;
        for (int i=n-1; i>=0; i--){
            curr=max(curr, height[i]);
            max_right[i] = curr;
        }

        int ans=0;
        for (int i=1; i<n-1; i++){
            ans+=max(0, min(max_left[i], max_right[i]) - height[i]);
        }
        
        return ans;
        
    }
};
