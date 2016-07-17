#!/usr/bin/python


from gurobipy import *

# diese Methode wird aus den Datenfiles (hier regressionData1.py und regressionData2.py) heraus aufgerufen
# fuehren Sie daher den Code in den Datenfiles aus
def solve(punkte, x_koord, y_koord):
    
    # Model
    model = Model('Regression')    
    
    #!!! Variable var_a soll Steigung der Regressionsgerade angeben!!!
    #!!! Variable var_b soll y-Achsenabschnitt der Regressionsgerade angeben!!!
    #!!! Variable max_y soll maximalen vertikalen Abstand von der Regressionsgerade zu den Punkten angeben!!!
    #!!! Aenderungen des Namens bedeuten 0 Punkte; Changing the name results in getting 0 points !!!
    # ergaenzen Sie ggf. untere und obere Schranken, sowie Zielfunktionskoeffizienten
    var_a = model.addVar( name='a', lb = -GRB.INFINITY)
    var_b = model.addVar( name='b', lb = -GRB.INFINITY)
    max_y = model.addVar( name='max_y_dist', obj=1)

    # ergaenzen Sie hier ggf. neue Variablen
    
    #ergaenzen Sie ab hier bitte keine neuen Variablen mehr
    
    #Minimiere den Abstand
    model.modelSense = GRB.MINIMIZE
    # Update um Variablen bekannt zumachen   
    model.update()

    # ergaenzen Sie ab hier die linearen Nebenbedingungen (aka constraints)
    # !!! Nichtlinearitaeten,im Modell z.B. Multiplikation zweier Entscheidungsvariablen fuehren zu 0 Punkten !!!
    # !!! nonlinearities in the model, e.g., multiplication of two decision variables, result in getting 0 points !!!
    for p in punkte:
        model.addConstr((var_a*x_koord[p] + var_b) - y_koord[p] <= max_y)

    for p in punkte:
        model.addConstr(y_koord[p] - (var_a*x_koord[p] + var_b) <= max_y)

    # ab hier lassen Sie den Code bitte unveraendert, Aenderungen des unteren Codes koennen zu 0 Punkten fuehren
    # making changes in the code below may result in getting 0 points
        
    def printSolution():
        if model.status == GRB.status.OPTIMAL:
           print ('\n Die Regressionsgerade ist y = %g x + %g.' % (var_a.x,var_b.x ))

    # Solve
    model.optimize()
    printSolution()

    return model
