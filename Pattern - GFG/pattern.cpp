//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution {
  public:
    void printDiamond(int n) {
        for(int i=1;i<=n;i++){
            for(int j=n-i;j>0;j--){
                cout<<" ";
            }
            for(int k=0;k<i;k++){
                cout<<"*"<<" ";
            }
            cout<<endl;
        }
        for(int i=0;i<n;i++){
            for(int k=0;k<i;k++){
                cout<<" ";
            }
            for(int j=n-i;j>0;j--){
                cout<<"*"<<" ";
            }
            cout<<endl;
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        Solution ob;
        ob.printDiamond(n);
    }
    return 0;
}
// } Driver Code Ends