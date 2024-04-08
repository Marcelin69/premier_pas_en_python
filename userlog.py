user = "marceli"
userName = ["marceline",  "julia", "alex", "michael", "natalie"]
adminName = ["marcelin","alex", "natalie", "julia"]



if  user in userName:
    print("bonjour", user)
elif user in adminName :
    print("bonjour et beinvenue dans l'interface administrateur")
else:
    print("utilisateur inconnu, veuillez vous inscrire.")