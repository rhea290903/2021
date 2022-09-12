#include<stdio.h>
#include<string.h>
#include"EVMSAMPLE.h"
int main()
{
    int ch;
    do
    {
        

        
        printf("                                  WELCOME TO VOTING SYSTEM                                                      \n");
        printf("*------*------*------*------*------*------*------*------*------*------*------*------*------*------*------*----*\n");
        printf("|                                       1.Admin Login                                                         |\n");
        printf("|                                   2.Voter Login and Voting                                                  |\n");
        printf("|                                       3.View Results                                                        |\n");
        printf("|                                   4.Exit Voting Sysytem                                                     |\n");
        printf("*------*------*------*------*------*------*------*------*------*------*------*------*------*------*------*----*\n");
        printf("YOUR CHOICE");
        scanf("%d",&ch);
        int n;
        switch(ch){
            case 1:
                adminlogin();
            break;
            case 2:
                verify();
            break;
            case 3:
                
                printf("1.president\n2.vice president\n3.sports head\n");
                scanf("%d",&n);
                if(n==1){
                FILE *fp1;
                fp1=fopen("president.txt","w");
                sort(fp1);
                }
                else if(n==2){
                FILE *fp1;
                fp1=fopen("vicepresident.txt","w");
                sort(fp1);

                }
                else if(n==3){
                FILE *fp1;
                fp1=fopen("sportshead.txt","w");
                sort(fp1);
                }
                else{
                printf("exit");
                }

                
            break;
            case 4:
            printf("\n");
            default:
            printf("\nthankyou");
            break;
        }
    }while(ch!=4);
    return 0;
}
