import sys
from antlr4 import *
from PortugolLexer import PortugolLexer
from PortugolParser import PortugolParser
from PortugolListener import PortugolListener
from AcoesSemanticas import *

def main(argv):
    input = FileStream(argv[1])
    lexer = PortugolLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PortugolParser(stream)
    #parser._listeners = [ PortugolErrorListener() ]
    tree = parser.programa()
    if('p' in argv and argv.index('p')>1):
    	print(tree.toStringTree())
    if('w' in argv and argv.index('w')>1):
        printer = AcoesSemanticas()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)