from enum import Enum

class TokenType(Enum):
    NUMBER = "NUMBER"      # NUM
    IDENTIFIER = "IDENTIFIER" # TEXT
    KEYWORD = "KEYWORD"    # 'is', 'plus', 'minus', 'times', 'divided', 'by', 'if', 'say', 'repeat', 'while', 'ask'
    OPERATOR = "OPERATOR"  # '+', '-', '*', '/', '<', '>', '='
    STRING = "STRING"      # "TEXT" || 'TEXT'
    LPAREN = "LPAREN"      # (
    RPAREN = "RPAREN"      # )
    LBRACE = "LBRACE"      # {
    RBRACE = "RBRACE"      # }
    LBRACKET = "LBRACKET"  # [
    RBRACKET = "RBRACKET"  # ]
