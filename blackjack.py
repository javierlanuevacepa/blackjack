import random
import time 


loop1=0
loop2=0
loop3=0
saldo=0
gagrit=0
apuesta=0
option = ""


carta=int(1)
carta_crupier=int(1)
#{}

print("------BIENVENIDO AL BLACKJACK DE LA NUEVA CEPA WESKER!!!!!!!!!!!------")

while loop1==0 :
    loop1=0

    print("(1) Ingresar dinero ")
    print("(2) Blackjack ")
    print("(4) Ver Saldo ")
    print("(5) Salir ")
 
    escoger=input("Elija su opcion:")

    if escoger not in ("1" , "2" , "3" , "4" , "5"):
        print("Ingrese un caracter valido ! ")
        

    if escoger=="1":
        print("(1) 500  $")
        print("(2) 1000 $")
        print("(3) 3000 $")
        print("(4) 5000 $")
        option=input("Ingrese cuanto saldo quiere cargar:")
        if option not in ("1" , "2" , "3" , "4"):
            print("Ingrese una opcion valida ")
        

        if option=="1":
            saldo=saldo+500
            print("Usted cargo 500$ correctamente")
        if option=="2":
            saldo=saldo+1000
            print("Usted cargo 1000$ correctamente")
        if option=="3":
            saldo=saldo+3000
            print("Usted cargo 3000$ correctamente")
        if option=="4":
            saldo=saldo+5000
            print("Usted cargo 5000$ correctamente")

        
        
        
    if escoger=="2":
        
        
        print("********BLACKJACK********")
        print("(1) 500  $")
        print("(2) 1000 $")
        print("(3) 3000 $")
        print("(4) 5000 $")
        escoger=input("Elige cuanto quiere apostar: ")
        if escoger not in ("1" , "2" , "3" , "4"):
            loop1+=1
            print("Ingrese un numero valido ! ")

        if apuesta<saldo:
            loop1+=1
            print("No te alcanza")
        if escoger=="1":

            apuesta=500
            print(f"Apuesta:" , apuesta)
        if option=="2":
            apuesta=1000
            print(f"Apuesta:" , apuesta)
        if option=="3":
            apuesta=3000
            print(f"Apuesta:" , apuesta)
        if option=="4":
            apuesta=5000
            print(f"Apuesta:" , apuesta)



        if apuesta>saldo:
            print(" No tiene saldo suficiente. ")
            loop1+=1
        if apuesta<=saldo:
            print(f"Tu apuesta es de {apuesta}")








        while loop2==0:
            print("Tienes: ", carta )    
            j=int(input("Escoge(1) Otra (2)retirarse: " ))
            if j==1:
                carta_kake=random.randint(1,13)
                print("Te salio: " , carta_kake)
                carta=carta+carta_kake
                print("Tienes: ", carta)
            if j==2:
                loop2=loop2+1
                print(" Foldeaste, tus cartas son en total: ", carta )
            if carta==21:
                print("Sacaste 21 !!!!!!!!!!!")
                loop2=loop2+1
            if carta>21:
                loop2=loop2+1
                gagrit=gagrit+1
                saldo=saldo-apuesta
            

        if carta>21:
            print("Perdiste !!!! ")
             


        while gagrit==0:

            print(" crupier tiene : " , carta_crupier)
            carta_kake=random.randint(1,13)
            print("al crupier le salio : " , carta_kake)
            carta_crupier=carta_crupier+carta_kake
            print("Tiene : ", carta_crupier)
            time.sleep(3)

            if carta>21:
                gagrit=gagrit+1

            if carta_crupier>carta and carta_crupier<=21:
                print(" --Crupier foldea y gana tiene carta mayor-- ")
                saldo=saldo-apuesta
                gagrit=gagrit+1
                
            if carta==carta_crupier:
                print("EMPATE !!!!!!!!")
               
                gagrit=gagrit+1

            if carta_crupier==21:

                saldo=saldo-apuesta
                gagrit=gagrit+1 
                print("--Crupier saco 21 !!!!!!!!!!--")
                print("----Perdiste----")
            

            elif carta_crupier>21 and carta_crupier>carta:
                gagrit=gagrit+1 
                saldo=saldo+apuesta
                
                print("--Crupier perdio-- ")
                print("----Ganaste----")
            
       
        apuesta=0
        carta=int(1)
        carta_crupier=int(1)
        loop2=0
        gagrit=0
        
                


    if escoger=="4":
        print(f"Tu saldo es:{saldo}")
    
    if escoger=="5":
        loop1+=1
        print("--Apagando el programa--")
        

            





        
