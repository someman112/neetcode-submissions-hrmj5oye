class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> data;

        for (string s: strs){
            string t = s;
            sort(t.begin(), t.end());
            data[t].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& [key, value]: data){
            res.push_back(value);
        }

        return res;
    }
};
