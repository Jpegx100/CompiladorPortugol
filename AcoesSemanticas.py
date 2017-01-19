from antlr4 import *
from PortugolListener import PortugolListener
from antlr4.error.ErrorListener import ErrorListener
from erros import *
if __name__ is not None and "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser

class Variavel():
    tipo = ""
    nome = ""
    def __init__(self, tipo, nome):
        self.tipo = tipo
        self.nome = nome
    def __str__(self):
        return "variavel{nome: "+str(self.nome)+", tipo: "+str(self.tipo)+"}"

class Funcao():
    tipo_retorno = ""
    lista_parametros = []
    nome = ""
    def __init__(self, tipo_retorno, lista_parametros, nome):
        self.tipo_retorno = tipo_retorno
        self.lista_parametros = lista_parametros
        self.nome = nome
    def __str__(self):
        params = [str(i) for i in self.lista_parametros]
        tipo_r = self.tipo_retorno if self.tipo_retorno!="" else "vazio"
        return "funcao{nome: "+str(self.nome)+", parametros: "+str(params)+", tipo_retorno: "+tipo_r+"}"

class AcoesSemanticas(PortugolListener):
    PALAVRAS_RESERVADAS = ['prog','fim','funcao','retorne','se','entao',
                            'senao','repita','ate','enquanto','faca','para',
                            'inteiro', 'real', 'booleano', 'string', 'passo', 
                            'verdadeiro', 'falso', 'sair']
    ERRORS = []
    INTEIRO = "inteiro"
    REAL = "real"
    BOOLEANO = "booleano"
    STRING = "string"
    tipos_numericos = [INTEIRO, REAL]
    tabela_simbolos = {}
    funcao_atual = None
    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        print(self.ERRORS)
        return

    def enterVariaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        tipo = ctx.TIPO()
        w = [w for w in ctx.lista_variaveis().getText().split(" ")]
        for i in w:
            for j in i.split(","):
                if j not in self.PALAVRAS_RESERVADAS:
                    if self.tabela_simbolos.get(j)==None:
                        var = Variavel(tipo, j)
                        self.tabela_simbolos[j] = var
                    else:
                        self.ERRORS.append(VARIAVEL_FUNCAO_JA_DECLARADA+self.tabela_simbolos.get(j).nome)
                else:
                    self.ERRORS.append(PALAVRA_RESERVADA+j)
        pass

    def enterFuncao(self, ctx:PortugolParser.FuncaoContext):
        if ctx.ID().getText() not in self.tabela_simbolos:
            parametros = []
            for i in ctx.parametro():
                var = Variavel(i.TIPO(), i.ID())
                parametros.append(var)
            if ctx.tipo_retorno():
                tipo_r = ctx.tipo_retorno().getText()
            else:
                tipo_r = "vazio"
                for comando in ctx.lista_comandos().comando():
                    for i in range(comando.getText().count("retorne")):
                        self.ERRORS.append(FUNCAO_SEM_RETORNO+"")
            self.funcao_atual = ctx.ID().getText()
            fun = Funcao(tipo_r, parametros, ctx.ID().getText())
            self.tabela_simbolos[ctx.ID().getText()] = fun
        else:
            self.ERRORS.append(VARIAVEL_FUNCAO_JA_DECLARADA+ctx.ID().getText())

    def exitFuncao(self, ctx:PortugolParser.FuncaoContext):
        self.funcao_atual = None
    
    def printtb(self):
        print(self.tabela_simbolos.keys())
    
    def exitFator(self, ctx:PortugolParser.FatorContext):
        if ctx.numero_real():
            ctx._tipo = self.REAL
        elif ctx.numero():
            ctx._tipo = self.INTEIRO
        elif ctx.ID():
            if(self.tabela_simbolos.get(ctx.ID().getText())):
                ctx._tipo = self.tabela_simbolos.get(ctx.ID().getText()).tipo
            else:
                if self.funcao_atual!=None:
                    for parametro in self.tabela_simbolos[self.funcao_atual].lista_parametros:
                        if str(parametro.nome) == ctx.ID().getText():
                            ctx._tipo = parametro.tipo
                            return 
                self.ERRORS.append(VARIAVEL_FUNCAO_NAO_DECLARADA+ctx.ID().getText())
        elif ctx.expressao():
            ctx._tipo = ctx.expressao()._tipo
        elif ctx.chamada_funcao_simples():
            nome_funcao = ctx.chamada_funcao_simples().ID().getText()
            if nome_funcao in self.tabela_simbolos:
                ctx._tipo = self.tabela_simbolos[nome_funcao].tipo_retorno
            else:
                self.ERRORS.append(VARIAVEL_FUNCAO_NAO_DECLARADA+nome_funcao)
        pass
    
    def exitTermo(self, ctx:PortugolParser.TermoContext):
        if ctx.termo():
            operador = ctx.op.text
            tp1, tp2 = str(ctx.termo()._tipo), str(ctx.fator()._tipo)
            if tp1 not in self.tipos_numericos or tp2 not in self.tipos_numericos:
                tp1 = tp1 if tp1 and tp1!="None" else "vazio"
                tp2 = tp2 if tp2 and tp2!="None" else "vazio"
                self.ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+tp1+" > "+tp2)
            if tp1==tp2:
                ctx._tipo = tp1
            else:
                ctx._tipo = "real"
        elif ctx.fator():
            if str(ctx.fator()._tipo) not in self.tipos_numericos:
                ctx._tipo = str(ctx.fator()._tipo)
            ctx._tipo = ctx.fator()._tipo
    
    def exitExpressao(self, ctx:PortugolParser.ExpressaoContext):
        if ctx.expressao():
            tp1, tp2 = str(ctx.expressao()._tipo), str(ctx.termo()._tipo)
            if tp1 not in self.tipos_numericos or tp2 not in self.tipos_numericos:
                tp1 = tp1 if tp1 and tp1!="None" else "vazio"
                tp2 = tp2 if tp2 and tp2!="None" else "vazio"
                self.ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+tp1+" > "+tp2)
            if tp1==tp2:
                ctx._tipo = tp1
            else:
                ctx._tipo = "real"
        else:
            tp1 = str(ctx.termo()._tipo)
            if tp1 not in self.tipos_numericos:
                #ERRORS.append(ERRO_TIPO_NAO_NUMERICO+tp1)
                ctx._tipo = tp1
                pass
            else:
                ctx._tipo = tp1
        pass
    def enterChamada_funcao_simples(self, ctx:PortugolParser.Chamada_funcao_simplesContext):
        if ctx.ID().getText() not in self.tabela_simbolos:
            if ctx.ID().getText()!="leia" and ctx.ID().getText()!="imprima":
                self.ERRORS.append(VARIAVEL_FUNCAO_NAO_DECLARADA+ctx.ID().getText())
        pass

    def exitChamada_funcao_simples(self, ctx:PortugolParser.Chamada_funcao_simplesContext):
        pass

    def enterChamada_funcao(self, ctx:PortugolParser.Chamada_funcaoContext):
        if ctx.ID().getText() not in self.tabela_simbolos:
            if ctx.ID().getText()!="leia" and ctx.ID().getText()!="imprima":
                self.ERRORS.append(VARIAVEL_FUNCAO_NAO_DECLARADA+ctx.ID().getText())

    def enterLista_parametros(self, ctx:PortugolParser.Lista_parametrosContext):
        pass
    
    def exitAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        if (ctx.ID().getText() in self.tabela_simbolos):
            simbolo = self.tabela_simbolos[ctx.ID().getText()]
            if isinstance(simbolo, Variavel):
                if ctx.expressao():
                    if str(simbolo.tipo) != str(ctx.expressao()._tipo):
                        self.ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+str(simbolo.tipo)+" > "+str(ctx.expressao()._tipo))
                elif ctx.teste_logico():
                    if str(simbolo.tipo) != str(ctx.teste_logico()._tipo):
                        self.ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+str(simbolo.tipo)+" > "+str(ctx.teste_logico()._tipo))
            else:
                if ctx.expressao():
                    self.ERRORS.append(ATRIBUICAO_PARA_FUNCAO+ctx.expressao().getText())
                elif ctx.teste_logico():
                    self.ERRORS.append(ATRIBUICAO_PARA_FUNCAO+ctx.teste_logico().getText())
        pass
    
    def enterFator(self, ctx:PortugolParser.FatorContext):
        pass
    def enterParametro(self, ctx:PortugolParser.ParametroContext):
        # print(ctx.getText())
        pass
    # def exitTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
    #     if ctx.OPERADOR_LOGICO:
    #         tp1 = str(ctx.teste_logico_esquerdo()._tipo)
    #         tp2 = str(ctx.teste_logico()._tipo)
    #         if tp1==tp2:
    #             ctx._tipo = tp1
    #         else:
    #             ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+tp1+">"+tp2)
    #     pass
    #     #teste_logico: NEGACAO? teste_logico_esquerdo (OPERADOR_LOGICO teste_logico)*;
    # def exitTeste_logico_esquerdo(self, ctx:PortugolParser.Teste_logico_esquerdoContext):
    #     if ctx.ID():
    #         ctx._tipo = self.tabela_simbolos.get(ctx.ID().getText()).tipo
    #     elif ctx.numero_real():
    #         ctx._tipo = REAL
    #     elif ctx.numero():
    #         ctx._tipo = INTEIRO
    #     elif ctx.chamada_funcao_simples():
    #         nome_funcao = ctx.chamada_funcao_simples().ID().getText()
    #         ctx._tipo = self.tabela_simbolos[nome_funcao].tipo_retorno
    #     elif ctx.expressao():
    #         ctx._tipo = ctx.expressao()._tipo

class PortugolErrorListener( ErrorListener ):
    def __init__(self):
        super(PortugolErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Oh no!!")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("Oh no!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Oh no!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no!!")