#########################################################################
# ___-___-___- Classes pour représenter les nœuds de l'AST -___-___-___ #
#########################################################################

# PROGRAM NODE
class ProgramNode:
    def __init__(self, statements):
        self.statements = statements  # Liste d'instructions

    def __repr__(self):
        return f"ProgramNode({len(self.statements)} instructions)"


# NUMBER NODE
class NumberNode:
    def __init__(self, value):
        self.value = float(value)

    def __repr__(self):
        return f"NumberNode({self.value})"


# STRING NODE
class StringNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"StringNode({self.value})"


# IDENTIFIER NODE
class IdentifierNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"IdentifierNode({self.name})"


# BINARY OP NODE
class BinaryOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOpNode({self.left} {self.operator} {self.right})"


# ASSIGNMENT NODE
class AssignmentNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return f"AssignmentNode({self.variable} = {self.value})"


# SAY NODE
class SayNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"SayNode({self.value})"


# COMPARISON NODE
class ComparisonNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"ComparisonNode({self.left} {self.operator} {self.right})"


# IF NODE
class IfNode:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch  # Liste d'instructions
        self.else_branch = else_branch  # Liste d'instructions (optionnel)

    def __repr__(self):
        return f"IfNode(if {self.condition} then {len(self.then_branch)} stmts else {len(self.else_branch) if self.else_branch else 0} stmts)"


# CONVERT NODE (pour "convert x to int")
class ConvertNode:
    def __init__(self, variable, target_type):
        self.variable = variable  # Nom de la variable (string)
        self.target_type = target_type  # 'int', 'string', 'bool'

    def __repr__(self):
        return f"ConvertNode({self.variable} to {self.target_type})"


# CAST NODE (pour "x as int")
class CastNode:
    def __init__(self, expression, target_type):
        self.expression = expression  # Expression à convertir
        self.target_type = target_type

    def __repr__(self):
        return f"CastNode({self.expression} as {self.target_type})"


# ASK NODE
class AskNode:
    def __init__(self, prompt):
        self.prompt = prompt  # Message à afficher (optionnel)

    def __repr__(self):
        return f"AskNode({self.prompt})"



# WHILE NODE
class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileNode(while {self.condition} then {self.body})"



#° # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #