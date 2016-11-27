from antlr4 import *
from PortugolListener import PortugolListener
from antlr4.error.ErrorListener import ErrorListener
if __name__ is not None and "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser
class Variavel():
    tipo = ""
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return "Tipo: "+self.tipo

class Funcao():
    tipo_retorno = ""
    lista_tipos = []


class AcoesSemanticas(PortugolListener):
    tabela_simbolos = {}
    # Enter a parse tree produced by PortugolParser#programa.
    def enterPrograma(self, ctx:PortugolParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PortugolParser#programa.
    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        for (key, value) in self.tabela_simbolos.items():
            print(value)
        pass


    # Enter a parse tree produced by PortugolParser#declaracao_variaveis.
    def enterVariaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        tipo = ctx.TIPO()
        w = [w for w in ctx.lista_variaveis().getText().split(" ")]
        for i in w:
            for j in i.split(","):
                if self.tabela_simbolos.get(j)==None:
                    var = Variavel(tipo)
                    self.tabela_simbolos[j] = var
        pass

    # Exit a parse tree produced by PortugolParser#declaracao_variaveis.
    def exitVariaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        pass


    # Enter a parse tree produced by PortugolParser#lista_variaveis.
    def enterLista_variaveis(self, ctx:PortugolParser.Lista_variaveisContext):
        #print(">>")
        #print(ctx.ID())
        pass

    # Exit a parse tree produced by PortugolParser#lista_variaveis.
    def exitLista_variaveis(self, ctx:PortugolParser.Lista_variaveisContext):
        #print("<<")
        pass


    # Enter a parse tree produced by PortugolParser#declaracao_funcoes.
    def enterDeclaracao_funcoes(self, ctx:PortugolParser.Declaracao_funcoesContext):
        pass

    # Exit a parse tree produced by PortugolParser#declaracao_funcoes.
    def exitDeclaracao_funcoes(self, ctx:PortugolParser.Declaracao_funcoesContext):
        pass


    # Enter a parse tree produced by PortugolParser#funcao.
    def enterFuncao(self, ctx:PortugolParser.FuncaoContext):
        pass

    # Exit a parse tree produced by PortugolParser#funcao.
    def exitFuncao(self, ctx:PortugolParser.FuncaoContext):
        pass


    # Enter a parse tree produced by PortugolParser#lista_comandos.
    def enterLista_comandos(self, ctx:PortugolParser.Lista_comandosContext):
        pass

    # Exit a parse tree produced by PortugolParser#lista_comandos.
    def exitLista_comandos(self, ctx:PortugolParser.Lista_comandosContext):
        pass


    # Enter a parse tree produced by PortugolParser#comando.
    def enterComando(self, ctx:PortugolParser.ComandoContext):
        pass

    # Exit a parse tree produced by PortugolParser#comando.
    def exitComando(self, ctx:PortugolParser.ComandoContext):
        pass


    # Enter a parse tree produced by PortugolParser#se_entao.
    def enterSe_entao(self, ctx:PortugolParser.Se_entaoContext):
        pass

    # Exit a parse tree produced by PortugolParser#se_entao.
    def exitSe_entao(self, ctx:PortugolParser.Se_entaoContext):
        pass


    # Enter a parse tree produced by PortugolParser#chamada_funcao.
    def enterChamada_funcao(self, ctx:PortugolParser.Chamada_funcaoContext):
        pass

    # Exit a parse tree produced by PortugolParser#chamada_funcao.
    def exitChamada_funcao(self, ctx:PortugolParser.Chamada_funcaoContext):
        pass


    # Enter a parse tree produced by PortugolParser#repita.
    def enterRepita(self, ctx:PortugolParser.RepitaContext):
        pass

    # Exit a parse tree produced by PortugolParser#repita.
    def exitRepita(self, ctx:PortugolParser.RepitaContext):
        pass


    # Enter a parse tree produced by PortugolParser#enquanto.
    def enterEnquanto(self, ctx:PortugolParser.EnquantoContext):
        pass

    # Exit a parse tree produced by PortugolParser#enquanto.
    def exitEnquanto(self, ctx:PortugolParser.EnquantoContext):
        pass


    # Enter a parse tree produced by PortugolParser#teste_logico.
    def enterTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        pass

    # Exit a parse tree produced by PortugolParser#teste_logico.
    def exitTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        pass


    # Enter a parse tree produced by PortugolParser#para.
    def enterPara(self, ctx:PortugolParser.ParaContext):
        pass

    # Exit a parse tree produced by PortugolParser#para.
    def exitPara(self, ctx:PortugolParser.ParaContext):
        pass


    # Enter a parse tree produced by PortugolParser#atribuicao.
    def enterAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by PortugolParser#atribuicao.
    def exitAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by PortugolParser#expressao.
    def enterExpressao(self, ctx:PortugolParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by PortugolParser#expressao.
    def exitExpressao(self, ctx:PortugolParser.ExpressaoContext):
        pass

    # Enter a parse tree produced by PortugolParser#termo.
    def enterTermo(self, ctx:PortugolParser.TermoContext):
        pass

    # Exit a parse tree produced by PortugolParser#termo.
    def exitTermo(self, ctx:PortugolParser.TermoContext):
        pass

    # Enter a parse tree produced by PortugolParser#fator.
    def enterFator(self, ctx:PortugolParser.FatorContext):
        pass

    # Exit a parse tree produced by PortugolParser#fator.
    def exitFator(self, ctx:PortugolParser.FatorContext):
        pass

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