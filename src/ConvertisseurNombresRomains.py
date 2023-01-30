def convertir(nombre):
    if nombre <= 3:
        return 'I' * nombre

    if nombre == 4:
        return 'IV'

    if nombre <= 8:
        return 'V' + 'I' * (nombre - 5)

    if nombre == 9:
        return 'IX'

    if nombre <= 13:
        return 'X' + 'I' * (nombre - 10)

    raise Exception('unexpected number')


def cas_symbole_plus_n_unites(symbole, valeur_symbole, nombre_arabe):
    return symbole + 'I' * (nombre_arabe - valeur_symbole)
