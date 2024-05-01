import time
nome_utente = input("inserisci il tuo nome utente ")
print('ciao '+ nome_utente)
time.sleep(3)
print()
print(nome_utente + ' immetti la tua password')
password1 = input("inserire password: ")
if password1 == 'la tua password':
    print("password errata")
    password2 = input("la password è errata ")
    if password2 == 'errata':
        print("La password è sbagliata")
        password3 = input('prova ancora ')
        if password3 == 'ancora':
            print("mi prendi in giro " + nome_utente + "?")
            time.sleep(5)
        
    
else:
    print("password corretta")
    time.sleep(5)
