#include<iostream>
using namespace std;

int size = 1000;

class Stack{
    public:
    int pos = -1;
    char arr[1000];
    void push(char a){
        if(a==' '){
            return;
        }
        pos++;
        arr[pos] = tolower(a);
    }
    char pop(){
        return arr[pos--];
    }
    char top(){
        return arr[pos];
    }
    void showData(){
        int temp = pos;
        while(temp!=-1){
            cout<<arr[temp]<<" ";
            temp--;
        }
    }
};

void check(string temp,Stack st){
    for(int i = 0;i<temp.size();i++){
        if(temp[i]!=st.pop()){
            cout<<"Not a plaindrome"<<endl;
            return;
        }
    }
    cout<<"Is is a palindrome"<<endl;
}

int main(){
    Stack st;
    string str = "poor dan is in a droop";
    string temp = "";
    for(int i = 0; i <str.size();i++){
        if(str[i]==' ') continue;
        temp+= tolower(str[i]);
    }
    for(int i = 0;i<temp.length();i++){
        st.push(temp[i]);
    }
    check(temp,st);
}
