#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct vdetails{
    
    char ID[5];
    char vname[20];
    
}vd;
typedef struct candidate{
    
    int age;
    char name[20];
    char dob[20];
    char email[20];
    int votes;
    char check[3];
}candidate;
void voterdetails(){
    vd *s;
    int n,i,found=0;
    FILE *fp,*fp1;

    printf("how many candidates you want to enter");
    scanf("%d",&n);
    s=(vd*)calloc(n,sizeof(vd));
    fp=fopen("data.txt","a");
    for(i=0;i<n;i++){
        printf("enter candidate ID:");
        scanf("%s",s[i].ID);
        fflush(stdin);
        printf("enter candidate name:");
        scanf("%s",s[i].vname);
        fwrite(&s[i],sizeof(vd),1,fp);
        }
    
    fclose(fp);

}
void result(FILE *fp){
    candidate *s,s1;   
    int i;       
    fread(&s[0],sizeof(candidate),1,fp);           
    printf("THE WINNER IS: %s",s[0].name);
}
void sort(FILE *fp){
    candidate *s,s1;
    int i,j,found=1;
    fseek(fp,0,SEEK_END);
    int n=ftell(fp)/sizeof(candidate);
    s=(candidate*)calloc(n,sizeof(candidate));
    rewind(fp);
    for(i=0;i<n;i++){
        fread(&s[i],sizeof(candidate),1,fp);
    }
    
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            if(s[i].votes<s[j].votes){
                s1=s[i];
                s[i]=s[j];
                s[j]=s1;
            }

        }
    }
    fclose(fp);
    for(i=0;i<n;i++){
        fwrite(&s[i],sizeof(candidate),1,fp);
        
    }
    fclose(fp);
    if(found==1){
        result(fp);
    }
    else{
        printf("no result");
    }

}

