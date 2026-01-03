class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        int n = x;
        long long revNum = 0;

        while(n>0){
            int temp = n%10;
            revNum = revNum*10 + temp;
            n /=10;
        }

        if(revNum == x){
            return true;
        }
        else{
            return false;
        }
    }
};