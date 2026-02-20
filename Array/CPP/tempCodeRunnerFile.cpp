#include<bits/stdc++.h>
using namespace std;

int secondLargest(vector<int>& arr){
    sort(arr.begin(), arr.end());
    return arr[arr.size()-1];
}

int main(){

    vector<int> arr1 = {1, 4, 2, 5, 2};
    cout << secondLargest(arr1);
    return 0;
}