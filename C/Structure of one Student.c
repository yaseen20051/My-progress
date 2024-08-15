#include <stdio.h>
#include <stdlib.h>

typedef struct {

char name[30];
int age;
int marks[3];


}details;
void detailsEnter(details *std);
void main(){
details student_1;
detailsEnter(&student_1);
printf("name : %s",student_1.name);
printf("\nage : %d\n",student_1.age);
for(int i=0;i<3;++i)
{
printf("mark_%d : %d\n",i+1,student_1.marks[i]);
}

}
void detailsEnter(details *std_1)
{
printf("name : ");
gets(std_1->name);
printf("age : ");
scanf("%d",&std_1->age);
for(int i=0;i<3;++i)
{
printf("mark_%d : ",i+1);
scanf("%d",&std_1->marks[i]);
}
}