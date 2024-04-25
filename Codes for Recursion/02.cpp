//user will give input and system will check if the number is prime or not.
#include<iostream>
using namespace std;

int main(){
    int i,n;
    cout<<"Enter a number: ";
    cin>>n;
    for(i=2; i<n; i++){
        if(n%i==0){
            cout<<"Non-prime"<<endl;
            break;
        }
    }
        if(i==n){ //if i runs till n number, means it has no other factor than 1 and itself n.
            cout<<"Prime"<<endl; //so it is prime.
            
        }

        if(n==1){
            cout<<"1 is neither prime nor composite."<<endl;
        }
    return 0;
    } 