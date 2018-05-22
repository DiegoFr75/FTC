import re

def validaName(name):
    nameTest = re.search(r'^[a-zA-Z][a-zA-Z0-9]+$',name)
    if nameTest:
        numCont = re.findall(r'\d',name)
        alfaCont = re.findall(r'\D', name)
        if(len(alfaCont) >= len(numCont)):
            return True
        else:
            return False
    else:
        return False

def validaPassword(senha):
    senhaTest = re.search(r'^[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}$',senha)
    if senhaTest:
        senhaSplit = senha.split('.')

        for i in range(4):
            if (senhaSplit[i][0]==senhaSplit[i][1]):
                return False

        for i in range(4):
            testaAlfa = re.findall(r'\d',senhaSplit[i])
            if (len(testaAlfa)==0):
                return False

        return True
    else:
        return False

def validaIp(numIp):
    ipTest = re.search(r'^(1[0-9]{0,2}|([2]?[0-4]?[0-9]|25[0-5]?|[1-9]?[0-9]))\.([1]?[0-9]{1,2}|([2]?[0-4]?[0-9]|25[0-5]?|[1-9]?[0-9]))\.([1]?[0-9]{1,2}|([2]?[0-4]?[0-9]|25[0-5]?|[1-9]?[0-9]))\.([1]?[0-9]{1,2}|([2]?[0-4]?[0-9]|25[0-5]?|[1-9]?[0-9]))$',numIp)
    if ipTest:
        return True
    else:
        return False

def validaMail(email):
    mailTest = re.search(r'^[a-z].+@[a-z]+\.[a-z]+[.]?[a-z]+?',email)
    mailArroba = re.findall(r'@',email)

    if mailTest and len(mailArroba) == 1:
        return True
    else:
        return False

def validaTran(tipo):
    typeTest = re.search(r'(\bpull\b|\bpush\b|\bstash\b|\bfork\b|pop\b)$',tipo)
    if typeTest:
        return True
    else:
        return False

def validaRepos(repo):
    repoTest = re.search(r'^[a-z][_a-z0-9]*[a-z0-9]$',repo)
    if repoTest:
        listRepo = repo.split("_")
        for i in range(len(listRepo)):
            if listRepo[i]=='':
                return False
        return True
    else:
        return False

def validaHash(hash):
    hashTest = re.search(r'^[a-f0-9]{32}$',hash)
    if hashTest:
        return True
    else:
        return False

def validaTudo(listaString):

    if (validaName(listaString[0]) == False):
        return False

    if (validaPassword(listaString[1]) == False):
        return False

    if (validaIp(listaString[2]) == False):
        return False

    if (validaMail(listaString[3]) == False):
        return False

    if (validaTran(listaString[4]) == False):
        return False

    if (validaRepos(listaString[5]) == False):
        return False

    if (validaHash(listaString[6]) == False):
        return False

    return True

try:
    recebeString = input()

    listaString = recebeString.split(" ")
    if len(listaString)==7:
        print(validaTudo(listaString))
    else:
        print(False)

except EOFError:
    print(False)





