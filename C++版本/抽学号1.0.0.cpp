#include<bits/stdc++.h> 

using namespace std;

int main()

{

	while(1)	{

	cout<<"输入抽取人数";

	srand(unsigned(time(NULL)));

	int n,i,j,a[50],s;

	memset(a,0,sizeof(a));

	while(cin>>n) //这里的多组是为了让exe文件运行后仍不退出

	{	

		for(i=1;i<=n;i++)

		{

			s=floor(rand()%40+1);

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

			cout<<a[i]<<" "; 

		}

	}

	cout << " " << endl;

	}

	return 0;

}
