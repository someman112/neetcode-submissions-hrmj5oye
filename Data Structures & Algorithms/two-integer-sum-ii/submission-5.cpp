class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int p1 = 0, p2 = numbers.size()-1;
        int curr = 0;

        while (p1<p2){
            curr = numbers[p1] + numbers[p2];

            if (curr<target) p1++;
            else if (curr>target)p2--;
            else break;
        }

        return vector{p1+1, p2+1};
        
    }
};
