#include <iostream>

using namespace std;

int main(){

    int n,rem;
    cout<<"Enter a number ";
    cin>>n;
    int rev= 0;
    while(n!=0){
        rem=n%10; //digit count
        rev=rev*10+rem; //reverse number
        n/=10;
    }

    cout<<rev;
}