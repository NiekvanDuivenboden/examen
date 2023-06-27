#  vraag leeftijd en werkstatuut gebruiker
while True:
    print("wat is je leeftijd?")
    leeftijd = int(input("voer het aantal jaren in: "))

    werkstatuut = ['medewerker', 'zelfstandige', 'ambtenaar']
    werkstatuut = input ("wat is je werkstatuut? \n voer in: medewerker, zelfstandige, ambtenaar: ")

# de keuze van de gebruiker koppelen aan een variabele
    if werkstatuut == 'medewerker' :
        werk = 1
    elif werkstatuut == 'zelfstandige':
        werk = 2
    else:
        werk = 3

#definieer de voorwaarden, het bedrag en print het bedrag dat gebruiker krijgt
    x= 65 - leeftijd
    if leeftijd < int(65):
            print(f"van werken word je gelukkig, je mag nog {x} jaar genieten van je baan.")

    def pensioen (leeftijd, werk):
        if leeftijd >= int(65) and leeftijd < int(70) and werk == 1:
            pensioen1 = '€350'
        if leeftijd >= int(70) and werk == 1:
            pensioen1 = '€370'
        if leeftijd >= int(65) and leeftijd < int(70) and werk == 2:
            pensioen1 = '€300'
        if leeftijd >= int(70) and werk == 2:
            pensioen1 = '€315'
        if leeftijd >= int(65) and leeftijd < int(70) and werk == 3:
            pensioen1 = '€370'
        if leeftijd >= int(70) and werk == 3:
            pensioen1 = '€395'
        return f"je krijgt {pensioen1} per week."
    if leeftijd >= int (65):
        print(pensioen(leeftijd, werk))

# herhaal alle stappen
    print("wil je je pensioen nog eens berekenen? (J/N)")
    ans= input ()
    if ans == 'n' or ans == 'N':
        break











