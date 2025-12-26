class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        if(n<k) return -1;

        double curr_sum = 0;
        for(int i=0;i<k;i++){
            curr_sum += nums[i];
        }
        double curr_avg = curr_sum/k;
        double max_avg = curr_avg;
        for(int i = k;i<n;i++){
            curr_sum = curr_sum - nums[i-k] + nums[i];
            curr_avg = curr_sum/k;
            max_avg = max(max_avg, curr_avg); 
        }
        return max_avg;
    }
};