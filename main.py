from tkinter import *

# Importa el módulo tkinter.ttk y sobrescribe automáticamente todos los widgets de tkinter
from tkinter.ttk import *

window= Tk()

# window.geometry("500x500")

window.config(padx=20, pady=20)

#titulo para nuestra app
window.title("MILES TO KILOMETERS CONVERTER")

#label guiando al usuario 
user_info=Label(window, text="Enter the data to convert").grid(row=0, column=2)


#ENTER WIDGET
#instancia de la clase StringVar.necesario para almacenar el dato del usuario
user_data=StringVar()
# Devuelve el texto ingresado por el usuario  como una cadena. 
user_data_get=user_data.get()
#boton de entrada de datoscls
data_entry=Entry(window, textvariable=user_data, width=10).grid(row=1, column=2)

#funcion para determinar si un dato es o no un float 
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
      

#funcin que hace la conversion de miles a kilometros
def calculate():
    # Devuelve el texto ingresado por el usuario  como una cadena. 
    user_data_get=user_data.get()
    
    #evaluamos si el dato ingresado por el usuario es un string or u entero
    if user_data_get.isdigit():
        #convertimos el dato a entero
        user_data_get=int(user_data_get)
    
    elif is_float(user_data_get):
        
        user_data_get=float(user_data_get)
    else:
        error_label=Label(window, text=" YOU DIDN'T ENTER A DIGIT ", relief=RAISED).grid(row=2, column=2)
        
    #print para probar que estamos rescatando el dato ingresado por el usario de manera correcta mostrando el dato en consola
    # print(f"user infor {user_data_get}") 
    
    #convirtiendo de millas a km
    result_km=user_data_get*1.6
    
    #MOSTRAR  RESULTADO EN KM
    result.config(text=f"{round(result_km, 2)}")
    
#LABEL "MILES"
to_miles_label=Label(window, text="to miles").grid(row=1, column=3)


#LABEL "IS IQUAL TO"
is_iqual_to=Label(window, text="is iqual to", font=('calibre',10,'bold')).grid(row=2, column=1)

#MOSTRAR  RESULTADO EN KM
result=Label(window, text='0')
result.grid(row=2, column=2)
    
#LABEL "KM"
kilimeter_label=Label(window, text="Km").grid(row=2, column=3)
    

#BOTON CALCULAR
Button(window, text='Calculate', command=calculate).grid(row=3, column=2)




    
    






window.mainloop()