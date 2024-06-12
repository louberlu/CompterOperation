import math
from typing import Tuple
#!/usr/bin/env python3
"""
Ce sous-module contient trois fonctions qui convertissent une ligne de code en une instruction.

Fonctions :
    StringToOpe(ligne): Convertit une ligne de code de la forme Var3 = Var2 OP Var1 en une instruction.
    StringToAffect(ligne): Convertit une ligne de code de la forme Var3 = Var2 en une instruction.
    StringToCond(ligne): Convertit une ligne de code de la forme Var1 OPREL Var2 en une instruction.

Constantes:
    OP: Opérations arithmétiques.
    OPREL: Opérations relationnelles.
    AF: Opérateur d'affectation.
    TANTQUE: Mot-clé while.
    AFFECTATION: Mot-clé Affectation.
    OPERATION: Mot-clé Operation.
    CONDITION: Mot-Clé Condition.
    INFINI: Mot-Clé Bouble Infinie.

Auteurs : NKILI OBELE Karen Fifi
"""

OP = ["+", "-", "*", "/"] # Opérations arithmétiques
OPREL = ["<=", ">=", "=="] # Opérations relationnelles
AF = "=" # Opérateur d'affectation
TANTQUE = "while" # Mot-clé while
AFFECTATION = "Affectation"
OPERATION = "Operation"
CONDITION = "Condition"
INFINI = "Boucle Infinie"


def StringToOpe(ligne):
    """Convertit une ligne de code de la forme Var3 = Var2 OP Var1 en une instruction
    
    Args:
        ligne (str): La ligne de code à convertir.
        
    Returns:
        tuple: Un tuple contenant les éléments de l'instruction, ou None si la ligne est vide.
    """
    try:
        if ligne == "":
            return None
        else:
            tab = ligne.split()
            return (tab[0], tab[1], tab[2], tab[3], tab[4])
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'StringToOpe' : Une erreur inattendue s'est produite : {e}")


def StringToAffect(ligne):
    """Convertit une ligne de code de la forme Var3 = Var2 en une instruction
    
    
    Args:
        ligne (str): La ligne de code à convertir.
        
    Returns:
        tuple: Un tuple contenant les éléments de l'instruction, ou None si la ligne est vide.
    """
    try:
        if ligne == "":
            return None
        else:
            tab = ligne.split()
            return (tab[0], tab[1], tab[2])
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'StringToAffect' : Une erreur inattendue s'est produite : {e}")


def StringToCond(ligne):
    """Convertit une ligne de code de la forme Var1 OPREL Var2 en une instruction
    
    Args:
        ligne (str): La ligne de code à convertir.
        
    Returns:
        tuple: Un tuple contenant les éléments de l'instruction, ou None si la ligne est vide.
    """
    try:
        if ligne == "":
            return None
        else:
            tab = ligne.split()
            return (tab[0], tab[1], tab[2])
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'StringToCond' : Une erreur inattendue s'est produite : {e}")


def IsOpe(ligne):
    """Vérifie si une ligne de code est une opération arithmétique.
    
    Args:
        ligne (str): La ligne de code à vérifier.
        
    Returns:
        bool: True si la ligne est une opération arithmétique, False sinon.
    """
    try:
        tab = ligne.split()
        # Si la ligne contient cinq éléments, que le quatrième est un opérateur 
        # et que le deuxième est un opérateur d'affectation
        if len(tab) == 5:
            if tab[3] in OP and tab[1] == AF:
                return True
        else:
            return False
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'IsOpe' : Une erreur inattendue s'est produite : {e}")
 
 
def IsAffect(ligne):
    """Vérifie si une ligne de code est une affectation.
    
    Args:
        ligne (str): La ligne de code à vérifier.
        
    Returns:
        bool: True si la ligne est une affectation, False sinon.
    """
    try:
        tab = ligne.split()
        # Si le deuxième élément de la ligne est l'opérateur d'affectation 
        # et la ligne contient trois éléments
        if len(tab) == 3:
            if tab[1] == AF:
                return True
        else:
            return False
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'IsAffect' : Une erreur inattendue s'est produite : {e}")

