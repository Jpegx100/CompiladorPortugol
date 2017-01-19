grammar Portugol; 

programa: cabecalho declaracao_variaveis declaracao_funcoes lista_comandos 'fim' '.';
cabecalho: 'prog' ID ';';
declaracao_variaveis: (variaveis)*;
variaveis: TIPO lista_variaveis ';';
parametro: TIPO ID;
lista_variaveis: ID 
	| ID ',' lista_variaveis
        ;
declaracao_funcoes: funcao*;
funcao: 'funcao' ID '(' parametro (',' parametro)* ')' (':' tipo_retorno)? ';' declaracao_variaveis lista_comandos retorne? FIM;
tipo_retorno: TIPO; 
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
retorne: 'retorne' (ID|STRING|expressao|teste_logico) ';';
se_entao: 'se' '(' teste_logico ')' 'entao' lista_comandos ('senao' lista_comandos)? FIM;
chamada_funcao: ID '(' lista_parametros ')' ';';
chamada_funcao_simples: ID '(' lista_parametros ')';
repita: 'repita' lista_comandos 'ate' '(' teste_logico ')'';';
lista_parametros: (STRING|expressao|teste_logico) (',' + lista_parametros)?;
enquanto: 'enquanto' '(' teste_logico ')' 'faca' lista_comandos FIM;

comparacao returns [String _tipo]: expressao OPERADOR_COMPARACAO expressao;
teste_logico returns [String _tipo]
        : teste_logico OU_LOGICO teste_logico2
        | teste_logico2
        ;
teste_logico2 returns [String _tipo]
        : teste_logico2 E_LOGICO teste_logico3
        | teste_logico3
        ;
teste_logico3 returns [String _tipo]
        : comparacao
        | '(' teste_logico ')'
        | ID
        | BOOL
        | NEGACAO teste_logico
        ;

para: 'para' ID '=' (ID|numero) 'ate' (ID|numero) ('passo' (ID|numero))? 'faca' lista_comandos FIM;
atribuicao: ID '=' (expressao|teste_logico) ';';

expressao returns [String _tipo]
        : expressao op=('+'|'-') termo
	| termo
	;
termo returns [String _tipo]
        : termo op=('*'|'/') fator 
	| fator
	;
fator returns [String _tipo]
        : ID
	| '(' expressao ')'
	| chamada_funcao_simples
        | numero
        | numero_real
        ;

numero : '-'? NUM ;
numero_real: '-'? NUM_REAL;
TIPO: 'inteiro'
    | 'real' 
    | 'booleano' 
    | 'string' 
    ;
FIM: 'fim' ';'; 
BOOL: 'verdadeiro' | 'falso';
NEGACAO: '!';
E_LOGICO: '&';
OU_LOGICO: '|';
OPERADOR_COMPARACAO : '>' | '<' | '<=' | '>=' | '==' | '!=';
SAIR: 'sair' ';';
ID: [a-zA-Z][a-zA-Z0-9]*;
NUM : [0-9]+;
NUM_REAL: [0-9]+ '.' [0-9]+;
STRING: '\"' .* '\"';
WS: [ \t\r\n] -> skip;
COMMENT
    : '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;