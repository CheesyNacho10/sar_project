import regex
# query = 'alpargata blanca (coche and ("oh yes" or casa)) and casa or rojo blanco "al caso" or "caso a"'
query = '(pollo and (blanco pie) or not queso) alpargata not blanca (coche and ("oh yes" or casa)) and casa or rojo blanco "al caso" or "caso a"'
parentesis = r'''(?<rec>\((?:[^()]++|(?&rec))*\))'''
comillas = r'''(?<rec>"(?:[^""]++)*")'''

print(query)
queryPar = regex.split(parentesis,query,flags=regex.VERBOSE) # Separar elementos con parentesis
querySep = [] # Lista donde guardaremos las palabras entre comillas como un solo item
for item in queryPar:
    if '(' in item: # si hay parentesis en el elemto, lo guardamos igual
        querySep.append(item)
    elif '\"' in item: # si hay comillas, 
        aux = regex.split(comillas,item,flags=regex.VERBOSE)
        for element in aux:
            if '\"' in element:
                querySep.append(element)
            else:
                querySep += element.split()
    else:
        querySep += item.split()

if '' in querySep: querySep.remove('')

queryFinal = []
needAnd = False # Booleano para saber si hace falta un and
for word in querySep:
    word = word.strip()
    if not needAnd:
        queryFinal.append(word)
        needAnd = True
        if word == 'not':
            needAnd = False
    elif word in ['or','and']:
        queryFinal.append(word)
        needAnd = False
    else:
        queryFinal.append('and')
        queryFinal.append(word)

print(queryFinal)