%{
  #include<stdio.h>
  #include<stdlib.h>

  int line;
  int loc;
  int id;
  char name[100];
  FILE* fp;

%}


keyword     char|short|int|long|double|float|if|else|for|do|while|void|switch|break|continue|case|return
identifier  [_a-zA-Z][_a-zA-Z0-9]*
number      [0-9]+
arithmetic  (\+)|(\-)|(\*)|(\/)|(\%)
relational  <|>|<=|>=|!=|==
assignment  =
special     \(|\)|[|]|\{|\}|;|\"|\'|#|\?|:|\.


%%
{keyword}     {printf("ID: %-8dType: Keyword      Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
{identifier}  {printf("ID: %-8dType: Identifier   Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
{number}      {printf("ID: %-8dType: Number       Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
{arithmetic}  {printf("ID: %-8dType: ArithOper    Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
{relational}  {printf("ID: %-8dType: RelatOper    Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
{assignment}  {printf("ID: %-8dType: AssignOper   Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
{special}     {printf("ID: %-8dType: SpecialChar  Line: %3d[%-3d]  Symbol: %s\n",id++, line, loc, yytext); loc+=yyleng;}
\n            {line++;loc=1;}
.             {loc+=yyleng;}
%%


int main()
{
id = 0;
line = 1;
loc = 1;
printf("Enter file name : ");
scanf("%s",name);
fp = fopen(name, "r");
if(!fp)
{
printf("Could not open the file");
exit(0);
}
yyin=fp;
printf("Lex output : \n");
yylex();
fclose(fp);
printf("Over");
return 0;
}

int yywrap()
{
return(1);
}
