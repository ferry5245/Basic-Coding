#include<stdio.h>

//void urutan(int a[],b)
//{
//	f_urut=fopen("Tinggi.txt","rb");
//	int c=0,d,x=0;
//	while(fread(&a,sizeof(a),1,f_urut)==1)
//	{
//		if(a[c]!=a[c-1]) x=1;
//	}
//} 

void main()
{
	
	int temp,tinggi[1000];
	int a,b,i,j,n,x=-1;
	printf("Jumlah Siswa (Min 2, Maks 1000): ");scanf("%d",&n);
	
	if(n<2) printf("Maaf, Jumlah Siswa Tidak Mencukupi\n");
	else if(n>=2&&n<=1000)
	{
		for(i=0;i<n;i++)
		{
			printf("Tinggi Siswa %d : ",i+1);scanf("%d",&tinggi[i]);
		}
	}
	else printf("Maaf, Jumlah Siswa Melebihi Batas.\n");
	
	for(i=0;i<n;i++) printf("%d ",tinggi[i]);
	
	for(i=0;i<n;i++)
	{
		if(tinggi[i]==tinggi[i+1])
		{
			for(j=i-1;j<n;j++)
			{
				if(j<n-1&&tinggi[j]!=tinggi[j+1]) x=1;
			}
		}
		
	}
	if(x==1) printf("\nYA!\n");
	else printf("\nTIDAK!\n");
	
	if(x==1)
	{
		for(i=0;i<n;i++)
		{
			if(tinggi[i]==tinggi[i+1])
			{
				for(j=i;j<n-1;j++)
				{
					a=j;b=j+1;
					if(tinggi[a]==tinggi[b])
					{
						temp=b;
						b=a;
						a=temp;
						break;
					}
				}
			}
		}
	}

	for(i=0;i<n;i++) printf("%d ",tinggi[i]);
}
