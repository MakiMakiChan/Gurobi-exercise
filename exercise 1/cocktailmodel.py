# coding=utf-8

from gurobipy import *



# diese Methode wird aus den Datenfiles (hier cocktaildata und cocktaildata2) heraus aufgerufen
# fuehren Sie daher den Code in den Datenfiles aus
  
def solve(ingredients, prices, alcohol, sugar, calories, min_alcohol, max_alcohol, min_sugar, max_calories, min_volume):

    model = Model("Cocktail")

    x = {}
    for i in ingredients:
        #!!! x[i] entspricht der Menge (Volumen), die von Inhaltsstoff i zum Mischen des Cocktails verwendet wird (in 100 ml) !!!
        #!!! Aenderungen des Namens bedeuten 0 Punkte; Changing the name results in getting 0 points !!!
        # ergänzen Sie ggf. untere und obere Schranken, sowie Zielfunktionskoeffizienten
        x[i] = model.addVar(name="x_%s" % i, obj = prices[i]) 
  
   
    
    model.update()
    model.setObjective(x[i] * min_volume * prices[i], GRB.MINIMIZE) 
    # ergaenzt hier die linearen Nebenbedingungen (aka constraints):
    # !!! Nichtlinearitaeten,im Modell z.B. Multiplikation zweier Entscheidungsvariablen fuehren zu 0 Punkten !!!
    # !!! nonlinearities in the model, e.g., multiplication of two decision variables, result in getting 0 points !!!
    model.addConstr(quicksum(alcohol[i] for i in alcohol) >= min_alcohol)
   # model.addConstr(quicksum(alcohol[i] for i in alcohol) <= max_alcohol)
    model.addConstr(quicksum(sugar[i] for i in sugar) >= min_sugar)
  #  model.addConstr(quicksum(calories[i] for i in calories) <= max_calories)
   # model.addConstr(quicksum(vol))
    model.update()
    
    
    
    
    
    
    
    # ab hier lassen Sie den Code bitte unveraendert, Aenderungen des unteren Codes koennen zu 0 Punkten fuehren
    # making changes in the code below may result in getting 0 points
    
    model.optimize()

    def print_model():
        if model.status == GRB.OPTIMAL:
            print "Preis des Cocktails: %g" % model.ObjVal
            for i in ingredients:
                print "Menge von %s im Cocktail: %g" % (i, x[i].X)
        else:
            print "No solution found. Status of model is: %i" % model.status
 
    print_model()

    return model
