"""
    Ce package contient des modules pour gérer les instructions 
    et compter les opérations.
"""

# Importer des fonctions spécifiques du module instruction dans le package Instruction
from .Instruction.instruction import StringToAffect, StringToCond, StringToOpe
from .Instruction.instruction import IsAffect, IsCond, IsInstr

# Importer des fonctions liées aux opérations 'while' du module instruction
from .Instruction.instruction import AsWhile, TakeWhile

# Importer des fonctions liées aux listes d'instructions du module instruction
from .Instruction.instruction import listeInstruction, listeInstructionWhile

# Importer des constantes liées aux opérations du module instruction
from .Instruction.instruction import TANTQUE, OP, OPREL, AF

# Importer des fonctions liées au comptage des opérations du module countOperation
from .countOperation import nbOperation

__all__ = ['StringToAffect', 'StringToCond', 'StringToOpe', 'IsAffect', 'IsCond', 
           'AsWhile', 'TakeWhile', 'listeInstruction', 'listeInstructionWhile', 
           'TANTQUE', 'OP', 'OPREL', 'AF', 'nbOperation']