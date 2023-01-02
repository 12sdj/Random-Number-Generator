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
	cout << "Welcome to the Draw Number Machine/欢迎使用抽学号机器" << endl;
	cout << "Please select a language!/请选择语言:(Chinese or English Press 1 for Chinese and 2 for English)/选中文按1，选英文按2" << endl;
	cout << "如果按3，弹出相关信息/If you press 3, the relevant information will pop up" << endl;
	int L;
	cin >> L;
	if(L == 1)
	{
		system("title 抽学号");
		cout << "本产品按数字键执行，按任意字母键终止程序" << endl; 
		cout << "注：每次输入完人数后，过5秒将清除一次界面,请再次输入抽取到的人数量" << endl;
		int as;
		cout <<"输入总抽取人数：";
		cin >> as;
		cout<<"输入单次抽到人数总量：";
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
			cout << "如果想看到作者的更多作品或联系作者，请搜索：yueguangqishi1314@outlook.com" << endl;
			usleep(500000);
			cout << "本产品由作者King34/caijinyuan123在没有团队协助的情况下发明。欢迎下次使用！再见！并且本产品具有 MIT 许可证，不用于商业用途" << endl;
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
