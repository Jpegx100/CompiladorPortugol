from antlr4 import *
from PortugolListener import PortugolListener
from antlr4.error.ErrorListener import ErrorListener
if __name__ is not None and "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser

class AcoesSemanticas(PortugolListener):
# Enter a parse tree produced by PortugolParser#programa.
    def enterPrograma(self, ctx:PortugolParser.ProgramaContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#programa.
    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#declaracao_variaveis.
    def enterDeclaracao_variaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#declaracao_variaveis.
    def exitDeclaracao_variaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#lista_variaveis.
    def enterLista_variaveis(self, ctx:PortugolParser.Lista_variaveisContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#lista_variaveis.
    def exitLista_variaveis(self, ctx:PortugolParser.Lista_variaveisContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#declaracao_funcoes.
    def enterDeclaracao_funcoes(self, ctx:PortugolParser.Declaracao_funcoesContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#declaracao_funcoes.
    def exitDeclaracao_funcoes(self, ctx:PortugolParser.Declaracao_funcoesContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#funcao.
    def enterFuncao(self, ctx:PortugolParser.FuncaoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#funcao.
    def exitFuncao(self, ctx:PortugolParser.FuncaoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#lista_comandos.
    def enterLista_comandos(self, ctx:PortugolParser.Lista_comandosContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#lista_comandos.
    def exitLista_comandos(self, ctx:PortugolParser.Lista_comandosContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#comando.
    def enterComando(self, ctx:PortugolParser.ComandoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#comando.
    def exitComando(self, ctx:PortugolParser.ComandoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#se_entao.
    def enterSe_entao(self, ctx:PortugolParser.Se_entaoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#se_entao.
    def exitSe_entao(self, ctx:PortugolParser.Se_entaoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#chamada_funcao.
    def enterChamada_funcao(self, ctx:PortugolParser.Chamada_funcaoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#chamada_funcao.
    def exitChamada_funcao(self, ctx:PortugolParser.Chamada_funcaoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#repita.
    def enterRepita(self, ctx:PortugolParser.RepitaContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#repita.
    def exitRepita(self, ctx:PortugolParser.RepitaContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#enquanto.
    def enterEnquanto(self, ctx:PortugolParser.EnquantoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#enquanto.
    def exitEnquanto(self, ctx:PortugolParser.EnquantoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#teste_logico.
    def enterTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#teste_logico.
    def exitTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#para.
    def enterPara(self, ctx:PortugolParser.ParaContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#para.
    def exitPara(self, ctx:PortugolParser.ParaContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#atribuicao.
    def enterAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#atribuicao.
    def exitAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        print(ctx.getText());pass


    # Enter a parse tree produced by PortugolParser#expressao.
    def enterExpressao(self, ctx:PortugolParser.ExpressaoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#expressao.
    def exitExpressao(self, ctx:PortugolParser.ExpressaoContext):
        print(ctx.getText());pass

    # Enter a parse tree produced by PortugolParser#termo.
    def enterTermo(self, ctx:PortugolParser.TermoContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#termo.
    def exitTermo(self, ctx:PortugolParser.TermoContext):
        print(ctx.getText());pass

    # Enter a parse tree produced by PortugolParser#fator.
    def enterFator(self, ctx:PortugolParser.FatorContext):
        print(ctx.getText());pass

    # Exit a parse tree produced by PortugolParser#fator.
    def exitFator(self, ctx:PortugolParser.FatorContext):
        print(ctx.getText());pass

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