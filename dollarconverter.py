
def converter(type_peso, dollar_value): #esa dos variables (parámetros) tienen de contenido lo que escriba acabo cuando las 'invoque'
    pesos = input("How much " + type_peso + " peso do you have?: ")
    pesos = float(pesos)
    dollar = pesos / dollar_value
    dollar = round(dollar, 2)
    dollar = str(dollar)
    print("That is equivalent to " + dollar + " dollars")
menu = """
Welcome to the currency converter 8)

Opt 1 - Colombian peso
Opt 2 - Argentinian peso
Opt 3 - Mexican peso 

Choose an option: """
option = int(input(menu)) #Con int convertí lo que el usuario escriba en número entero, para no poner entre comillas el número de abajo
if option == 1: #sería "1", de no haber puesto int arriba.
    converter("colombian", 3875) #Aquí se le da el contenido a las variables (parámetros) del def de arriba
elif option == 2:
   converter("argentinian", 120)
elif option == 3:
    converter("mexican", 20)
else:
    print("Don't you read'? type a valid option >:/")





