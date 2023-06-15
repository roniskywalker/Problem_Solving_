//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution {
  public:
    void up(int n){
    for(int i=0;i<n;i++){

    
    for(int j=0;j<n-i;j++){
        cout<<"*";
    }
    for(int j=0;j<2*i;j++){
        cout<<" ";
    }
    for(int j=0;j<n-i;j++){
        cout<<"*";
    }
    cout<<endl;
    }
}
void down(int n){

    for(int i=1;i<=n;i++){
    for(int j=0;j<i;j++){
        cout<<"*";
    }

    for(int j=0;j<2*n-2*(i);j++){
        cout<<" ";
    }

    for(int j=0;j<i;j++){
        cout<<"*";
    }
    cout<<endl;
}
}


    void printTriangle(int n) {
        up(n);
        down(n);
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
        ob.printTriangle(n);
    }
    return 0;
}
// } Driver Code Ends