#!/usr/bin/python

from gurobipy import *


# diese Methode wird aus den Datenfiles (hier transportdata1.py und tranpsortdata2.py) heraus aufgerufen
# fuehren Sie daher den Code in den Datenfiles aus
def solve(staedte, gueter, kosten, distanz,
                kapazitaet, verfuegbar, bedarf):
    # Model
    model = Model("transport")

    x = {}
    for s1 in staedte:
        for s2 in staedte:
            for k in gueter:
                #!!! Variablen x[s1,s2,k] entsprechen der Anzahl an Chargen von Gut k, die von Stadt s1 zu Stadt s2 transportiert werden!!!
                #!!! Aenderungen des Namens bedeuten 0 Punkte; Changing the name results in getting 0 points !!!
                # ergaenzen Sie ggf. untere und obere Schranken, sowie Zielfunktionskoeffizienten
                x[s1, s2, k] = model.addVar(name="x_"+s1+"_"+s2+"_"+k, obj=kosten[k]*distanz[s1,s2])

    # ergaenzen Sie hier ggf. neue Variablen




    #ergaenzen Sie ab hier bitte keine neuen Variablen mehr

    #Minimiere die Kosten    
    model.modelSense = GRB.MINIMIZE
    # Update um Variablen bekannt zumachen    
    model.update()

    # ergaenzen Sie ab hier die linearen Nebenbedingungen (aka constraints)
    # !!! Nichtlinearitaeten,im Modell z.B. Multiplikation zweier Entscheidungsvariablen fuehren zu 0 Punkten !!!
    # !!! nonlinearities in the model, e.g., multiplication of two decision variables, result in getting 0 points !!!
    for s1 in staedte:
        for k in gueter:
            model.addConstr(quicksum(x[s2, s1, k] for s2 in staedte) + verfuegbar[s1, k] >= bedarf[s1, k], "Bedarf von"+k+"in "+s2)
    
    for s1 in staedte:
        for s2 in staedte:
            for k in gueter:
                model.addConstr(x[s1, s2, k] <= kapazitaet[s1, s2], "Kapazitaet von "+k+"von "+s1+"nach "+s2)
                
    for s1 in staedte:
        for k in gueter:
            model.addConstr(quicksum(x[s1, s2, k] for s2 in staedte) <= verfuegbar[s1, k], "Verfuegbarkeit von "+k+"in "+s1)

    

    # ab hier lassen Sie den Code bitte unveraendert, Aenderungen des unteren Codes koennen zu 0 Punkten fuehren
    # making changes in the code below may result in getting 0 points

    def printSolution():
        if model.status == GRB.status.OPTIMAL:
            print "Transportkosten: %.7g" % model.ObjVal
            for s1 in staedte:
                for s2 in staedte:
                    for k in gueter:
                        if x[s1, s2, k].x > 0.0001:
                            print ('\nVon %s nach %s werden %g Chargen %s transportiert.' % (s1,s2, x[s1, s2, k].x, k))
    # Solve
    model.optimize()
    printSolution()
