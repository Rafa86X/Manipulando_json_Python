import json

f = open("aquario.json", encoding="utf8")
aquario = json.load(f)
animais = aquario["data"]

def printa_bixo(tipoDePeixe, nuntanque):
    i=0
    peixeSelecionado = []
    
    for animal in animais:
        if animal["type"] == tipoDePeixe:
            p = animais[i]
            p['tank number'] = nuntanque
            peixeSelecionado.append(p)                    
        i=i+1
    return peixeSelecionado

print('\n',printa_bixo('fish',42))
print('\n',printa_bixo('shellfish',38))
print('\n',printa_bixo('turtle',17),'\n')

