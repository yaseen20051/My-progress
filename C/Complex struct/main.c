#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<math.h>
typedef struct {

float Real;
float Imaginary;

}complex;
complex complexOperation(complex*num_1,complex*num_2,char operation);
///complex Multiple(complex*num_1,complex*num_2);
void main(){
char operation;
complex num_1={4,3};
complex num_2={4,3};
scanf("%c",&operation);
complex result;
result=complexOperation(&num_1,&num_2,operation);
printf("(%g)+(%g)i",result.Real,result.Imaginary);
}
complex complexOperation(complex*num_1,complex*num_2,char operation)
{
if(operation=='+')
{
complex AddTwoComplex;
AddTwoComplex.Real=num_1->Real+num_2->Real;
AddTwoComplex.Imaginary=num_2->Imaginary+num_2->Imaginary;
return AddTwoComplex;
}
else if(operation=='-')
{
complex substractTwoComplex;
substractTwoComplex.Real=num_1->Real-num_2->Real;
substractTwoComplex.Imaginary=num_2->Imaginary-num_2->Imaginary;
return substractTwoComplex;
}
else if (operation=='*')
{
complex MulitpleTwoComplex;
MulitpleTwoComplex.Real=(num_1->Real*num_2->Real)-(num_2->Imaginary*num_1->Imaginary);
MulitpleTwoComplex.Imaginary=(num_1->Real*num_2->Imaginary)+(num_2->Real*num_1->Imaginary);

return MulitpleTwoComplex;
}



}
/**complex Multiple(complex*num_1,complex*num_2)
{
complex MulitpleTwoComplex;
float angle_1=atan(num_1->Imaginary/num_1->Real*1.0)*180/3.14;
float angle_2=atan(num_2->Imaginary/num_2->Real*1.0)*180/3.14;
float angle_3=angle_1+angle_2;
float R=sqrt((num_1->Real*num_1->Real)+(num_1->Imaginary*num_1->Imaginary))*sqrt((num_2->Real*num_2->Real)+(num_2->Imaginary*num_2->Imaginary));

MulitpleTwoComplex.Real=R*cos(angle_3*3.14/180);
MulitpleTwoComplex.Imaginary=R*sin(angle_3*3.14/180);
return MulitpleTwoComplex;
}*/
