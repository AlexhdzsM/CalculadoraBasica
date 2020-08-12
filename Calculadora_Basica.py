from tkinter import *

"""Calculadora Basica-----------------------
inicia en 0, los numero se introducen presionando los botones
sumas, restas, multiplicaciones y divisiones
DEL=es para borrar y volver a poner en 0"""
#--------------------------------------------------------------------------
raiz=Tk()
raiz.title("Calculadora basica")
raiz.config(bg="gray")
miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bd=10)
miFrame.config(relief="groove")
miFrame.config(bg="black")

operacion=""

reset_pantalla=False

resultado=0


#-------------pantalla----------------------------------------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")
numeroPantalla.set("0")
#---------------------Borrado------------------------------------------------------------------
def borrar():
	global operacion
	global reset_pantalla
	global resultado

	operacion=""

	reset_pantalla=False

	resultado=0

	numeroPantalla.set("0")


#-------------------pulsaciones teclado---------------------------------------------------------------

def numeroPulsado(num):

	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False
	elif numeroPantalla.get()=="0" and num=="0":
		numeroPantalla.set("0")

	elif numeroPantalla.get()=="0" and num!="0":
		numeroPantalla.set(num)

	else:
	
		numeroPantalla.set(numeroPantalla.get() + num)


#----------------funcion suma----------------------------------

def suma(num):

	global operacion

	global resultado

	global reset_pantalla

	resultado+=float(num) 

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)



#---------------funcion resta------------------------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=float(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-float(num)

		else:

			resultado=float(resultado)-float(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*float(num)

		else:

			resultado=float(resultado)*float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+float(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))

		resultado=0

		contador_divi=0

	




#-------------fila 1---------------------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton7.config(bg="black", fg="white")

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton8.config(bg="black", fg="white")

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
boton9.config(bg="black", fg="white")

botonDiv=Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)
botonDiv.config(bg="black", fg="white")


#-------------fila 2---------------------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton4.config(bg="black", fg="white")

boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton5.config(bg="black", fg="white")

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
boton6.config(bg="black", fg="white")

botonMult=Button(miFrame, text="x", width=3, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=3, column=4)
botonMult.config(bg="black", fg="white")

#-------------fila 3---------------------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton1.config(bg="black", fg="white")

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton2.config(bg="black", fg="white")

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
boton3.config(bg="black", fg="white")

botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)
botonRest.config(bg="black", fg="white")


#-------------fila 4---------------------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
boton0.config(bg="black", fg="white")

botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonComa.config(bg="black", fg="white")

botonSum=Button(miFrame, text="+", width=8, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=3, columnspan=2)
botonSum.config(bg="black", fg="white")

#----------------------------------fila5----------------------------------------
botondel=Button(miFrame,text="DEL", width=8, command=lambda:borrar())
botondel.grid(row=6, column=1, columnspan=2)
botondel.config(bg="red")
botonIgual=Button(miFrame, text="=", width=8, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3, columnspan=2)
botonIgual.config(bg="blue")




"Ejecutar programa"
raiz.mainloop()