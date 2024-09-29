class Solution {
public:
    long long int mySqrt(int x) {
        int s = 0, e = x;
        long long int ans = -1;
        long long int mid;
        while(s<=e){
            mid = s+ (e-s)/2;
            long long int sq = mid*mid;
            if(sq == x){
                return mid;
            }
            else if(sq < x){
                ans = mid; 
                s = mid +1;
            }
            else{
                e = mid -1;
            }
        }
        return ans;
    }
};