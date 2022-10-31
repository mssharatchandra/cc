%{
#include<stdio.h>
#include<stdlib.h>
%}

%%
^[k](.)* {printf("%s starts with k\n",yytext);}
(.)*[k]$ {printf("%s ends with k\n",yytext);}
(.)* {printf("%s does not match k-pattern\n",yytext);}
%%

int main()
{
yylex();
return 0;
}
