#include <stdio.h>
#include <stdlib.h>
double seriesSum(int numOfTerms );
int factorial(int number);
int main()
{
   int numOfTerms=0;
   double sum;
while (numOfTerms<=0)
  {

      printf("number of terms of the series : ");

      scanf("%d",&numOfTerms);
  }

  sum=seriesSum(numOfTerms);


printf("\n%lf",sum);
    return 0;
}
double seriesSum(int numOfTerms )
{
double sum;
int counter=1;
int numOfTermsCopy=numOfTerms;

for (counter;numOfTermsCopy!=0;counter=counter+2)
{
int denominator= factorial(counter-1);
int nominator=pow(counter,2);

sum+=nominator/(denominator*1.0);
--numOfTermsCopy;
}
return sum;

}
int factorial(int number)
{
  if (number==1||number==0)
  {return 1;}
  else
    return number*factorial(number-1);
}
