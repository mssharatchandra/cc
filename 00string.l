%{
#include<stdio.h>
#include<stdlib.h>
%}


%%
(.)*00$ {printf("%s ends with 00\n",yytext);}
.* {printf("%s does not end with 00\n",yytext);}
%%

int main()
{
yylex();
return 0;
}
