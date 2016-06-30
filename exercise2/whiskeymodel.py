#!/usr/bin/python

from gurobipy import *


# diese Methode wird aus den Datenfiles (hier whiskeydata1 und whiskeydata2) heraus aufgerufen
# fuehren Sie daher den Code in den Datenfiles aus

def solve(sorten, kosten, max_import, mischungen, erloes, min_amount, max_amount):
    # Model
    model = Model("whiskey")
    
    x = {}
    for s in sorten:
        for m in mischungen:
            #!!! Mischungsvariablen x[s,m] entsprechen der Menge (Volumen), die von Sorte s fuer die Mischung m verwendet wird in Liter!!!
            #!!! Aenderungen des Namens bedeuten 0 Punkte; Changing the name results in getting 0 points !!!
            # ergaenzen Sie ggf. untere und obere Schranken, sowie Zielfunktionskoeffizienten
            x[s,m] = model.addVar(name= "x_"+s+"_"+m, obj=erloes[m]-kosten[s])
    
    # ergaenzen Sie hier ggf. neue Variablen


    #ergaenzen Sie ab hier bitte keine neuen Variablen mehr

    #Maximiere den Gewinn
    model.modelSense = GRB.MAXIMIZE;

    model.update()

    # ergaenzen Sie ab hier die linearen Nebenbedingungen (aka constraints)
    # !!! Nichtlinearitaeten,im Modell z.B. Multiplikation zweier Entscheidungsvariablen fuehren zu 0 Punkten !!!
    # !!! nonlinearities in the model, e.g., multiplication of two decision variables, result in getting 0 points !!!
    for m in mischungen:
        for s in sorten:
            model.addConstr(x[s,m] >= min_amount[s,m]*quicksum(x[s,m] for s in sorten))
        
    for m in mischungen:
        for s in sorten:
            model.addConstr(x[s,m] <= max_amount[s,m]*quicksum(x[s,m] for s in sorten))
    
    for s in sorten:
        model.addConstr(quicksum(x[s,m] for m in mischungen) <= max_import[s])



    # ab hier lassen Sie den Code bitte unveraendert, Aenderungen des unteren Codes koennen zu 0 Punkten fuehren
    # making changes in the code below may result in getting 0 points

    def printSolution():
        if model.status == GRB.status.OPTIMAL:
            print "Profit: %.7g" % model.ObjVal
            for s in sorten:
                for m in mischungen:
                    if x[s,m].x > 0.0001:
                        print('\nVon Sorte %s werden %g Liter in Mischung %s verwendet.' % (s, x[s,m].x, m))
        else:
            print('Keine Loesung gefunden')

    # Solve
    model.optimize()
    printSolution()
