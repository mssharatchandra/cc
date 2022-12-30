%{
#include<stdio.h>
#include<stdlib.h>
%}
%%
[\+\-\*\\] printf("%s is arithmetic operator\n", yytext);
[=] printf("%s is assignment operator\n", yytext);
[,] printf("%s is comma operator\n", yytext);
[<|>]|(<=)|(>=)|(==)|(!=) printf("%s is relational operator\n", yytext);
.* printf("%s is not operator\n",yytext);
%%
int main()
{
yylex();
return 0;
}
