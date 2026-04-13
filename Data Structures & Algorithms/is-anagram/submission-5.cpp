class Solution {
public:
    bool isAnagram(string s, string t) {
                if (s.length()!=t.length()) return false;
        vector<int> freqs(26,0);

        for(int i=0; i<s.length(); i++){
            freqs[s[i] - 'a']++;
            freqs[t[i] - 'a']--;
        }
        for(int i: freqs){
            if (i!=0) return false;
        }

        return true;
    }
    
};
