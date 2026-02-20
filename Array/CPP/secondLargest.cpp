#include<bits/stdc++.h>
using namespace std;


// #brute method
int secondLargest(vector<int>& arr){
    sort(arr.begin(), arr.end());
    int largest = arr[arr.size()-1];
    int secondLarge;
    for(int i = arr.size() - 1; i>= 0; i--){
        if(arr[i] != largest){
            secondLarge = arr[i];
            break; 
        }
    }
}

// # optimal Solution

int secondLargestO(vector<int>& arr){
    int largest = arr[0];
    for (int i = 0; i<= arr.size()-1; i++){
        if (arr[i] > largest && arr[i] != largest){
            largest = arr[i];
            // cout << largest;
        }
    }
    return largest;
}

int main(){
    vector<int> arr1 = {1, 4, 2, 5, 2};
    cout << secondLargestO(arr1);
    return 0;
}