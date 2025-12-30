class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size(); // 6 5 5 
        int vote = 0;
        int candidate = 0;
        for(int i=0;i<n;i++){
            if(vote==0){ // 0
                candidate = nums[i]; //   can = 6
                vote++; // 1
            }
            else if(vote != 0){
                if(candidate == nums[i]){  //  6 != 5
                    vote++; // 
                }
                else{
                    vote--;
                }
            }
        }
        return candidate;
    }
};