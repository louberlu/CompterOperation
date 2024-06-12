from Instruction.instruction import IsAffect, IsOpe
from Instruction.instruction import TakeWhile, AsWhile
from Instruction.instruction import takeInitialWhile, evaluateWhile, takeInstructionWhile
from Instruction.instruction import INFINI
"""Ce module comprend des fonctions permettant de compter le nombre d'opérations dans un fichier texte.

Fonctions:
    nbOperation(fichierTxt:str) -> int
    nbOpeWhile(texteWhile:str) -> int

Auteurs : NKILI OBELE Karen Fifi, AGBOSSA YAO Serge
"""
def nbOperation(fichierTxt:str):
    """Récupère le nombre d'opérations dans un fichier texte contenant un pseudo-code.

    Args:
        fichierTxt (str): Le nom et le chemin du fichier texte à lire.

    Returns:
        int: Le nombre d'opérations.
    """
    count = 0
    countW = 0
    try:
        with open(fichierTxt, 'r') as file:
            lines = file.read()
            #Bloc sans la boucle While et le bloc avec la boucle
            linesNoW, linesW = TakeWhile(lines)
            
            #Calcul du nombre de tour de la boucle
            cond,instr = takeInstructionWhile(linesW)
            initial = takeInitialWhile(lines)
            nbT = evaluateWhile(cond, instr, initial)
            
            #Compte le nombre d'opérations dans le bloc de text sans while
            for line in linesNoW.split("\n"):
                if IsOpe(line):
                    count += 1
                elif IsAffect(line):
                    count += 1
            
            #Compte le nombre d'operation dans la boucle while
            if nbT != INFINI:
                for line in linesW.split("\n"):
                    if IsOpe(line):
                        countW += 1
                    elif IsAffect(line):
                        countW += 1
                    elif AsWhile(line):
                        countW += 1
                countW *= nbT
            else:
                return INFINI+" a été trouvé dans votre algorithme"
            
            #Compte le nombre d'opération total
            print("Nombre de tour: ",nbT)
            count+=countW
    except FileNotFoundError:
        raise ValueError("Le fichier spécifié est introuvable.")
    except Exception as e:
        print(f"Fonction 'nbOperation' - Une erreur inattendue s'est produite : {e}")
    return count


if __name__ == "__main__":
    # Exemples de lignes de code
    
    m = nbOperation("exemple.txt")
    print(m)
    n = nbOperation("exemple2.txt")
    print(n)
    l = nbOperation("exemple3.txt")
    print(l)