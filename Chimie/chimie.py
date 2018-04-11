def extract_atoms(atoms_string):
    pile = [[]]
    context = pile[0]
    pass_until = -1

    # Parcours de la chaine
    for iter_atom in range(len(atoms_string)):
        if (not(pass_until != -1 and iter_atom <= pass_until)):
            act_char = atoms_string[iter_atom]

            if (act_char.isalpha()):
                # On ajoute la lettre
                # Si y a une minuscule apres
                if (iter_atom + 1 < len(atoms_string) and atoms_string[iter_atom + 1].islower()):
                    act_char = act_char + atoms_string[iter_atom + 1]
                    pass_until = iter_atom + 1
                context.append({act_char: 1})

            elif(act_char.isnumeric()):
                # Pour un chiffre on multiplie le ou les précédents par ce chiffre
                act_char = int(act_char)
                dico_tmp = {}

                # On multiplie le dernier élément du contexte actuel
                for atom, nb in context[-1].items():
                    dico_tmp[atom] = nb * act_char
                context[-1] = dico_tmp

            elif(act_char == "("):
                # On entre dans un nouveau contexte
                pile.append([])
                context = pile[-1]

            elif(act_char == ")"):
                # On sort d'un contexte
                group = {}
                for group_iter in context:
                    for atom, nb in group_iter.items():
                        nb_ini = 0
                        if (atom in group):
                            nb_ini = group[atom]
                        group[atom] = nb_ini + nb
                pile = pile[:-1]

                # On se place dans le nouveau contexte
                context = pile[-1]

                # On ajoute le contexte duquel on est sorti
                context.append(group)

            elif(act_char == " " or act_char == "+"):
                # Que ce soit accorcher ou pas ballec
                pass
            else:
                print("UNKNOWN")

    # On sort le resultat du contexte et on somme tout
    res = {}
    for group in context:
        for atom, nb in group.items():
            nb_ini = 0
            if(atom in res):
                nb_ini = res[atom]
            res[atom] = nb_ini + nb
    return res


data_in = "C2H4O + H2O -> (CH2OH)2"
data = data_in.split("->")
atom_res = []
for i in range(2):
    data[i] = data[i].strip()
    atom_res.append(extract_atoms(data[i].strip()))

error = False
for atom, nb in atom_res[0].items():
    if(not(atom in atom_res[1] and nb == atom_res[1][atom])):
        error = True
        break
print("Reaction OK ?", not(error))
print(atom_res[0])
print(atom_res[1])

print(extract_atoms("(CH3(CH2)3O)2"))