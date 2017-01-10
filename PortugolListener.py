# Generated from Portugol.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser

# This class defines a complete listener for a parse tree produced by PortugolParser.
class PortugolListener(ParseTreeListener):

    # Enter a parse tree produced by PortugolParser#programa.
    def enterPrograma(self, ctx:PortugolParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PortugolParser#programa.
    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PortugolParser#cabecalho.
    def enterCabecalho(self, ctx:PortugolParser.CabecalhoContext):
        pass

    # Exit a parse tree produced by PortugolParser#cabecalho.
    def exitCabecalho(self, ctx:PortugolParser.CabecalhoContext):
        pass


    # Enter a parse tree produced by PortugolParser#declaracao_variaveis.
    def enterDeclaracao_variaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        pass

    # Exit a parse tree produced by PortugolParser#declaracao_variaveis.
    def exitDeclaracao_variaveis(self, ctx:PortugolParser.Declaracao_variaveisContext):
        pass


    # Enter a parse tree produced by PortugolParser#variaveis.
    def enterVariaveis(self, ctx:PortugolParser.VariaveisContext):
        pass

    # Exit a parse tree produced by PortugolParser#variaveis.
    def exitVariaveis(self, ctx:PortugolParser.VariaveisContext):
        pass


    # Enter a parse tree produced by PortugolParser#parametro.
    def enterParametro(self, ctx:PortugolParser.ParametroContext):
        pass

    # Exit a parse tree produced by PortugolParser#parametro.
    def exitParametro(self, ctx:PortugolParser.ParametroContext):
        pass


    # Enter a parse tree produced by PortugolParser#lista_variaveis.
    def enterLista_variaveis(self, ctx:PortugolParser.Lista_variaveisContext):
        pass

    # Exit a parse tree produced by PortugolParser#lista_variaveis.
    def exitLista_variaveis(self, ctx:PortugolParser.Lista_variaveisContext):
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


    # Enter a parse tree produced by PortugolParser#tipo_retorno.
    def enterTipo_retorno(self, ctx:PortugolParser.Tipo_retornoContext):
        pass

    # Exit a parse tree produced by PortugolParser#tipo_retorno.
    def exitTipo_retorno(self, ctx:PortugolParser.Tipo_retornoContext):
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


    # Enter a parse tree produced by PortugolParser#retorne.
    def enterRetorne(self, ctx:PortugolParser.RetorneContext):
        pass

    # Exit a parse tree produced by PortugolParser#retorne.
    def exitRetorne(self, ctx:PortugolParser.RetorneContext):
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


    # Enter a parse tree produced by PortugolParser#chamada_funcao_simples.
    def enterChamada_funcao_simples(self, ctx:PortugolParser.Chamada_funcao_simplesContext):
        pass

    # Exit a parse tree produced by PortugolParser#chamada_funcao_simples.
    def exitChamada_funcao_simples(self, ctx:PortugolParser.Chamada_funcao_simplesContext):
        pass


    # Enter a parse tree produced by PortugolParser#repita.
    def enterRepita(self, ctx:PortugolParser.RepitaContext):
        pass

    # Exit a parse tree produced by PortugolParser#repita.
    def exitRepita(self, ctx:PortugolParser.RepitaContext):
        pass


    # Enter a parse tree produced by PortugolParser#lista_parametros.
    def enterLista_parametros(self, ctx:PortugolParser.Lista_parametrosContext):
        pass

    # Exit a parse tree produced by PortugolParser#lista_parametros.
    def exitLista_parametros(self, ctx:PortugolParser.Lista_parametrosContext):
        pass


    # Enter a parse tree produced by PortugolParser#enquanto.
    def enterEnquanto(self, ctx:PortugolParser.EnquantoContext):
        pass

    # Exit a parse tree produced by PortugolParser#enquanto.
    def exitEnquanto(self, ctx:PortugolParser.EnquantoContext):
        pass


    # Enter a parse tree produced by PortugolParser#comparacao.
    def enterComparacao(self, ctx:PortugolParser.ComparacaoContext):
        pass

    # Exit a parse tree produced by PortugolParser#comparacao.
    def exitComparacao(self, ctx:PortugolParser.ComparacaoContext):
        pass


    # Enter a parse tree produced by PortugolParser#teste_logico.
    def enterTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        pass

    # Exit a parse tree produced by PortugolParser#teste_logico.
    def exitTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        pass


    # Enter a parse tree produced by PortugolParser#teste_logico2.
    def enterTeste_logico2(self, ctx:PortugolParser.Teste_logico2Context):
        pass

    # Exit a parse tree produced by PortugolParser#teste_logico2.
    def exitTeste_logico2(self, ctx:PortugolParser.Teste_logico2Context):
        pass


    # Enter a parse tree produced by PortugolParser#teste_logico3.
    def enterTeste_logico3(self, ctx:PortugolParser.Teste_logico3Context):
        pass

    # Exit a parse tree produced by PortugolParser#teste_logico3.
    def exitTeste_logico3(self, ctx:PortugolParser.Teste_logico3Context):
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


    # Enter a parse tree produced by PortugolParser#numero.
    def enterNumero(self, ctx:PortugolParser.NumeroContext):
        pass

    # Exit a parse tree produced by PortugolParser#numero.
    def exitNumero(self, ctx:PortugolParser.NumeroContext):
        pass


    # Enter a parse tree produced by PortugolParser#numero_real.
    def enterNumero_real(self, ctx:PortugolParser.Numero_realContext):
        pass

    # Exit a parse tree produced by PortugolParser#numero_real.
    def exitNumero_real(self, ctx:PortugolParser.Numero_realContext):
        pass


