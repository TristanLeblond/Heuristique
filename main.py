objets = [
{ " nom " : " objet1 " , " poids " : 5 , " valeur " : 10} ,
{ " nom " : " objet2 " , " poids " : 3 , " valeur " : 7} ,
{ " nom " : " objet3 " , " poids " : 2 , " valeur " : 3} ,
{ " nom " : " objet4 " , " poids " : 8 , " valeur " : 20} ,
]

poids_sac = 0
capacite = 10
ratio_valeur_poids = []
objets_sac = []

def heuristique_valeur_poids ( objets , capacite ):
    for obj in objets:
        ratio_valeur_poids.append(obj[" valeur "] / obj[" poids "])

    return objets[ratio_valeur_poids.index(max(ratio_valeur_poids))][" nom "]

def heuristique_valeur ( objets , capacite ):
    n = len(objets)
    dp = [[0 for _ in range(capacite + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacite + 1):
            if objets[i - 1][" poids "] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - objets[i - 1][" poids "]] + objets[i - 1][" valeur "])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacite]


valeur_heuristique1 = heuristique_valeur_poids ( objets , capacite )
valeur_heuristique2 = heuristique_valeur ( objets , capacite )

print ( f" valeur / poids : ␣ { valeur_heuristique1 } " )
print ( f" valeur : ␣ { valeur_heuristique2 } " )
