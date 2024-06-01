//Fibonacci Series upto nth term
#include <iostream>
using namespace std;
int main(){
    cout<<"Enter the number of terms: ";
    int n;
    cin>>n;
    int a=0, b=1;
    for(int i=0; i<n; i++){
        cout<<a<<" ";
        int c=a+b;
        a=b;
        b=c;
    }
    return 0;
}
