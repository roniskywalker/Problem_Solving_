//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;
#define ll long long

// } Driver Code Ends
// #define ll long long
class Solution{
public:
    vector<ll> nthRowOfPascalTriangle(int n) {
        vector <vector<ll>> v(n);
        long long mod = 1e9+7;
        for(int i = 0;i < n;i++){
            v[i].resize(i+1);
            v[i][0] = v[i][i] = 1;
            for(int j = 1;j < i;j++) v[i][j] = (v[i-1][j-1]+v[i-1][j])%mod;
        }   
        return v[n-1];
    }
};


//{ Driver Code Starts.


void printAns(vector<ll> &ans) {
    for (auto &x : ans) {
        cout << x << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        auto ans = ob.nthRowOfPascalTriangle(n);
        printAns(ans);
    }
    return 0;
}

// } Driver Code Ends