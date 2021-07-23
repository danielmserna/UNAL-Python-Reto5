def tipos_lamina(laminas):
    laminas_unicas=[]
    for i in laminas:
        if i not in laminas_unicas:
            laminas_unicas.append(i)
    return laminas_unicas

def laminas_faltantes_tipo(numeros_lamina,clases_lamina,lamina):
    return [ i for i in numeros_lamina if lamina ==clases_lamina[i] ]
def me_faltan(laminas_otra_persona,mis_laminas):
    laminas_quiero=[]
    for i in laminas_otra_persona:
        if i not in mis_laminas:
            laminas_quiero.append(i)
    return laminas_quiero

def cambiar(laminas_persona_1,laminas_persona2):
    a = set(laminas_persona_1)
    b = set(laminas_persona2)
    return len(list(b-a)) if len(list(b-a)) < len(list(a-b)) else len(list(a-b))