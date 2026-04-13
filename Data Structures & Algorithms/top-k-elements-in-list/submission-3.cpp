class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        for(int i: nums) freqs[i]++;

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minheap;

        for (const auto& [key,value]: freqs){
            minheap.push({value, key});
            if(minheap.size()>k) minheap.pop();
        }

        vector<int> res;

        while (!minheap.empty()){
            res.push_back(minheap.top().second);
            minheap.pop();
        }

        return res;
        
    }
};