def TakeCond(ligne):
    """Récupère la condition d'un while.
    
    Args:
        ligne (str): La ligne de code à analyser.
    
    Returns:
        str: La condition.
    """
    
    try:
        ligne = ligne.split(")")[0].split('(')[1]
    
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'TakeCond' : Une erreur inattendue s'est produite : {e}")
    return ligne


def IsCond(ligne):
    """Vérifie si une ligne de code est une condition.
    
    Args:
        ligne (str): La ligne de code à vérifier.
        
    Returns:
        bool: True si la ligne est une condition, False sinon.
    """
    try:
        tab = ligne.split()
        
        # Si la ligne contient trois éléments et le deuxième élément est une opération relationnelle
        if len(tab) == 3 :
            if tab[1] in OPREL:
                return True
        else:
            return False
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'IsCond' : Une erreur inattendue s'est produite : {e}")


def AsWhile(bloc):
    """Vérifie si le bloc de texte contient une instruction while.

    Args:
        bloc (str): Le bloc de texte à vérifier.
    
    Returns:
        bool: True si le bloc contient une instruction while, False sinon.
    """
    
    try:
        if TANTQUE in bloc:
            return True
        else:
            return False
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'AsWhile' : Une erreur inattendue s'est produite : {e}")


def TakeWhile(bloc):
    """Récupère l'instruction while d'un bloc de texte.
    
    Args:
        bloc (str): Le bloc de texte à analyser.
    
    Returns:
        tuple: Un tuple contenant le bloc sans l'instruction while et l'instruction while.
    """
    try:
        blocNoW = bloc.split(TANTQUE)[0]+bloc.split("}")[1]
        blocW = TANTQUE+bloc.split(TANTQUE)[1].split("}")[0]+"}"
        return (blocNoW,blocW)
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'TakeWhile' : Une erreur inattendue s'est produite : {e}")

def takeInstructionWhile(bloc):
    """Récupère l'instruction while d'un bloc de texte qui effectue l'itération.

    Args:
        bloc (str): Le bloc de texte à analyser.
    
    Returns:
        tuple: Un tuple contenant la condition et l'instruction de la boucle while.
    """
    try:
        blocs = bloc.split("\n")
        lcond = blocs[0]
        cond = TakeCond(lcond)
        var, OpC, Val = StringToCond(cond)
        instr = None

        for line in blocs[1:]:
            if IsOpe(line):
                varI, OpI, VarI2, Op, VarI1 = StringToOpe(line)
                if varI == var and VarI2 == var:
                    instr = line
        
        return (cond, instr)
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'takeInstructionWhile' : Une erreur inattendue s'est produite : {e}")
             
def takeInitialWhile(bloc):
    """Récupère la instruction d'initialisation du While.

    Args:
        bloc (str): le  bloc à analyser.
    
    Returns:
        str: l'instruction d'initialisation
    """
    try:
        linesNoW, linesW = TakeWhile(bloc)
        linesNoW = bloc.split(TANTQUE)[0] #Le bloc avant le while
        cond,instr = takeInstructionWhile(linesW) #On récupère la condition du while
        var,opR,var2 = StringToCond(cond)
        
        #Cherche la ligne d'affectation
        for line in linesNoW.split('\n'):
            if IsAffect(line): #Vérifie si c'est la ligne d'initialisation
                varA,afA,valA = StringToAffect(line)
                if varA == var:
                    return line

    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'takeInitialWhile' : Une erreur inattendue s'est produite : {e}")


