class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        if(n == 0) return 0;
        int start = 0, end = n-1;
        while(start < end){
            if(nums[start] == val){
                swap(nums[start], nums[end--]);
            }
            else{
                start++;
            }
        }
        if(nums[start] == val) return start;
        else return end+1;

    }
};