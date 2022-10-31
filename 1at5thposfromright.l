%{
#include<stdio.h>
#include<stdlib.h>
%}

%%
[0-9]*1[0-9]{4}$ printf("%s has 1 at position 5 from right\n", yytext);
.* printf("%s does not match pattern\n",yytext);
%%

int main()
{
yylex();
return 0;
}