def evaluateWhile(cond, instruction, initial):
    """Évalue l'instruction while. 
    La fonction ne prend en compte que les boucles ayant 
    des conditions de la forme i <= 10 ou i >= 10.
    L'initialisation sera de la forme i = 0.
    Et la fonction peut seulement calculer le nombre de tour de la boucle
    si l'instruction est de la forme i = i + 1 ou i = i * 2 ou i = i - 1, 
    donc incrémentation et la décrémentation de la variable de la condition.
    
    Args:
        cond (str): La condition du while.
        instruction (str): L'instruction du while.
    
    Returns:
        int: Le nombre de tour de la boucle, ou 'Infini' si la boucle est infinie.
    """
    try:
        if instruction == None:
            return INFINI
        it = 0
        varC, OpC, VarC2 = StringToCond(cond)
        varI, OpI, VarI2, Op, VarI1 = StringToOpe(instruction)
        varIn, AfIn, Val2 = StringToAffect(initial)
        
        #Calcule le nombre de tour de la boucle
        if OpC == OPREL[0]: #Si la condition est de la forme i <= 10
            if Op == OP[0]: #Si l'instruction est de la forme i = i + 1
                it = (((int(VarC2) - int(Val2))) // int(VarI1))
            elif Op == OP[1]:
                return INFINI
            elif Op == OP[2]:
                if int(Val2) != 0:
                    it = math.log(int(VarC2) / int(Val2), int(VarI1)) + 1
                else:
                    return 0
        elif OpC == OPREL[1]: #Si la condition est de la forme i >= 10
            if Op == OP[1]: #Si l'instruction est de la forme i = i - 1
                it = ((int(Val2) - int(VarC2)) // int(VarI1)) + 1
            elif Op == OP[0]:
                return INFINI
            elif Op == OP[2]:
                return INFINI
        return int(it)
            
    except AttributeError:
        raise ValueError("Une chaîne de caractères était attendue, mais un autre type a été reçu.")
    except Exception as e:
        print(f"Fonction 'evaluateWhile' : Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    # Exemples de lignes de code
    str1 = "j = i + 1" # Une opération arithmétique
    str2 = "k = j"  # Une affectation
    str3 = "i <= 10"  # Une condition
    pseudo_code = """
    a = 2
    p = a + 3
    while(a <= 10){
        j = i + 1
        k = j
        a = a + 3
    }
    a = 4 + 6
    """  # Un bloc while
    pseudo_code2 = """
    a = 1
    p = a + 3
    while(a <= 10){
        j = i + 1
        k = j
        a = a * 2
    }
    a = 4 + 6
    """

    pseudo_code3 = """
    a = 10
    p = a + 3
    while(a >= 2){
        j = i + 1
        k = j
        a = a - 3
    }
    a = 4 + 6
    """

    blocSansWhile = pseudo_code.split("while")[0]+pseudo_code.split("}")[1]  # Le bloc sans l'instruction while
    
    
    while1 = "while"+pseudo_code.split("while")[1].split("}")[0]+"}"  # L'instruction while
    Cond, Instr = takeInstructionWhile(while1)
    Ini = takeInitialWhile(pseudo_code)
    print(Cond)
    print(Instr)
    print(Ini)
    
    ResW = evaluateWhile(Cond, Instr, Ini)
    print(ResW)

    while2 = """while(a <= 10){
    j = i + 1
    k = j
    a = a * 2
    }"""
    C, I = takeInstructionWhile(while2)
    In = takeInitialWhile(pseudo_code2)
    print(C)
    print(I)
    print(In)
    
    while3 = """while(a >= 2){
        j = i + 1
        k = j
        a = a - 3
    }
    """
    C1, I1 = takeInstructionWhile(while3)
    In1 = takeInitialWhile(pseudo_code3)
    print(C1)
    print(I1)
    print(In1)
    
    ResW2 = evaluateWhile(C, I, In)
    print(ResW2)
    
    a = IsOpe(str1)
    b = IsAffect(str2)
    d = AsWhile(pseudo_code)
    f = IsOpe(str3)
    g = IsAffect(str1)
    h = IsCond(str2)
    
    print(a, b, d, f, g, h)