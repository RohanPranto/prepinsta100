//cpp code to find out Quadrants in which a given coordinate lies

#include <iostream>
using namespace std;

int main(){
    int x, y;
    cout<<"Enter the x coordinate: ";
    cin>>x;
    cout<<"Enter the y coordinate: ";
    cin>>y;

    if(x>0 && y>0){
        cout<<"The coordinate lies in the First Quadrant";
    }else if(x<0 && y>0){
        cout<<"The coordinate lies in the Second Quadrant";
    }else if(x<0 && y<0){
        cout<<"The coordinate lies in the Third Quadrant";
    }else if(x>0 && y<0){
        cout<<"The coordinate lies in the Fourth Quadrant";
    }else if(x==0 && y==0){
        cout<<"The coordinate lies at the Origin";
    }else if(x==0){
        cout<<"The coordinate lies on the Y-axis";
    }else{
        cout<<"The coordinate lies on the X-axis";
    }
    return 0;
}