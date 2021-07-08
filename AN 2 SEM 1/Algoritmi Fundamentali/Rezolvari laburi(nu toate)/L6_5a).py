'''
    Dat un graf NEORIENTAT sa se verifice daca e eulerian
    daca este sa se afiseze un ciclu eulerian
    altfel sa zic de ce nu e eulerian
    verificare grade ca toate sa fie pare
    pt ciclu alg lui Hierholzer
'''
def verific():
    global graf, n, grade
    for i in range (n):
        grade[i]=0

    for l in graf:
        for nod in l:
            grade[nod]+=2
    print(grade)
    for i in range(n):
        if grade[i]%2==1:
            return False
    return True
def Circuit():
    global graf, n
    nr_muchii= dict()#dictionar cu gradele nodurilor
    for i in range(n):
        nr_muchii[i] = len(graf[i])

    #stiva cu noduri
    curent = []
    # vector pentru circuit
    circuit = []

    #incep de la nodul 0
    curent.append(0)
    nod_curent = 0

    while len(curent):
        if nr_muchii[nod_curent]!=0:#daca a mai ramaas vreo muchie
            curent.append(nod_curent)#adaug nodul

            # retin urmatorul nod, pt ca urmeaza sa sterg muchia
            nod_urm = graf[nod_curent][-1]
            nr_muchii[nod_curent] -= 1 #scad nr de muchii
            graf[nod_curent].pop() #scod nodul(auto muchia)

            nod_curent = nod_urm #trec la urmatorul nod
        else:
            circuit.append(nod_curent)#daca nu a mai ramas nicio muchie
                                    #pot adauga nodul in circuit
            nod_curent = curent[-1]#trec la urmatorul nod
            curent.pop()
    print("Circuitul este: ", circuit)

#folosesc lista de adiacenta
#incep numerotarea de la nodul 0!!
n=7
graf=[[1, 6], [2], [0, 3], [4], [2, 5], [0], [4]]
grade = {}
if verific()==True:
    print("Graful este eulerian")
    print("un circuit eulerian este:", end=" ")
    Circuit()
else:
    print("graful NU este eulerian deoarece nodurile: ", end=" ")
    for i in range(n):
        if grade[i]%2==1:
            print(i, end=" ")
    print("au grade impare")