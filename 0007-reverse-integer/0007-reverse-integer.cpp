class Solution {
public:
    int reverse(int x) {
        bool flag = false;
        long long n = llabs((long long)x);   // 👈 changed line
        if(x < 0) flag = true;

        long long revNum = 0;
        while(n > 0){
            int d = n % 10;
            revNum = revNum * 10 + d;
            n /= 10;
        }

        if(flag) revNum = -revNum;
        if(revNum > INT_MAX || revNum < INT_MIN) return 0;
        return revNum;
    }
};
