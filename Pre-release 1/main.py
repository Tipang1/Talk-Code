from lexer import lexer
from parser import Parser
from interpreter import Interpreter


def run_file(filename):
    """Exécute un fichier de code"""
    # 1. Lire le fichier
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()

    # 2. Lexer
    tokens = lexer(code)

    # 3. Parser
    parser = Parser(tokens)
    ast = parser.parse_program()

    # 4. Interpréter
    interpreter = Interpreter()
    interpreter.visit(ast)

    print(f"\nVariables finales: {interpreter.variables}")


# Test
if __name__ == "__main__":
    run_file(input("Chemin absolu vers le fichier : "))
