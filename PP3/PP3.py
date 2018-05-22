def turingMachine(tape_1, tape_2, tape_3, heads):
    state = "q1"
    while(state != "accept" and state != "reject"):
        if(state == "q1"):
            state = q1(tape_1, tape_2, tape_3, heads)
        elif (state == "q2"):
            state = q2(tape_1, tape_2, tape_3, heads)
        elif (state == "q3"):
            state = q3(tape_1, tape_2, tape_3, heads)
        elif (state == "q4"):
            state = q4(tape_1, tape_2, tape_3, heads)
        elif (state == "q5"):
            state = q5(tape_1, tape_2, tape_3, heads)
        elif (state == "q6"):
            state = q6(tape_1, tape_2, tape_3, heads)
        elif (state == "q7"):
            state = q7(tape_1, tape_2, tape_3, heads)
        elif (state == "q8"):
            state = q8(tape_1, tape_2, tape_3, heads)
        elif (state == "q9"):
            state = q9(tape_1, tape_2, tape_3, heads)
        elif (state == "q10"):
            state = q10(tape_1, tape_2, tape_3, heads)
    if(state == "accept"):
        accept(tape_1, tape_2)
    if(state == "reject"):
        reject(tape_1)


def q1(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        tape_2.append("V")
        tape_2[heads[1]] = "I"
        heads[0] += 1
        heads[1] += 1
        return "q2"
    else:
        return "reject"

def q2(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        tape_2.append("V")
        tape_2[heads[1]] = "I"
        heads[0] += 1
        heads[1] += 1
        return "q2"
    elif( (tape_1[heads[0]] == "#") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        tape_2.append("V")
        tape_2[heads[1]] = "#"
        heads[0] += 1
        heads[1] += 1
        return "q3"
    else:
        return "reject"

def q3(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        tape_2.append("V")
        tape_3.append("V")
        tape_2[heads[1]] = "I"
        tape_3[heads[2]] = "I"
        heads[0] += 1
        heads[1] += 1
        heads[2] += 1
        return "q4"
    else:
        return "reject"

def q4(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        tape_2.append("V")
        tape_3.append("V")
        tape_2[heads[1]] = "I"
        tape_3[heads[2]] = "I"
        heads[0] += 1
        heads[1] += 1
        heads[2] += 1
        return "q4"
    elif( (tape_1[heads[0]] == "V") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        heads[0] -= 1
        heads[1] -= 1
        heads[2] -= 1
        return "q5"
    else:
        return "reject"

def q5(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "I")):
        tape_2[heads[1]] = "V"
        heads[0] -= 1
        heads[1] -= 1
        heads[2] -= 1
        return "q5"
    elif( (tape_1[heads[0]] == "#") and (tape_2[heads[1]] == "#") and (tape_3[heads[2]] == "V") ):
        tape_2[heads[1]] = "V"
        heads[0] -= 1
        heads[1] -= 1
        return "q6"
    else:
        return "reject"

def q6(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "V") ):
        heads[0] -= 1
        heads[1] -= 1
        return "q6"
    elif( (tape_1[heads[0]] == "V") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        heads[0] += 1
        heads[1] += 1
        heads[2] += 1
        return "q7"
    else:
        return "reject"

def q7(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "I") ):
        heads[1] += 1
        heads[2] += 1
        return "q7"
    elif( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "I") ):
        heads[0] += 1
        heads[1] -= 1
        heads[2] -= 1
        return "q8"
    elif( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "V") ):
        heads[1] += 1
        return "q9"
    else:
        return "reject"

def q8(tape_1, tape_2, tape_3, heads):
    return "accept"

def q9(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "V") ):
        heads[1] += 1
        return "q9"
    elif( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        heads[1] -= 1
        heads[2] -= 1
        return "q10"
    else:
        return "reject"

def q10(tape_1, tape_2, tape_3, heads):
    if( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "V") ):
        heads[1] -= 1
        return "q10"
    elif( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "I") and (tape_3[heads[2]] == "I") ):
        tape_2[heads[1]] = "V"
        heads[1] -= 1
        heads[2] -= 1
        return "q10"
    elif( (tape_1[heads[0]] == "I") and (tape_2[heads[1]] == "V") and (tape_3[heads[2]] == "V") ):
        heads[1] += 1
        heads[2] += 1
        return "q7"
    else:
        return "reject"

def accept(tape_1, tape_2):
    i = 1
    while(tape_1[i]!= "V"):
        print(tape_1[i],end = "")
        i+= 1
    print("=",end="")
    i = 1
    while(tape_2[i]!= "V"):
        print(tape_2[i],end="")
        i+=1
    print(" ACEITA")


def reject(tape_1):
    i = 1
    while (tape_1[i] != "V"):
        print(tape_1[i], end="")
        i += 1
    print("=", end="")
    print("REJEITA")


#Pegando a entrada e colocando "V" de vazio nos extremos
tape_1 = list(input())
tape_1.insert(0,"V")
tape_1.append("V")

tape_2 =["V","V"]
tape_3 =["V","V"]

heads = [1,1,1]
turingMachine(tape_1, tape_2, tape_3, heads)