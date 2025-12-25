class Solution {
public:
    void rotateArray(vector<int>& arr, int start, int end){
        int temp;
        while(start<end){
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++,end--;
        }
    }
    void rotate(vector<int>& arr, int k) {
        int n = arr.size();
        k = k%n;
        rotateArray(arr,0,n-1);
        rotateArray(arr,0,k-1);
        rotateArray(arr,k,n-1);
    }
};