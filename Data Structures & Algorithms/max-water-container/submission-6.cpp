class Solution {
public:
    int maxArea(vector<int>& heights) {
        int p1 = 0, p2 = heights.size()-1;
        int ans=0;

        while(p1<p2){
            ans = max(ans, min(heights[p1], heights[p2]) * (p2-p1));

            if(heights[p1]<heights[p2]){
                p1++;
            }
            else{
                p2--;
            }
        }

        return ans;
        
    }
};
