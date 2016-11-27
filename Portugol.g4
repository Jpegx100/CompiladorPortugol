grammar Portugol;

programa: 'prog' ID ';' declaracao_variaveis declaracao_funcoes lista_comandos 'fim' ';'
	;
declaracao_variaveis: (variaveis)+
	;
variaveis: TIPO lista_variaveis ';';
declaracao_parametros: TIPO ID (',' TIPO ID)*;
lista_variaveis: ID 
	| ID ',' lista_variaveis
	;
declaracao_funcoes: funcao*;
funcao: 'funcao' ID '(' declaracao_parametros* ')' (':' TIPO)? ';' lista_comandos retorne? 'fim' ';';
lista_comandos: comando+;
comando: se_entao 
       | atribuicao
       | para
       | enquanto
       | repita
       | chamada_funcao
       | retorne
       | SAIR
	;
retorne: 'retorne' (ID|NUM|expressao) ';';
se_entao: 'se' '(' teste_logico ')' 'entao' lista_comandos ('senao' lista_comandos)? 'fim'';';
chamada_funcao: ID '(' lista_parametros ')' ';';
chamada_funcao_simples: ID '(' lista_parametros ')';
repita: 'repita' lista_comandos 'ate' '(' teste_logico ')'';';
lista_parametros: (ID|STRING|NUM|expressao|teste_logico|chamada_funcao_simples) (',' + lista_parametros)?;
enquanto: 'enquanto' '(' teste_logico ')' 'faca' lista_comandos 'fim'';';
teste_logico: (ID|NUM|chamada_funcao_simples|expressao) (OPERADOR_LOGICO teste_logico)*
            | '!' (ID|NUM)
            ;
para: 'para' ID '=' (ID|NUM) 'ate' (ID|NUM) ('passo' (ID|NUM))? 'faca' lista_comandos 'fim'';';
atribuicao: ID '=' expressao ';'
	;
expressao: expressao ('+'|'-') termo
	| termo
	;
termo: termo ('*'|'/') fator 
	| fator
	;
fator: NUM
	| ID 
	| '(' expressao ')'
	| chamada_funcao_simples
	;
TIPO: 'inteiro'
    | 'real'
    | 'booleano'
    | 'string'
    ;
OPERADOR_LOGICO: '>' | '<' | '<=' | '>=' | '==' | '!=' | '&' | '|';
SAIR: 'sair' ';';
ID: [a-zA-Z][a-zA-Z0-9]*;
NUM: [0-9]+('.'[0-9]+)?;
STRING: '\"'[a-zA-Z0-9]*'\"';
WS: [ \t\r\n ] -> skip;