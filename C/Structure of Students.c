#include <stdio.h>
#include <stdlib.h>
#include<string.h>
typedef struct {

char name[30];
int age;
int markss[3];


}details;
details*detailsEnter(int age_1,char*name,int*marks);
void main(){
char student_22[30]="Yaseen";
char student_11[30]="Islam";
int marksss_11[3]={10,20,30};
int marksss_22[3]={8,20,27};
details *student_2;
details *student_1;
student_2=detailsEnter(18,student_22,marksss_22);
student_1=detailsEnter(19,student_11,marksss_11);
printf("name : %s",student_1->name);
printf("\nage : %d\n",student_1->age);
for(int i=0;i<3;++i)
{
printf("mark_%d : %d\n",i+1,student_1->markss[i]);
}
printf("\nname : %s",student_2->name);
printf("\nage : %d\n",student_2->age);
for(int i=0;i<3;++i)
{
printf("mark_%d : %d\n",i+1,student_2->markss[i]);
}

}
details*detailsEnter(int age_1,char*name,int*marks)
{
details*std_1=malloc(sizeof(details));
strcpy(std_1 ->name,name);
std_1->age=age_1;
for(int i=0;i<3;++i)
std_1->markss[i]=marks[i];

}