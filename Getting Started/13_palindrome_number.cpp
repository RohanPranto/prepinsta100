#include<bits/stdc++.h>
using namespace std;
 
int main(){
    int n;
    cin>>n;
    int rev=0;
    int rem;
    int temp=n;
    while(n!=0){
        rem=n%10; //digit count
        rev=rev*10+rem; //reverse number
        n/=10;
    }
    if(rev==temp){
        cout<<"Palindrome Number"<<endl;
    }
    else{
        cout<<"Not Palindrome Number"<<endl;
    }
}