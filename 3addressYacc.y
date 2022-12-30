3add.y

%{
#include<stdio.h>
#include<string.h>
int nIndex = 0;
struct Intercode{
char operand1;
char operand2;
char opera;};
%}
%union{char sym;}
%token <sym> letter number
%type <sym> expr
%left ‘-‘’+’
%right ‘*’’/’
%%
statement: letter‘=’expr’;’ {addtotable((char)$1, (char)$3, ‘=’);}
|expr;
;
expr: expr’+’expr {$$=addtotable((char)$1,(char)$3, ‘+’);}
|expr’-’expr {$$=addtotable((char)$1,(char)$3, ‘-’);}
|expr’*’expr {$$=addtotable((char)$1,(char)$3, ‘*’);}
|expr’/’expr {$$=addtotable((char)$1,(char)$3, ‘/’);}
|’(‘expr’)’ {$$=(char)$2;}
|number {$$=(char)$1;}
|letter {$$=(char)$1;}
%%
yyerror(char *s){
printf(“%s”,s);
exit(0);}
struct Intercode code[20];
char addtotable(char operand1, char operand2, char opera){
char temp=’A’;
code[nIndex].operand1 = operand1;
code[nIndex].operand2 = operand2;
code[nIndex].opera = opera;
nIndex++;
temp++;
return temp;
}
threeaddresscode(){
int nCnt=0;
char temp=’A’;
printf(“\n\n\t three address codes\n\n”);
temp++;
while(nCnt < nIndex){
printf(“%c:=\t”,temp);
if(isalpha(code[nCnt].operand1))
printf(“%c\t”, code[nCnt].operand1);
else
printf(“%c\t”, temp);
printf(“%c\t”,code[nCnt].opera);
if(isalpha(code[nCnt].operand2))
printf(“%c\t”, code[nCnt].operand2);
else
printf(“%c\t”, temp);
printf(“\n”);
nCnt++;
temp++;}}
main(){
printf(“Enter expression : “);
yyparse();
threeaddresscode();}
yywrap(){
return 1;}



3addlex.l

%{
#include “y.tab.h”
extern char yyval;
%}
number [0-9]+
letter [a-zA-Z]+
%%
{number} {yylval.sym=(char)yytext[0]; return number;}
{letter} {yylval.sym=(char)yytext[0]; return letter;}
\n {return 0;}
{return yytext[0];}
%%
