from antlr4 import *
from PortugolListener import PortugolListener
from antlr4.error.ErrorListener import ErrorListener
from erros import *
if __name__ is not None and "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser
ERRORS = []
INTEIRO = "inteiro"
REAL = "real"
BOOLEANO = "booleano"
STRING = "string"

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
        tipo_r = self.tipo_retorno if self.tipo_retorno!="" else "None"
        return "funcao{nome: "+str(self.nome)+", parametros: "+str(params)+", tipo_retorno: "+tipo_r+"}"

class AcoesSemanticas(PortugolListener):
    tabela_simbolos = {}
    
    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        print(ERRORS)
        pass
    # Enter a parse tree produced by PortugolParser#declaracao_variaveis.
    def enterVariaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        tipo = ctx.TIPO()
        w = [w for w in ctx.lista_variaveis().getText().split(" ")]
        for i in w:
            for j in i.split(","):
                if self.tabela_simbolos.get(j)==None:
                    var = Variavel(tipo, j)
                    self.tabela_simbolos[j] = var
                else:
                    print("Variavel já definida como: ")
                    print(self.tabela_simbolos.get(j))
        pass

    # Enter a parse tree produced by PortugolParser#funcao.
    def enterFuncao(self, ctx:PortugolParser.FuncaoContext):
        parametros = []
        for i in ctx.parametro():
            var = Variavel(i.TIPO(), i.ID())
            parametros.append(var)
        tipo_r = ctx.tipo_retorno().getText() if ctx.tipo_retorno() else ""
        fun = Funcao(tipo_r, parametros, ctx.ID().getText())
        self.tabela_simbolos[ctx.ID().getText()] = fun
        pass
    
    def printtb(self):
        print(self.tabela_simbolos.keys())

    def enterTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        # print("tl1 "+ctx.getText())
        pass
    def enterTeste_logico2(self, ctx:PortugolParser.Teste_logico2Context):
        # print("tl2 "+ctx.getText())
        pass
    def enterTeste_logico3(self, ctx:PortugolParser.Teste_logico3Context):
        # print("tl3 "+ctx.getText())
        pass
    def enterComparacao(self, ctx:PortugolParser.ComparacaoContext):
        # print("cop "+ctx.getText())
        pass
    def enterTermo(self, ctx:PortugolParser.TermoContext):
        # print("termo "+ctx.getText())
        pass 
    
    def exitTermo(self, ctx:PortugolParser.TermoContext):
        if ctx.termo():
            operador = ctx.op.text
            tp1, tp2 = str(ctx.termo()._tipo), str(ctx.fator()._tipo)
            if tp1 not in ["inteiro", "real"] or tp2 not in ["inteiro", "real"]:
                ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+tp1+">>"+tp2)
                pass
            if tp1==tp2:
                ctx._tipo = tp1
            else:
                ctx._tipo = "real"
        elif ctx.fator():
            if str(ctx.fator()._tipo) not in ["inteiro", "real"]:
                #ERRORS.append(ERRO_TIPO_NAO_NUMERICO+str(ctx.fator()._tipo))
                ctx._tipo = str(ctx.fator()._tipo)
                pass
            ctx._tipo = ctx.fator()._tipo
        pass
    
    def enterExpressao(self, ctx:PortugolParser.ExpressaoContext):
        # print("exp "+ctx.getText())
        pass
    
    def exitExpressao(self, ctx:PortugolParser.ExpressaoContext):
        if ctx.expressao():
            tp1, tp2 = str(ctx.expressao()._tipo), str(ctx.termo()._tipo)
            if tp1 not in [INTEIRO, REAL] or tp2 not in [INTEIRO, REAL]:
                ERRORS.append(ERRO_TIPOS_INCOMPATIVEIS+tp1+">"+tp2)
                pass
            if tp1==tp2:
                ctx._tipo = tp1
            else:
                ctx._tipo = "real"
        else:
            tp1 = str(ctx.termo()._tipo)
            if tp1 not in [INTEIRO, REAL]:
                #ERRORS.append(ERRO_TIPO_NAO_NUMERICO+tp1)
                ctx._tipo = tp1
                pass
            else:
                ctx._tipo = tp1
        pass
    
    # Enter a parse tree produced by PortugolParser#fator.
    def enterFator(self, ctx:PortugolParser.FatorContext):
        # print("fat "+ctx.getText())
        pass

    # Exit a parse tree produced by PortugolParser#fator.
    def exitFator(self, ctx:PortugolParser.FatorContext):
        global ERRORS
        if ctx.numero_real():
            ctx._tipo = REAL
        elif ctx.numero():
            ctx._tipo = INTEIRO
        elif ctx.ID():
            if(self.tabela_simbolos.get(ctx.ID().getText())):
                ctx._tipo = self.tabela_simbolos.get(ctx.ID().getText()).tipo
            else:
                ERRORS.append(VARIAVEL_FUNCAO_NAO_DECLARADA+ctx.ID().getText())
        elif ctx.expressao():
            ctx._tipo = ctx.expressao()._tipo
        elif ctx.chamada_funcao_simples():
            nome_funcao = ctx.chamada_funcao_simples().ID().getText()
            ctx._tipo = self.tabela_simbolos[nome_funcao].tipo_retorno
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