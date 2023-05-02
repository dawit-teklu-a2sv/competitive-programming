class Solution {
public:
    int arraySign(vector<int>& nums) {
        
        for(auto it: nums)
            if(it == 0)
                return 0;
        for(int i = 0; i < nums.size();i++){
            if (nums[i] <0)
                nums[i] = -1;
            else
                nums[i] = 1;
        }
        int initialProduct = 1;
        return accumulate(nums.begin(),nums.end(),initialProduct,multiplies<int>());
        
    }
};