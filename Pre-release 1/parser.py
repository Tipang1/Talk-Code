from Types.TokensTypes import TokenType
from Types.NodesTypes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        """Retourne le token actuel"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def next_token(self):
        """Retourne le token suivant"""
        if self.pos+1 < len(self.tokens):
            return self.tokens[self.pos+1]
        return None
    
    def advance(self, n=1):
        """Avance au token suivant"""
        self.pos += n


#TODO ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    def parse_assignment(self):
        """Parse: IDENTIFIER 'is' EXPRESSION"""

        # 1. Vérifier qu'on a bien un IDENTIFIER
        token = self.current_token()
        if token.type != TokenType.IDENTIFIER:
            raise SyntaxError(f"Attendu un identifiant, reçu {token}")

        variable_name = token.value  # Sauvegarder le nom
        self.advance()  # Passer au token suivant (devrait être 'is')

        # 2. Vérifier qu'on a le keyword "is"
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value != 'is':
            raise SyntaxError(f"Attendu 'is', reçu {token}")

        self.advance()  # Passer à l'expression

        # 3. Parser la valeur
        value_node = self.parse_value()

        # Skip comments
        #self.skip_comments()
        # 4. Créer et retourner le nœud
        return AssignmentNode(variable_name, value_node)

    def parse_say(self):
        """Parse: say EXPRESSION"""
        # Vérifier qu'on a le keyword "say"
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value != 'say':
            raise SyntaxError(f"Attendu 'say', reçu {token}")

        self.advance()  # Passer à l'expression

        # Parser ce qu'on veut afficher
        value = self.parse_value()

        # Skip comments
        self.skip_comments()
        return SayNode(value)

    def parse_if(self):
        """Parse: if CONDITION { STATEMENTS } [else { STATEMENTS }]"""
        # Vérifier 'if'
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value != 'if':
            raise SyntaxError(f"Attendu 'if', reçu {token}")
        self.advance()

        # Parser la condition
        condition = self.parse_expression()

        # Vérifier '{'
        token = self.current_token()
        if token.type != TokenType.LBRACE:
            raise SyntaxError(f"Attendu '{{', reçu {token}")
        self.advance()

        # Parser les instructions du then
        then_branch = []
        while self.current_token() and self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt:  # Ignorer les None
                then_branch.append(stmt)

        # Vérifier '}'
        if self.current_token().type != TokenType.RBRACE:
            raise SyntaxError(f"Attendu '}}', reçu {self.current_token()}")
        self.advance()

        # Vérifier s'il y a un 'else'
        else_branch = None
        token = self.current_token()
        if token and token.type == TokenType.KEYWORD and token.value == 'else':
            self.advance()

            # Vérifier '{'
            if self.current_token().type != TokenType.LBRACE:
                raise SyntaxError(f"Attendu '{{', reçu {self.current_token()}")
            self.advance()

            # Parser les instructions du else
            else_branch = []
            while self.current_token() and self.current_token().type != TokenType.RBRACE:
                stmt = self.parse_statement()
                if stmt:
                    else_branch.append(stmt)

            # Vérifier '}'
            if self.current_token().type != TokenType.RBRACE:
                raise SyntaxError(f"Attendu '}}', reçu {self.current_token()}")
            self.advance()

        return IfNode(condition, then_branch, else_branch)

    def parse_convert(self):
        """Parse: convert IDENTIFIER to TYPE"""
        # Vérifier 'convert'
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value != 'convert':
            raise SyntaxError(f"Attendu 'convert', reçu {token}")
        self.advance()

        # Récupérer le nom de la variable
        token = self.current_token()
        if token.type != TokenType.IDENTIFIER:
            raise SyntaxError(f"Attendu un identifiant, reçu {token}")
        var_name = token.value
        self.advance()

        # Vérifier 'to'
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value != 'to':
            raise SyntaxError(f"Attendu 'to', reçu {token}")
        self.advance()

        # Récupérer le type cible
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value not in ['int', 'float', 'string', 'bool']:
            raise SyntaxError(f"Attendu un type (int/string/bool), reçu {token}")
        target_type = token.value
        self.advance()

        return ConvertNode(var_name, target_type)

    def parse_ask(self):
        """Parse: ask [STRING]"""
        # Vérifier 'ask'
        token = self.current_token()
        if token.type != TokenType.KEYWORD or token.value != 'ask':
            raise SyntaxError(f"Attendu 'ask', reçu {token}")
        self.advance()

        # Le prompt est optionnel
        prompt = None
        if self.current_token() and self.current_token().type == TokenType.STRING:
            prompt = self.current_token().value
            self.advance()

        return AskNode(prompt)

    def parse_value(self):
        """Parse une expression complète (point d'entrée)"""
        return self.parse_expression()

    def parse_expression(self):
        """Parse comparaisons et opérations arithmétiques"""
        left = self.parse_arithmetic()

        # Gérer les comparaisons
        token = self.current_token()
        if token and token.type == TokenType.OPERATOR and token.value in ['<', '>', '=']:
            operator = token.value
            self.advance()
            right = self.parse_arithmetic()
            return ComparisonNode(left, operator, right)

        return left

    def parse_arithmetic(self):
        """Parse addition et soustraction (anciennement parse_expression)"""
        left = self.parse_term()

        while self.current_token() and self.current_token().type == TokenType.OPERATOR:
            op = self.current_token().value
            if op not in ['+', '-', 'plus', 'minus']:
                break
            self.advance()
            right = self.parse_term()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_term(self):
        """Parse multiplication et division (haute priorité)"""
        left = self.parse_simple_value()

        while self.current_token() and self.current_token().type == TokenType.OPERATOR:
            op = self.current_token().value
            if op not in ['*', '/', 'times', 'divided']:
                break  # Pas un opérateur de haute priorité
            self.advance()
            right = self.parse_simple_value()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_simple_value(self):
        """Parse un nombre, string, identifier, ou expression entre parenthèses"""
        token = self.current_token()

        result = None

        if token.type == TokenType.NUMBER:
            self.advance()
            result = NumberNode(token.value)

        elif token.type == TokenType.STRING:
            self.advance()
            result = StringNode(token.value)

        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            result = IdentifierNode(token.value)

        elif token.type == TokenType.KEYWORD and token.value == 'ask':
            return self.parse_ask()

        elif token.type == TokenType.LPAREN:
            self.advance()
            result = self.parse_expression()
            if self.current_token().type != TokenType.RPAREN:
                raise SyntaxError(f"Attendu ')', reçu {self.current_token()}")
            self.advance()

        else:
            raise SyntaxError(f"Valeur inattendue: {token}")

        # Vérifier si on a un 'as type'
        token = self.current_token()
        if token and token.type == TokenType.KEYWORD and token.value == 'as':
            self.advance()

            # Récupérer le type
            token = self.current_token()
            if token.type != TokenType.KEYWORD or token.value not in ['int', 'string', 'bool']:
                raise SyntaxError(f"Attendu un type (int/string/bool), reçu {token}")
            target_type = token.value
            self.advance()

            result = CastNode(result, target_type)

        return result

    def skip_comments(self):
        """Ignore les commentaires (parenthèses après une expression)"""
        while self.current_token() and self.current_token().type == TokenType.LPAREN:
            # C'est un commentaire, ignorer jusqu'à ')'
            self.advance()  # Sauter '('
            depth = 1
            while depth > 0 and self.current_token():
                if self.current_token().type == TokenType.LPAREN:
                    depth += 1
                elif self.current_token().type == TokenType.RPAREN:
                    depth -= 1
                self.advance()


#TODO ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    def parse_program(self):
        """Parse tout le programme (plusieurs instructions)"""
        statements = []

        while self.current_token() is not None:
            # Parser une instruction
            stmt = self.parse_statement()
            statements.append(stmt)

        return ProgramNode(statements)

    def parse_statement(self):
        """Parse une instruction (assignment, say, if, while, etc.)"""
        token = self.current_token()

        if token is None:
            return None

        if token.type == TokenType.LPAREN:
            return self.skip_comments()

        # Si ça commence par un identifiant, c'est un assignment
        elif token.type == TokenType.IDENTIFIER:
            return self.parse_assignment()

        elif token.type == TokenType.KEYWORD:
            if token.value == 'say':
            # Si ça commence par "say", c'est une commande say
                return self.parse_say()
            elif token.value == 'if':
            # Si ça commence par "if", c'est une condition
                return self.parse_if()
            elif token.value == 'convert':
            # Si ça commence par "convert", c'est une conversion
                return self.parse_convert()
            elif token.value == 'ask':
                return self.parse_ask()

        else:
            raise SyntaxError(f"Instruction non reconnue: {token}")


if __name__ == "__main__":
    from lexer import lexer

    # Test 1
    tokens = lexer("x is 10")
    parser = Parser(tokens)
    print(parser.parse_assignment())

    # Test 2
    tokens = lexer('message is "Hello"')
    parser = Parser(tokens)
    print(parser.parse_assignment())

    # Test 3
    tokens = lexer('y is 5 + 3 * 2 - 9')
    parser = Parser(tokens)
    print(parser.parse_assignment())
