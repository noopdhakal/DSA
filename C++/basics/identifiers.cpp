#include <iostream>

using namespace std;

class Car{
    string Brand;
    string model;
    int year;
};


void getSum(int a, int b){
    int _sum = a + b;
    cout << "The sum is " << _sum;
}

int main(){
    int studentAge = 20;
    double accountBalance = 1000.50;
    string student_name = "Anup";

    getSum(2, 10);

    return 0;
}