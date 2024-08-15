#include <stdio.h>

#include <stdlib.h>

void main ()
{int counter=0,sum=0,stopCase=0;

int markSt[100],rank0=0,rank1=0,rank2=0,rank3=0,rank4=0;

while(stopCase!=-1)

{
scanf("%d",&markSt[counter]);
stopCase=markSt[counter];
if(markSt[counter]/20==0)
{rank0++;}
else if(markSt[counter]/20==1)
{rank1++;}
else if(markSt[counter]/20==2)
{rank2++;}
else if(markSt[counter]/20==3)
{rank3++;}
else if(markSt[counter]/20==4)
{rank4++;}
++counter;

}
printf("students of rank_0 = %d\n",rank0);
printf("students of rank_1 = %d\n",rank1);
printf("students of rank_2 = %d\n",rank2);
printf("students of rank_3 = %d\n",rank3);
printf("students of rank_4 = %d\n",rank4);
/**counter=0;
for(counter;counter<size;++counter)
{
printf("Element[%d] = %d\n",counter,arrayWrite[counter]);
}
counter=1;int maxElement=arrayWrite[0],place=0;
for (counter;counter<size;++counter)
{
if (arrayWrite[counter]>maxElement)
{
maxElement=arrayWrite[counter];
place=counter;
}
}
printf("sum=%d\nmaxElement is %d and in the index of %d\n",sum,maxElement,place);

int temp;counter=0;

for (counter;counter<size/2;++counter)
{
temp=arrayWrite[counter];
arrayWrite[counter]=arrayWrite[size-(counter+1)];
arrayWrite[size-(counter+1)]=temp;

}


counter=0;
for(counter;counter<size;++counter)
{
printf("Element[%d] = %d\n",counter,arrayWrite[counter]);
}
printf("sum=%d\nmaxElement is %d and in the index of %d\n",sum,maxElement,place);
*/
}
