%{
#include<stdio.h>
#include<string.h>
int line;
int j;
int dataline;
char name[100];
FILE* fp;
char data[100][199];
%}
%%
[\n] {strcat(data[dataline], "\n\0"); dataline++; line++; data[dataline][0]=line+48; 
data[dataline][1]='\0';}
. {strcat(data[dataline],yytext);}
%%
int main()
{
dataline = 0;
line = 1;
printf("Enter file name : ");
scanf("%s",name);
fp = fopen(name, "r");
yyin = fp;
yylex();
fclose(fp);
fp = fopen(name, "w");
fprintf(fp,"1");
for(j=0; j<line; j++)
fprintf(fp, data[j]);
fclose(fp);
return 0;
}
