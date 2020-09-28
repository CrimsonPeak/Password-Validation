import passwortValidierer as pw

pword = False
while(pword == False):
    print("Ihr Passwort muss mindestens 5 Zeichen lang sein und mindestens eine Zahl, ein Sonderzeichen, einen Großbuchstaben und einen Kleinbuchstaben enthalten.")
    print("Geben Sie das Passwort ein:")
    passw = input()
    if(pw.passwordContainsDigits(passw) == True & pw.passwordContainsUppercase(passw) == True & pw.passwordContainsLowercase(passw) == True & pw.passwordContainsSpecialCharacters(passw) == True & pw.passwordLength(passw) == True):
        print("Ihr Passwort wurde akzeptiert.")
        pword = True
    else:
        print("Ihr Passwort wurd nicht akzeptiert.")
        pword = False