from tkinter import *

ventana = Tk()

colorFondo ='#30475E'
colorTablero = '#E05D5D'
colorCabecera = '#CA3E47'
colorTitulo = '#00A19D'
colorTextoCabecera = 'white'
colorTexto = '#FFB344'
colorCasilla = 'white'
colorTablaPuntos = '#30475E'
colorPuntos =  'white'

ventana.attributes('-alpha',0.9) #transparencia de la ventana

pantallaInicio = Frame(ventana , border = 0  , bg = colorFondo ,  height = 800 , width = 800)
Tablero = Frame(ventana , border = 0 , bg =  colorTablero,  height = 700 , width = 700)
tablaPuntos = Frame(ventana , bg = colorTablaPuntos , height = 50 , width = 800)
Continuar = Button( ventana , text = 'Continuar!' , command = lambda: _continuar_())
reiniciarJuego = Button( ventana , text = 'Reiniciar Juego!' , command = lambda: _reiniciarJuego_())

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.Turno = True
        self.puntos = 0

    def suTurno(self):
        self.Turno

    def name(self):
        return self.nombre
    
    def puntos(self):
        return self.puntos    

Jugador1 = Usuario('Jugador 1')
Jugador2 = Usuario('Jugador 2')
jugador = None
tituloJuego = Label(ventana , bg = colorTitulo , font = 20)
finalizarRonda = 'no'

puntosJugador1 = Label(tablaPuntos , fg = colorPuntos , text = Jugador1.nombre , font = 100 , bg = colorTablaPuntos)
puntosJugador = Label(tablaPuntos ,  fg = colorPuntos , text = '      ' , font = 100 , bg = colorTablaPuntos).grid(row = 0 , column = 1)
puntosJugador2 = Label(tablaPuntos , fg = colorPuntos , text = Jugador2.nombre , font = 100 , bg = colorTablaPuntos)
nroPuntosJugador = Label(tablaPuntos ,  fg = colorPuntos , text='' , font = 100 , bg = colorTablaPuntos).grid(row = 1 , column = 1)
nroPuntosJugador1 = Label(tablaPuntos ,  fg = colorPuntos , text = Jugador1.puntos, font = 200 , bg = colorTablaPuntos)
nroPuntosJugador2 = Label(tablaPuntos ,  fg = colorPuntos , text = Jugador2.puntos, font = 200 , bg = colorTablaPuntos)

def cambiar_a_X():
    global simbol
    global jugador
    simbol = 'X'
    jugador = Jugador2

def cambiar_a_O():
    global simbol
    global jugador
    simbol = 'O'
    jugador = Jugador1

class casilla:

    def __init__(self,estado):
        self.boton = Button(Tablero, font = 800 , height = 6 , border = '0' , width = 16 , bg = colorCasilla , command = lambda: self.presionarBoton())
        self.estado = estado
        self.contenido = ''
        self.boton.config(text='')

    def presionarBoton(self):
        print(self.estado)
        global Jugador1
        global Jugador2
        global jugador
        global nroPuntosJugador1
        global nroPuntosJugador2
        global reiniciarJuego

        if self.estado == 'vacio' and simbol == 'X':
            cambiar_a_O()
            self.contenido = 'O'
            self.boton.config(text = simbol)
            
        elif self.contenido == '' and simbol == 'O': 
            cambiar_a_X()
            self.contenido = 'X'
            self.boton.config(text = simbol)
        
        evaluar_resultado()

        tituloJuego.config(text=f"Es el turno de {jugador.name()}")
        self.estado = 'presionado'

        if finalizarRonda == 'si' and simbol == 'X':
            jugador = Jugador1
            tituloJuego.config(text=f"¡ {jugador.name()} ha ganado esta ronda ¡", bg= '#7CD1B8' , fg = 'black')
            Jugador1.puntos += 1
            
            nroPuntosJugador1['text'] = Jugador1.puntos

            if Jugador1.puntos < 3:
                Continuar.pack()

            print('el jugador 1 tiene ahora ',Jugador1.puntos,' punto')

        elif finalizarRonda == 'si' and simbol == 'O':
           
            jugador = Jugador2
            tituloJuego.config(text=f"¡ {jugador.name()} ha ganado esta ronda ¡", bg= '#7CD1B8' , fg = 'black')
            Jugador2.puntos +=1
            Continuar.pack()
            nroPuntosJugador2['text'] = Jugador2.puntos

            if Jugador2.puntos == 3:
                print('gano el 2')

        if Jugador1.puntos == 3 or Jugador2.puntos == 3:
            reiniciarJuego.pack()


    def reiniciar(self):
        global finalizarRonda
        global jugador
        global simbol
        self.estado = 'vacio'
        self.boton.config(text='', bg = colorCasilla)
        self.contenido = ''
        jugador = Jugador1
        simbol = ''
        cambiar_a_O()
        finalizarRonda = 'No'

    def contenido(self):
        self.contenido

    def colocar(self,fila,columna):
        self.boton.grid(padx=5, pady=5, row=fila, column=columna)

casilla1 = casilla('vacio')
casilla2 = casilla('vacio')
casilla3 = casilla('vacio')
casilla4 = casilla('vacio')
casilla5 = casilla('vacio')
casilla6 = casilla('vacio')
casilla7 = casilla('vacio')
casilla8 = casilla('vacio')
casilla9 = casilla('vacio')

