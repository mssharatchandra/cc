yacc1.y
%{
#include<stdio.h>
#include<ctype.h>
%}
%token NUM
%%
cmd:E {printf(“%d\n”, $1);}
E: E’+’T {$$= $1+$3;}
|T {$$= $1;};
E: E’-‘T {$$= $1-$3;};
T: T’*’F {$$= $1*$3;}
|F {$$=$1;};
T: T’/’F {$$= $1/$3;};
F: ‘(‘E’)’ {$$= $2;};
NUM {$$= $1;};
%%
int yyerror(char* s){
printf(“%s\n”, s);
return 0;}
int main(){
yyparse();
return 0;}
yacclex1.l
%{
#include “y.tab.h”
extern int yylval;
%}
%%
[0-9]+ {yylval=atoi(yytext); return NUM;}
\n {return 0;}
{return yytext[0];}
%%
int yywrap(){
return 1;}
