%{
#include<stdio.h>
#include<stdlib.h>
%}

%%
char|short|int|long|double|float|if|else|for|do|while|void|switch|break|continue|case|return {printf("%s is a keyword\n",yytext);}
.* printf("%s not a keyword\n",yytext);
%%

int main()
{
yylex();
return 0;
}
