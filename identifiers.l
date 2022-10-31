%{
#include<stdio.h>
#include<stdlib.h>
%}

%%
^[a-zA-Z_][a-zA-Z0-9_]*$ printf("%s is valid identifier\n", yytext);
.* printf("%s is invalid\n",yytext);
%%

int main()
{
yylex();
return 0;
}
