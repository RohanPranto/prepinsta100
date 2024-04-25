//Perfect Square
#include<bits/stdc++.h>
using namespace std;
void valid_perfectsq(long long n){
    if(sqrt(n))

    if(sqrt(n) - floor(sqrt(n)) == 0){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
}
int main(){
    long long n;
    
    cout<<"Enter a number ";
    cin>>n;
    valid_perfectsq(n);
}