void vote(FILE *fp){
    candidate s1;
    char name[20];
    FILE *fp1;
    int id,found=0;
    while(fread(&s1,sizeof(candidate),1,fp)){
        printf("\nname= %s\n",s1.name);
    }
    fclose(fp);
    fp1=fopen("temp.txt","w");
    printf("enter the candidate name you want to vote for");
    scanf("%s",name);
    while(fread(&s1,sizeof(candidate),1,fp)){
        if(strcmp(s1.name,name)==0){
            found=1;
            fflush(stdin);
            s1.votes+=1;
            
        }
        fwrite(&s1,sizeof(candidate),1,fp1);
    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1=fopen("temp.txt","r");
        while(fread(&s1,sizeof(candidate),1,fp1)){
            fwrite(&s1,sizeof(candidate),1,fp);
        }

        fclose(fp);
        fclose(fp1);

    }
    

}
void verify(){
    vd s2;
    FILE *fp2;
    int found,n;
    char id[5];
    printf("enter voter id:");
    scanf("%s",id);
    fp2=fopen("data.txt","r");
    
    while(fread(&s2,sizeof(vd),1,fp2)){
        
        if(strcmp(s2.ID,id)==0){
            found=1;

            


        }
        
    }
    fclose(fp2);
    
    if(found==1){
        printf("1.president\n2.vice president\n3.sports head\n");
        scanf("%d",&n);
        if(n==1){
        FILE *fp1;
        fp1=fopen("president.txt","w");
        vote(fp1);
        }
        else if(n==2){
        FILE *fp1;
        fp1=fopen("vicepresident.txt","w");
        vote(fp1);
        }
        else if(n==3){
        FILE *fp1;
        fp1=fopen("sportshead.txt","w");
        vote(fp1);
        }
        else{
        printf("exit");
        }

        
    }
    else{
        printf("not found");
    }

    
}
void create(FILE *fp)
{
    candidate *s;
    int n,i,found=0;
    printf("how many candidates you want to enter");
    scanf("%d",&n);
    s=(candidate*)calloc(n,sizeof(candidate));
    for(i=0;i<n;i++){
        printf("enter candidate age:");
        scanf("%d",&s[i].age);
        fflush(stdin);
        printf("enter candidate name:");
        scanf("%s",s[i].name);
        printf("enter candidate DOB:");
        scanf("%s",s[i].dob);
        printf("enter candidate phone number:");
        scanf("%s",s[i].email);
        fwrite(&s[i],sizeof(candidate),1,fp);
        }
    
    fclose(fp);
    

        

}
void display(FILE *fp){
    candidate s1;
    while(fread(&s1,sizeof(candidate),1,fp)){
        printf("\nage= %d\nname= %s\nDOB= %s\nEmail= %s\n",s1.age,s1.name,s1.dob,s1.email);
    }
    fclose(fp);

}
void update(FILE *fp){
    candidate s1;
    FILE  *fp1;
    char name[20];
    int found;
    fp1=fopen("temp.txt","w");
    printf("enter the name to update:");
    scanf("%s",name);
    while(fread(&s1,sizeof(candidate),1,fp)){
        if(strcmp(s1.name,name)==0){
            found=1;
            printf("enter new candidate age:");
            scanf("%d",&s1.age);
            fflush(stdin);
            printf("enter candidate DOB:");
            scanf("%s",s1.dob);
            printf("enter candidate phone number:");
            scanf("%s",s1.email);

        }
        fwrite(&s1,sizeof(candidate),1,fp1);
    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1=fopen("temp.txt","r");
        while(fread(&s1,sizeof(candidate),1,fp1)){
            fwrite(&s1,sizeof(candidate),1,fp);
        }
        fclose(fp);
        fclose(fp1);
    }
    



}
void delete1(FILE *fp){

    candidate s1;
    FILE  *fp1;
    char name[20];
    int found=0;
    fp1=fopen("temp.txt","w");
    printf("enter the name to delete:");
    scanf("%s",name);
    while(fread(&s1,sizeof(candidate),1,fp)){
        if(strcmp(s1.name,name)==0){
            found=1;
            

        }
        else{
            fwrite(&s1,sizeof(candidate),1,fp1);

        }
        
    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1=fopen("temp.txt","r");
        while(fread(&s1,sizeof(candidate),1,fp1)){
            fwrite(&s1,sizeof(candidate),1,fp);
        }

        fclose(fp);
        fclose(fp1);

    }


}
void adminlogin()
{

    char username[30];
    int password,ch,p,m;
    int n;
    printf("enter user name\n");
    scanf("%s",username);
    printf("enter password\n");
    scanf("%d",&password);
    if(strcmp(username, "Rhea") == 0&& password==34768)
    {
        do
        {
            printf("\n1.add record");
            printf("\n2.display record");
            printf("\n3.modify record");
            printf("\n4.delete record");
            printf("\n5.enter voter details");
            printf("\n enter 0 to come out of admin page");
    

            printf("\nenter choice:");
            scanf("%d",&ch);
            switch(ch)
            {
                case 1:
                printf("1.president\n2.vice president\n3.sports head\n");
                scanf("%d",&n);
                if(n==1){
                FILE *fp1;
                fp1=fopen("president.txt","w");
                create(fp1);
                }
                else if(n==2){
                FILE *fp1;
                fp1=fopen("vicepresident.txt","w");
                create(fp1);

                }
                else if(n==3){
                FILE *fp1;
                fp1=fopen("sportshead.txt","w");
                create(fp1);
                }
                else{
                printf("exit");
                }

                break;
                case 2:
                printf("1.president\n2.vice president\n3.sports head\n4.sports vice head\n");
                scanf("%d",&n);
                if(n==1){
                FILE *fp1;
                fp1=fopen("president.txt","r");
                display(fp1);
                }
                else if(n==2){
                FILE *fp1;
                fp1=fopen("vicepresident.txt","r");
                display(fp1);

                }
                else if(n==3){
                FILE *fp1;
                fp1=fopen("sportshead.txt","r");
                display(fp1);
                }
                else{
                printf("exit");
                }  
                                      
                break;
                case 3:
                printf("1.president\n2.vice president\n3.sports head\n4.sports vice head\n");
                scanf("%d",&n);
                if(n==1){
                FILE *fp1;
                fp1=fopen("president.txt","r");
                update(fp1);
                }
                else if(n==2){
                FILE *fp1;
                fp1=fopen("vicepresident.txt","w");
                update(fp1);

                }
                else if(n==3){
                FILE *fp1;
                fp1=fopen("sportshead.txt","w");
                update(fp1);
                }
                else{
                printf("exit");
                }  
                                 
                break;
                case 4:
                printf("1.president\n2.vice president\n3.sports head\n4.sports vice head\n");
                scanf("%d",&n);
                if(n==1){
                FILE *fp1;
                fp1=fopen("president.txt","w");
                delete1(fp1);
                }
                else if(n==2){
                FILE *fp1;
                fp1=fopen("vicepresident.txt","w");
                delete1(fp1);

                }
                else if(n==3){
                FILE *fp1;
                fp1=fopen("sportshead.txt","w");
                delete1(fp1);
                }
                else{
                printf("exit");
                }  
                                  
                
                
                        
                break;
                case 5:
                        voterdetails();
                default:
                printf("bye");
                break;
                
            }
        }while(ch!=0);
    }
}
                
                    

    
                    

