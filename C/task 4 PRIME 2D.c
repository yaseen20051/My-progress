#include <stdlib.h>
#include <stdio.h>
int Count (int n, int m, int a[n][m]);
int checkPrime(int Number);
int main ()
{

int rows=0,columns=0,i=0,j=0,counter=0;
while (rows<=0)
{
printf("enter no.of Rows :");
scanf("%d",&rows);}

while (columns<=0)
{
printf("enter no.of columns :");
scanf("%d",&columns);}
int *p=malloc(sizeof(int)*rows*columns);

for(i=0;i<rows;++i)
{for(j=0;j<columns;++j)
{printf("element[%d][%d]= ",i,j);
scanf("%d",(p+counter));
++counter;
}
}
int noOfprimes=Count (rows, columns,p);
printf("\nnoOfprimes=%d",noOfprimes);
}
int Count (int n, int m, int a[n][m])
{int prime=0,counterPrime=0,j=0;
for(int i=0;i<n;++i)
{
for (j=0;j<m;++j)
{
prime=checkPrime(a[i][j]);

if (prime)
{++counterPrime;}
}
}
return counterPrime;


}
int checkPrime(int Number)
{
int i=2;
if(Number<=1)
{return 0 ;}
if(Number==2)
{return 1 ;}
for(i;i<Number;++i)
{
if(Number%i==0)
{return 0;}
}
return 1;
}
