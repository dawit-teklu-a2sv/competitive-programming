class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& q) {
        int n = arr.size();
        int prefix[n];
        prefix[0] = arr[0];
        for (int i = 1; i<n;i++)
            prefix[i] = prefix[i-1] ^ arr[i];
        
        vector<int> res;

        for(int i = 0; i<q.size();i++){
            int L = q[i][0];
            int R = q[i][1];
            if (L == 0)
                res.push_back(prefix[R]);
            else
                res.push_back(prefix[R] ^ prefix[L-1]);
        }
        return res;
    }
};