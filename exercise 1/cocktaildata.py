from gurobipy import *

# Die ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern.

ingredients, prices, alcohol, sugar, calories = multidict({
    "Rum": [1.57, 0.45, 0, 247],
    "Blue_Curacao": [1.41, 0.3, 17, 243],
    "Amaretto": [1.73, 0.28, 30.4, 284],
    "OrangeJuice": [0.99, 0, 8.8, 47],
    })

# ingredients: Liste der Inhaltsstoffe (als str)
# prices: Dictionary der Preise je 100ml: z.B.: prices["Amaretto"]=1.73 
# alcohol: Dictionary des Alkoholgehalts: z.B.: alcohol["Amaretto"]=0.28
# sugar: Dictionary des Zuckergehalts in Gramm je 100ml: z.B.: sugar["Amaretto"]=30.4
# calories: Dictionary der Kalorien in 100ml: z.B calories["Amaretto"]=284


max_alcohol = 0.25 # (25 Prozent)
min_alcohol = 0.15 # (15 Prozent)
min_sugar = 30  # in Gramm
max_calories = 500 # in Kalorien
min_volume = 2.5 # in 100 ml


import cocktailmodel
model = cocktailmodel.solve(ingredients, prices, alcohol, sugar, calories, min_alcohol, max_alcohol, min_sugar, max_calories, min_volume)

if not isinstance(model, gurobipy.Model ):
    print ("Sie haben vergessen das Modellobjekt zurueckzugeben!")