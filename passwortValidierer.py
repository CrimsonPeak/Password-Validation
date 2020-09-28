# Passwort Validierer
# 5 Funktionen zur Prüfung / Validierung eines passwort (enthält Zahl, Großbuchstabe, ...)
# Es sollen die Funktionen für die Abfrage 
# - enthält das Passwort Sonderzeichen?
# - enthält das Passwort eine Zahl?
# - enthält das Passwort Grpßbuchstaben?
# - enthält das Passwort Kleinbuchstaben?
# - Passwort ist mindestens 6 Zeichen lang

def passwordContainsDigits(password):
    for z in password:
        if(z.isdigit()):
            return True
    return False

def passwordContainsUppercase(password):
    for z in password:
        if(z.isupper()):
            return True
    return False

def passwordContainsLowercase(password):
    for z in password:
        if(z.islower()):
            return True
    return False

def passwordContainsSpecialCharacters(password):
    sonderzeichen = "[-@_!#$%^&*()<>?/\|}{~:]"
    for z in password:
        if z in sonderzeichen:
            return True
    return False

def passwordLength(password):
    if(len(password) >= 5):
        return True
    return False