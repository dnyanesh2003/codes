#include<iostream>
using namespace std;
const int max_size=10;

class CircularQ{
    private:
    int rear;
    int front,count;
    int orders[max_size];
    public:
    bool isEmpty(){
        return ;
    }

    bool isFull(){
        return ;
    }
    void enqueue(int order_no){
        if(isFull()){
            cout<<"Queue is full.order cannot accept";
            return;
        }
        if(isEmpty()){
            front=rear=0;
        }
        else{
            rear=(rear+1)% max_size;
        }
        orders[rear]=order_no;
        count++;
        cout<<"Order"<<orders[rear]<<" is placed successfully....";
    }
    void dequeue(){
        if(isEmpty()){
            cout<<"Queue is empty...";
            return;
        }
        int serve_order=orders[front];
        if(front==rear){
            front=rear=-1;
        }
        else{
            front=(front+1)%max_size;
        }
        count--;
        cout<<"Order "<<serve_order<<" is served...";
    }
        void displayQueue() {
        if (isEmpty()) {
            cout << "Queue is empty.\n";
            return;
        }

        int i = front;
        do {
            cout << "Order " << orders[i] << " ";
            i = (i + 1) % max_size;
        } while (i != (rear + 1) % max_size);
        cout << endl;
    }
};
int main(){
    int m;
    cout<<"Enter max orders : ";
    cin>>m;
    int ch;
    CircularQ Q;
    do{
        cout << "\n1. Place an order\n";
        cout << "2. Serve an order\n";
        cout << "3. Display orders\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> ch;
        switch (ch) {
            case 1: {
                if (Q.isFull()) {
                    cout << "Cannot accept more orders. Queue is full.\n";
                } else {
                    int orderNumber;
                    cout << "Enter the order number: ";
                    cin >> orderNumber;
                    Q.enqueue(orderNumber);
                }
                break;
            }
            case 2:
                Q.dequeue();
                break;
            case 3:
                Q.displayQueue();
                break;
            case 4:
                cout << "Exiting the program.\n";
                break;
            default:
                cout << "Invalid choice. Please enter a valid option.\n";
        }
    } while (ch != 4);
    return 0;

}