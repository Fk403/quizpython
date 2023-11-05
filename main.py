# Question et Reponse pour le sujet de python 
questions_python = {
"Quelle est la fontion qui permet d'affiche du texte en python ? ":["print()","input()","write()","read()"],
"Quel operateur est opérateur est utilisé pour l'addition en python? ":["+","-","/","*" ],
"Quelle est la premier méthode pour ajouter un élément à une liste en python? ": [".append()",".add()",".insert()",".extend" ],
}

question_mathematique = {
    "Quel est le resultat de 2 + 2 ? " : ["4","50","90"],
    "Quelle est la racine carrée de 9 ": ["3","40","77"],
    "Quel est le perimètre d'un carrée de côte 5 unites": ["20","3","67"],
}

question_physique = {
    "Quel est l'unité de mesure de la force ?":["Newton","volt","Joule"],
    "Rapeler la loi d'ohme":["U = R * I","U = R/I","U = R % I"],
    "Quel est l'unité de mesure de la frenquence ?":["hertz","volt","tomme"],
}

#Recupération de la liste des question   de chaque sujet donné

def get_questions(sujet):

    questions = {
        "mathématiques":question_mathematique,
        "physiques":question_physique,
        "python":questions_python,
    }
    return questions
print(get_questions("test"))
#Poser une question et demander au joueur de repondre

# def ask_question(question,reponses):
#     print(question)
#     for i, reponse in enumerate(reponses,start=1):
#         print(f"{i}.{reponse}")
# #Faire une boucle de choix des reponse de l'utilisateur 
#     while True:
#         try:  
#             choix = int(input("Votre choix (1, 2, 3, 4) :"))
#             if choix < 1 or choix > 4:
#                 raise ValueError 
#             break 
#         except ValueError: 
#             print("Veuillez saisir un nombre entre 1 et 4")
#     return choix 

 #print(ask_question("test","test"))

#jouer un quizz en fontion du sujet

# def jouer_quizz(sujet):
#     pass















