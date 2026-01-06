from Types.TokensTypes import TokenType
from Classes.TokenClass import Token
from KeywordsOperators import *

# Fonction réutilisable pour lire jusqu'à un délimiteur
def read_until(code, i, delimiter):
    """Lit les caractères jusqu'à trouver le délimiteur"""
    i += 1  # Sauter le délimiteur d'ouverture
    content = ''
    while i < len(code) and code[i] != delimiter:
        content += code[i]
        i += 1
    i += 1  # Sauter le délimiteur de fermeture
    return content, i

def lexer(code):
    tokens = []
    i = 0
    
    while i < len(code):
        char = code[i]
        
        # Ignorer espaces et tabs
        if char in " \t\n":
            i += 1
            continue
        
        # Reconnaître les nombres
        if char.isdigit():
            num = ''
            while i < len(code) and (code[i].isdigit() or code[i] == '.'):  # Support décimaux !
                num += code[i]
                i += 1
            tokens.append(Token(TokenType.NUMBER, num))
            continue
        
        # Reconnaître les identifiants et mots-clés
        if char.isalpha():
            word = ''
            while i < len(code) and (code[i].isalnum() or code[i] == '_'):
                word += code[i]
                i += 1
            
            if word in KEYWORDS:
                tokens.append(Token(TokenType.KEYWORD, word))
            else:
                tokens.append(Token(TokenType.IDENTIFIER, word))
            continue
        
        # Reconnaître les strings (guillemets doubles ou simples)
        if char in '"\'':
            string, i = read_until(code, i, char)
            tokens.append(Token(TokenType.STRING, string))
            continue
        
        # Reconnaître les parenthèses, accolades, crochets
        if char == '(':
            tokens.append(Token(TokenType.LPAREN, char))
            i += 1
            continue
        if char == ')':
            tokens.append(Token(TokenType.RPAREN, char))
            i += 1
            continue
        if char == '{':
            tokens.append(Token(TokenType.LBRACE, char))
            i += 1
            continue
        if char == '}':
            tokens.append(Token(TokenType.RBRACE, char))
            i += 1
            continue
        if char == '[':
            tokens.append(Token(TokenType.LBRACKET, char))
            i += 1
            continue
        if char == ']':
            tokens.append(Token(TokenType.RBRACKET, char))
            i += 1
            continue
        
        # Reconnaître les opérateurs
        if char in OPERATORS:
            tokens.append(Token(TokenType.OPERATOR, char))
            i += 1
            continue
        
        # Si on arrive ici, caractère inconnu
        raise SyntaxError(f"Caractère inconnu: '{char}' à la position {i+1}")
    
    return tokens

# Test
if __name__ == "__main__":
    test_code = 'x is 10\nmessage is "Hello World"\ny is 5 + 3.14\nz is (2 + 3) * 4'
    print(lexer(test_code))