import sys
from antlr4 import *
from PortugolLexer import PortugolLexer
from PortugolParser import PortugolParser
from PortugolListener import PortugolListener
from AcoesSemanticas import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl

def lower_arquivo(path):
    arq = open(path,'r')
    texto = arq.read().lower()
    arq.close
    arq = open(path,'w')
    arq.write(texto)
    arq.close()

def main(argv):
    lower_arquivo(argv[1])
    input = FileStream(argv[1])
    lexer = PortugolLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PortugolParser(stream)

    tree = parser.programa()
    if('p' in argv and argv.index('p')>1):
        print_tree(tree, 0)

    if('w' in argv and argv.index('w')>1):
        printer = AcoesSemanticas()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

def print_tree(tree, lev):
    if(tree==None):
        return
    print((" " * lev) + " " + str(tree.getText()))
    if(type(tree)!=TerminalNodeImpl):
        for c in tree.getChildren():
            print_tree(c, lev + 1)

if __name__ == '__main__':
    main(sys.argv)