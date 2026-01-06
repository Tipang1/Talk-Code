from Types.NodesTypes import *

class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        """Visite un noeud et l'execute"""
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"Pas de méthode visit_{type(node).__name__} définie")

    def visit_NoneType(self, *args):
        pass

    def visit_ProgramNode(self, node):
        """Exécute toutes les instructions du programme"""
        result = None
        for statement in node.statements:
            result = self.visit(statement)
        return result  # Retourne le résultat de la dernière instruction

    def visit_NumberNode(self, node):
        """Retourne la valeur du nombre"""
        return node.value

    def visit_StringNode(self, node):
        """Retourne la valeur de la string"""
        return node.value

    def visit_IdentifierNode(self, node):
        """Récupère la valeur d'une variable"""
        if node.name in self.variables:
            return self.variables[node.name]
        else:
            raise NameError(f"Variable '{node.name}' non définie")

    def visit_BinaryOpNode(self, node):
        """Exécute une opération binaire"""
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.operator in ['+', 'plus']:
            return left + right
        elif node.operator in ['-', 'minus']:
            return left - right
        elif node.operator in ['*', 'times']:
            return left * right
        elif node.operator in ['/', 'divided']:
            return left / right
        else:
            raise Exception(f"Opérateur inconnu: {node.operator}")

    def visit_ComparisonNode(self, node):
        """Exécute une comparaison"""
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.operator == '<':
            return left < right
        elif node.operator == '>':
            return left > right
        elif node.operator == '=':
            return left == right
        else:
            raise Exception(f"Opérateur de comparaison inconnu: {node.operator}")

    def visit_AssignmentNode(self, node):
        """Assigne une valeur à une variable"""
        value = self.visit(node.value)
        self.variables[node.variable] = value
        return value  # Retourne la valeur assignée

    def visit_SayNode(self, node):
        """Affiche une valeur"""
        value = self.visit(node.value)
        # Arrondir les floats pour un affichage propre
        if isinstance(value, float):
            print(round(value, 10))  # Enlève les erreurs de précision minimes
        else:
            print(value)
        return value

    def visit_IfNode(self, node):
        """Exécute un if"""
        condition = self.visit(node.condition)

        if condition:
            # Exécuter le then
            for stmt in node.then_branch:
                self.visit(stmt)
        elif node.else_branch:
            # Exécuter le else
            for stmt in node.else_branch:
                self.visit(stmt)

    def visit_ConvertNode(self, node):
        """Convert: modifie la variable directement"""
        if node.variable not in self.variables:
            raise NameError(f"Variable '{node.variable}' non définie")

        value = self.variables[node.variable]
        converted = self._convert_type(value, node.target_type)
        self.variables[node.variable] = converted
        return converted

    def visit_CastNode(self, node):
        """Cast: conversion inline sans modifier la variable"""
        value = self.visit(node.expression)
        return self._convert_type(value, node.target_type)

    def visit_AskNode(self, node):
        """Demande une entrée utilisateur"""
        if node.prompt:
            return input(node.prompt + " ")
        else:
            return input()



    def _convert_type(self, value, target_type):
        """Fonction helper pour convertir"""
        if target_type == 'int':
            return int(float(value))  # float() d'abord pour gérer "3.14"

        elif target_type == 'float':
            return float(value)

        elif target_type == 'string':
            # Si c'est un nombre entier, enlever le .0
            if isinstance(value, float) and value.is_integer():
                return str(int(value))
            return str(value)

        elif target_type == 'bool':
            # 0, "", [] → False, tout le reste → True
            return bool(value)

        else:
            raise Exception(f"Type inconnu: {target_type}")

# Test
if __name__ == "__main__":
    from lexer import lexer
    from parser import Parser

    # Test 1: x is 10
    code = "x is 10"
    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse_assignment()

    interpreter = Interpreter()
    result = interpreter.visit(ast)
    print(f"{code} => {result}")
    print(f"Variables: {interpreter.variables}")

    # Test 2: y is 5 + 3
    code = "y is 5 + 3"
    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse_assignment()

    result = interpreter.visit(ast)
    print(f"{code} => {result}")
    print(f"Variables: {interpreter.variables}")
