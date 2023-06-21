//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
//User function template for C++
class Solution{
public:

	void rearrange(int arr[], int n) {
	    vector<int>pos;
	    vector<int>neg;
	    
	    for(int i= 0; i< n; i++){
	        if (arr[i]<0)
	            neg.push_back(arr[i]);
	        else
	            pos.push_back(arr[i]);
	    }
	    if (pos.size()>neg.size()){
    	    for(int j=0; j<neg.size(); j++){
    	        arr[2*j]=pos[j];
    	        arr[2*j+1]=neg[j];
    	    }
    	    int index = neg.size()*2;
    	    for (int k = neg.size(); k < pos.size();k++)
    	        arr[index++] = pos[k];
	    }
	    else{
	        for(int j=0; j<pos.size(); j++){
    	        arr[2*j]=pos[j];
    	        arr[2*j+1]=neg[j];
    	    }
    	    int index = pos.size()*2;
    	    for (int k = pos.size(); k < neg.size();k++)
    	        arr[index++] = neg[k];
	    }
	}
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int arr[n];
        for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        ob.rearrange(arr, n);
        for (i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends