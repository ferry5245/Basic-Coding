#include<stdio.h>
#include<string.h>

int input,i,x;

struct custaccount{
	char uname[99],pwd[99],name[99],born[99],gender[99],address[99];
	int age,number;
}custacc;

char uname[99],pwd[99];

void adminlogin();
void adminmenu();
void customer();
void custregis();
void custlogin();
void header();

FILE *f_akuncust;


int main()
{
	header();
	printf("==== MAIN MENU ====\n\n");
	printf("1. Admin\n2. Customer\n3. Exit\n\n");
	printf("Choose Menu : ");scanf("%d",&input);getchar();
	switch(input)
	{
		case 1 : 
			{
				system("cls");
				i=2;
				adminlogin();
				break;
			}
		case 2 : 
			{
				system("cls");
				customer();
				break;
			}
		case 3 : 
			{ 
				system("cls");
				header();
				printf("Come back again");
				getchar();
				break;
			}
		default : 
			{
				system("cls");
				header();
				printf("Menu not available\n\n   Program Terminated");
				getchar();
				break;
			}
	}
	return 0;
}

void header()
{
	printf("	BBBBBB          AAAA        NNN     NNN  KKK   KKK\n");
	printf("	BBB BBB        AAAAAA       NNN NN  NNN  KKK  KKK\n");
	printf("	BBB  BBB      AAA  AAA      NNN  NN NNN  KKK KKK\n");
	printf("	BBBBBBB      AAA    AAA     NNN   NNNNN  KKKKKK\n");
	printf("	BBB  BBB    AAAAAAAAAAAA    NNN    NNNN  KKK KKK\n");
	printf("	BBB BBB    AAA        AAA   NNN     NNN  KKK  KKK\n");
	printf("	BBBBBB    AAA          AAA  NNN     NNN  KKK   KKK\n\n");
	printf("\t==================================================\n");
	printf("\t============== WELCOME TO THE BANK ===============\n");
	printf("\t==================================================\n\n");
}

void adminlogin()
{
	header();
	char admunm[99],admpwd[99];
	printf("==== ADMIN LOGIN ====\n\n");
	printf("  Username\t: ");gets(admunm);
	printf("  Password\t: ");gets(admpwd);
	if(i>0&&strcmp(admunm,"admin")==0&&strcmp(admpwd,"1234")==0)
	{
		printf("\n==== LOGIN SUCCESSFUL ====\n");
		getchar();
		system("cls");
	}
	else if(i>0)
	{
		printf("\n===== LOGIN FAILED ====\n");
		getchar();
		i--;
		system("cls");
		adminlogin();
	}
	else
	{
		printf("\nSorry, too many failed attempt\nReturning to Main Menu\n");
		getchar();
		system("cls");
		main();
	}
	getchar();
}

void adminmenu()
{
	header();
	printf("==== ADMIN MENU ====\n\n");
	printf("1. Customer's Deposit'\n2. Customer's Gold Investment\n3. Gold Price List'\n4. Return to main menu\n\n");
	printf("Choose Menu : ");scanf("%d",&input);getchar();
	switch(input)
	{
		case 1: 
		{
			
		}
	}
}

void customer()
{
	header();
	printf("Choose the Menu below\n\n");
	printf("1. Registration\n2. Login\n3. Return to Main Menu\n\n");
	printf("Choose Menu : ");scanf("%d",&input),getchar();
	switch(input)
	{
		case 1 : 
			{
				system("cls");
				custregis();
				break;
			}
		case 2 : 
			{
				system("cls");
				i=3;
				custlogin();
				break;
			}
		case 3 : 
			{ 
				system("cls");
				main();
				getchar();
				break;
			}
		default : 
			{
				system("cls");
				header();
				printf("Menu not available\n\n   Program Terminated");
				getchar();
				break;
			}
	}
}

void custregis()
{
	char yn;
	header();
	printf("====Account Registration====\n\n");
	
	f_akuncust=fopen("AkunMember.txt","ab");

	printf("Username\t\t: ");gets(custacc.uname);
	printf("Password\t\t: ");gets(custacc.pwd);
	printf("\n---BIODATA---\n\n");
	printf("Full Name\t\t: ");gets(custacc.name);
	printf("Born Place & Date\t: ");gets(custacc.born);
	printf("Sex\t\t\t: ");gets(custacc.gender);
	printf("Address\t\t\t: ");gets(custacc.address);
	printf("Age\t\t\t: ");scanf("%d",&custacc.age);
	printf("Phone Num\t\t: ");scanf("%d",&custacc.number);getchar();
	fwrite(&custacc,sizeof(custacc),1,f_akuncust);
	printf("\n---Registration Successful---\n");
	fclose(f_akuncust);
	printf("Do you want to head to Login Section? (y/n)\n");scanf("%c",&yn);getchar();
	if(yn=='y')
	{
		system("cls");
		i=3;
		custlogin();
	}
	else if(yn=='n')
	{
		system("cls");
		customer();
	}
	else 
	{
		printf("Invalid Selection\n");
		system("cls");
		getchar();
	}
}

void custlogin()
{
	header();
	printf("====Login Section====\n\n");
	printf("Username\t: ");gets(uname);
	printf("Password\t: ");gets(pwd);
	x=0;
	f_akuncust=fopen("AkunMember.txt","rb");
	while(fread(&custacc,sizeof(custacc),1,f_akuncust)==1)
	{
		if(strcmp(uname,custacc.uname)==0&&strcmp(pwd,custacc.pwd)==0)
		{
			x==1;
			break;
		}
	}
	fclose(f_akuncust);
	if(x==1)
	{
		printf("Login Successful");
		getchar();
		system("cls");
		//custmenu();
	}
	else
	{
		i--;
		if(i>0) 
		{
			printf("Login Failed, Try Again (Chances = %d)",i);
			getchar();
			system("cls");
			custlogin();
		}
		else
		{
			printf("---Login Failed---\n   Sorry, Out of chances, returning to main menu\n\n");
			getchar();
			system("cls");
			main();
		}
	}
}
