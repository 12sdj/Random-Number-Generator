#include<stdio.h>
#include<windows.h>
#include<bits/stdc++.h>
#include<iostream>
#include<string>
#include<cstring>
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<time.h>
#include<unistd.h>
#include<cstdlib>
#include<conio.h>
#include<stdlib.h>
#define random(x) (rand()%x)
using namespace std;
int main()
{
	system("color F0");
	cout << "Welcome to the Draw Number Machine/��ӭʹ�ó�ѧ�Ż���" << endl;
	cout << "Please select a language!/��ѡ������:(Chinese or English Press 1 for Chinese and 2 for English)/ѡ���İ�1��ѡӢ�İ�2" << endl;
	cout << "�����3�����������Ϣ/If you press 3, the relevant information will pop up" << endl;
	int L;
	cin >> L;
	if(L == 1)
	{
		system("title ��ѧ��");
		cout << "����Ʒ�����ּ�ִ�У���������ĸ����ֹ����" << endl; 
		cout << "ע��ÿ�������������󣬹�5�뽫���һ�ν���,���ٴ������ȡ����������" << endl;
		int as;
		cout <<"�����ܳ�ȡ������";
		cin >> as;
		cout<<"���뵥�γ鵽����������";
		srand(unsigned(time(NULL)));
		int n,i,j,a[50],s;
		memset(a,0,sizeof(a));
			while(cin>>n)
			{	
				for(i=1;i<=n;i++)
				{
					s=floor(rand()%as+1);
					for(j=1;j<i;j++)
					if(s==a[j]) s=0;
					if(s==0)
					{
						i--;
					}
					else
					{
						a[i]=s;
					}
				}
				for(i=1;i<=n;i++)
				{ 
					cout<< a[i] << " ";
				}
				cout << " " << endl;
				Sleep(5000);
				system("cls");
				
			}
			cout << "����뿴�����ߵĸ�����Ʒ����ϵ���ߣ���������yueguangqishi1314@outlook.com" << endl;
			usleep(500000);
			cout << "����Ʒ������King34/caijinyuan123��û���Ŷ�Э��������·�������ӭ�´�ʹ�ã��ټ������ұ���Ʒ���� MIT ���֤����������ҵ��;" << endl;
			usleep(3000000);
			cout << " "; 
		} 
	if(L == 2)
	{
		system("title Draw number");
		cout << "This product is executed by pressing the number keys and any letter key to terminate the program" << endl;
		cout << "Note: After entering the number of people each time, the screen will be cleared once in 5 seconds, please enter the number of people drawn again" << endl;
		int as;
		cout <<"Enter the total number of people drawn:";
		cin >> as;
		cout<<"Enter the total number of people drawn in a single draw:";
		srand(unsigned(time(NULL)));
		int n,i,j,a[50],s;
		memset(a,0,sizeof(a));
			while(cin>>n)
			{	
				for(i=1;i<=n;i++)
				{
					s=floor(rand()%as+1);
					for(j=1;j<i;j++)
					if(s==a[j]) s=0;
					if(s==0)
					{
						i--;
					}
					else
					{
						a[i]=s;
					}
				}
				for(i=1;i<=n;i++)
				{
					cout << a[i] << " ";
				}
				cout << " " << endl;
				Sleep(5000);
				system("cls");
			}
		cout << "If you would like to see more of the author's work or contact the author, please search: yueguangqishi1314@outlook.com" << endl;
		usleep(500000);
		cout << "This product was invented by the author King34/caijinyuan123 without team assistance. Welcome to use it next time! Good bye! And this product has an MIT license and is not for commercial use" << endl;
		usleep(1000000);
		cout << " ";
	}
	if(L == 3)
	{
		cout << "If you would like to see more of the author's work or contact the author, please search: yueguangqishi1314@outlook.com" << endl;
		usleep(500000);
		cout << "This product was invented by the author King34/caijinyuan123 without team assistance. Welcome to use it next time! Good bye! And this product has an MIT license and is not for commercial use" << endl;
		usleep(3000000);
		cout << " ";
		return 0; 
	}
	return 0;
}
