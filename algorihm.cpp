
#include <iostream>
using namespace std;

int Search(int arr[],int size,int num);


void Sort(int arr[],int size);
int binary_search(int arr[],int size,int num);


int main(){
int size;
int num;
cout<<"enter the size of array"<<endl;
   cin>>size;
int arr[size];
cout<<"enter array elements"<<endl;
for(int i=0;i<size;i++){
	cout<<"enter element "<<i+1<<endl;
   	   cin>>arr[i];
}
int Choice;
cout<<"for searching enter 1 sorting 2 binary search 3"<<endl;
cin>>Choice;
if(Choice==1){
  cout<<"enter the number to be searched"<<endl;
	cin>>num;
if(Search(arr,size,num)==-1){
	cout<<"not found";}else{
cout<<"found at index "<<Search(arr,size,num)<<endl;
}


}
else if(Choice==2){
Sort(arr,size);
}

else if(Choice==3){

  cout<<"enter the number to be searched"<<endl;
	cin>>num;
if(Search(arr,size,num)==-1){
	cout<<"not found";}else{
cout<<"found at index "<<binary_search(arr,size,num)<<endl;
}


}






}





void Sort(int arr[],int size){




for(int i=0;i<size;i++){

for(int j=i+1;j<size;j++){
if(arr[i]>arr[j]){
int temp;
temp=arr[i];
arr[i]=arr[j];
arr[j]=temp;
}
}
}


for(int i=0;i<size;i++){
cout<<arr[i]<<" ";
}
}


int Search(int arr[],int size,int num){
int index;
for(int i=0;i<size;i++){
if(arr[i]==num){
return i;
}

}
return -1;

}






int binary_search(int arr[],int size,int num){



int k=0;


for(int i=0;i<size;i++){

for(int j=i+1;j<size;j++){
if(arr[i]>arr[j]){
int temp;
temp=arr[i];
arr[i]=arr[j];
arr[j]=temp;
}
}
}
int top=size;
int bottom =0;
int middle=size/2;

while(top>=bottom){

if(arr[middle]==num){
return middle;
break;
}
else if(arr[middle]>num){
top=middle-1;
middle=top/2;

}
else{
bottom=middle+1;
middle=(top+bottom)/2;
}

size/=2;
}



return -1;}