def evaluar_resultado():
    def revisarCasillas(simbolo,casilla_a,casilla_b,casilla_c):
        global finalizarRonda
        if casilla_a.contenido == simbolo and casilla_b.contenido == simbolo and casilla_c.contenido == simbolo:
            finalizarRonda = 'si'
            casilla_a.boton.config(bg = '#7CD1B8')
            casilla_b.boton.config(bg = '#7CD1B8')
            casilla_c.boton.config(bg = '#7CD1B8')

    revisarCasillas('X',casilla1,casilla2,casilla3)
    revisarCasillas('X',casilla4,casilla5,casilla6)
    revisarCasillas('X',casilla7,casilla8,casilla9)
    revisarCasillas('X',casilla2,casilla5,casilla8)
    revisarCasillas('X',casilla3,casilla6,casilla9)
    revisarCasillas('X',casilla1,casilla4,casilla7)
    revisarCasillas('X',casilla3,casilla5,casilla7)
    revisarCasillas('X',casilla1,casilla5,casilla9)

    revisarCasillas('O',casilla1,casilla2,casilla3)
    revisarCasillas('O',casilla4,casilla5,casilla6)
    revisarCasillas('O',casilla7,casilla8,casilla9)
    revisarCasillas('O',casilla2,casilla5,casilla8)
    revisarCasillas('O',casilla3,casilla6,casilla9)
    revisarCasillas('O',casilla1,casilla4,casilla7)
    revisarCasillas('O',casilla3,casilla5,casilla7)
    revisarCasillas('O',casilla1,casilla5,casilla9) 

def init():
    global simbol
    global jugador
    global Jugador1
    global Jugador2

    simbol = 'O'
    jugador = Jugador2
    Jugador1.nombre = ''
    Jugador2.nombre = ''

    ventana.config(bg = colorFondo)
    ventana.geometry('480x650+0+0')
    ventana.resizable( width = False, height = False )

    finalizarRonda == 'no'

    cabecera()
    
def cabecera():
    cab = Label( ventana , bg = colorCabecera , fg = colorTextoCabecera , height = 1 , width = 800  , text = ' TA TE TI ' )
    cab.pack()

def pantallaDeInicio(pantallaInicio):
    pantallaInicio.pack_propagate(0)
    pantallaInicio.pack()
 
    nombrarJugador1 = pantallaInicio = Frame( pantallaInicio , bd = 0  , bg = colorTitulo ,  height = 250 , width = 400 , relief="solid")
    Titulo = Label(nombrarJugador1 , text = ' ELIGE UN NOMBRE DE USUARIO' , font = 50 , bg = colorTitulo)
    Titulo.pack(pady = 20)

    textoNombrarUsuario = Label( nombrarJugador1 , bd = 0 , text = 'Jugador 1:'  , bg = colorTexto  , font = 20)
    entrada = Entry(nombrarJugador1 , bd = 1)
    boton = Button(nombrarJugador1 , text = 'aceptar' , bg = '#E05D5D' , bd = 0  , command = lambda: Boton1() )

    textoNombrarUsuario.pack(pady = 20)
    entrada.pack(pady=5)
    boton.pack(pady = 20 , ipady = 3 , ipadx = 5)

    def Boton1():
        boton.config(command = lambda: Boton2())
        textoNombrarUsuario.config(text = 'Jugador 2:')
        Jugador1.nombre = entrada.get()
        entrada.delete(0,"end")
        print(Jugador1.nombre)

    def Boton2():
        boton.config(command = lambda: Boton1())
        textoNombrarUsuario.config(text = 'Jugador 1:')
        Jugador2.nombre = entrada.get()
        entrada.delete(0,"end")
        print(Jugador2.nombre)
        pantallaDeJuego()

    nombrarJugador1.pack(pady = 100 , ipady = 9)
    nombrarJugador1.pack_propagate(0)

def pantallaDeJuego():
    global puntosJugador1
    global puntosJugador2

    tituloJuego.pack(pady = 20)
    pantallaInicio.pack_forget()
    Tablero.pack(pady = 30)
    tablaPuntos.pack(pady = 10)

    tituloJuego.config(text=f"Es el turno de {Jugador1.name()}")
    puntosJugador1.config(text = Jugador1.nombre)
    puntosJugador2.config(text = Jugador2.nombre)

    puntosJugador1.grid(row = 0 , column = 0)
    puntosJugador2.grid(row = 0 , column = 2)
    nroPuntosJugador1.grid(row = 1 , column = 0)
    nroPuntosJugador2.grid(row = 1 , column = 2)

    ponerTablero()
    
def ponerTablero():
    casilla1.colocar(0 , 0)
    casilla2.colocar(0 , 1)
    casilla3.colocar(0 , 2)
    casilla4.colocar(1 , 0)
    casilla5.colocar(1 , 1)
    casilla6.colocar(1 , 2)
    casilla7.colocar(2 , 0)
    casilla8.colocar(2 , 1)
    casilla9.colocar(2 , 2)

def _continuar_():
    tituloJuego.config(text=f"Es el turno de {jugador.name()}")

    casilla1.reiniciar()
    casilla2.reiniciar()
    casilla3.reiniciar()
    casilla4.reiniciar()
    casilla5.reiniciar()
    casilla6.reiniciar()
    casilla7.reiniciar()
    casilla8.reiniciar()
    casilla9.reiniciar()

    Continuar.pack_forget()

def _reiniciarJuego_():
    global Jugador1
    global Jugador2

    Jugador1.puntos = 0
    Jugador2.puntos = 0
    nroPuntosJugador1.config(text = Jugador1.puntos)
    nroPuntosJugador2.config(text = Jugador2.puntos)

    _continuar_()

    Tablero.pack_forget()
    reiniciarJuego.pack_forget()
    tablaPuntos.pack_forget()
    tituloJuego.pack_forget()

    pantallaInicio.pack()


init()
pantallaDeInicio(pantallaInicio)

ventana.mainloop()





