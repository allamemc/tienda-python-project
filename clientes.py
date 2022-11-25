import modulos_textos

def inicio(): #creamos una funcion inicial para determinar a que clase pertenece la persona que usa la aplicacion
    modulos_textos.inicioopc()
    j=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
    print('------------------------------------')

    match j:
        case '1':
            persona=Cliente()
            persona.pantalla_principal()
        case '2':
            persona=Trabajador()
            print('AUN NO HAY FUNCIONES PARA USTED')
            print('------------------------------------')
        case '3':
            persona=Admin()
            print('AUN NO HAY FUNCIONES PARA USTED')
            print('------------------------------------')
        case _:
            print('INTRODUZCA UN NUMERO VALIDO')
            print('------------------------------------')
            inicio()

#Los productos los añadirmos a un dict para poder asignarles un valor todo ello dentro de una lista
productos = {'3060':399,'3070':499,'3080':699,'i5':200,'i7':250,'monitor':150,'raton':50,'teclado':70,'cascos':20,'altavoces':30,'portatil':999,'rx580':450,'rx6670':890}
lista_deseosa={}
carrito_compra={}


#La interface empieza con persona donde tendremos unas funciones base que cambiaran segun nuestras clases hijas derivadas mediante soobreescritura
class Persona():
        def __init__(self):
            pass

        def muestradatos(self):
            pass
            
        def pantalla_principal(self):
            pass
        
        def carrito_lista(self):
            modulos_textos.carritoylista()
            y=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
            print('------------------------------------')
            #el programa da uso completo al switch case para sustituir los ifs
            match y:
                case '1':
                    def carrito():
                        modulos_textos.carritodef()
                        z=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                        print('------------------------------------')
                        match z:
                            case '1':
                                def agregar_carrito():
                                    modulos_textos.carritoopc()
                                    h=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                                    print('------------------------------------')
                                    match h:
                                        case '1':
                                            print('------LISTA PRODUCTOS------')
                                            for key, value in productos.items():
                                                print(key, ' PRECIO: ', value,'€')
                                            print('------------------------------------')
                                            agregar_carrito()
                                        case '2':
                                            def productoc():
                                                try:
                                                    print('------------------------------------')
                                                    k=input('DIME EL PRODUCTO: ')
                                                    carrito_compra[k]=productos[k] #append del dict
                                                    print('------------------------------------')
                                                    print('1. AÑADIR OTRO PRODUCTO')
                                                    print('2. VOLVER')
                                                    o = input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                                                    print('------------------------------------')
                                                    match o:
                                                        case '1':
                                                            productoc()
                                                        case '2':
                                                            agregar_carrito()
                                                except:
                                                    modulos_textos.except_carrilis()
                                                    u = input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                                                    print('------------------------------------')
                                                    match u:
                                                        case '1':
                                                            productoc()
                                                        case '2':
                                                            agregar_carrito()
                                                        case _:
                                                            productoc()
                                            productoc()
                                            agregar_carrito()
                                        case '3':
                                            carrito()
                                        case _:
                                            agregar_carrito()
                                agregar_carrito()
                            case '2':
                                print('------CARRITO------')
                                for key, value in carrito_compra.items(): #recorremos el dict sus key y values
                                    print(key, ' PRECIO: ', value,'€')
                                print('------------------------------------')
                                def eliminarproducto():
                                    print('¿DESEA ELIMINAR ALGUN PRODUCTO?')
                                    print('1. ELIMINAR PRODUCTO')
                                    print('2. VOLVER')
                                    eliminar=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')

                                    match eliminar:
                                        case '1':
                                            try:
                                                eliminarp=input('DIME EL PRODUCTO: ')
                                                del carrito_compra[eliminarp]
                                                print('------TU NUEVO CARRITO------')
                                                for key, value in carrito_compra.items(): #recorremos el dict sus key y values
                                                    print(key, ' PRECIO: ', value,'€')
                                                ('----------------------------------')
                                                eliminarproducto()
                                            except:
                                                print('-------------------------------')
                                                print('EL PRODUCTO NO ESTA EN LA LISTA')
                                                print('-------------------------------')
                                                eliminarproducto()
                                        case '2':
                                            pass
                                        case _:
                                            eliminarproducto()
                                eliminarproducto()
                                carrito()
                            case '3':
                                self.carrito_lista()
                    carrito()
                case '2':
                    def lista_deseos():
                        modulos_textos.listadese()
                        i=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                        print('------------------------------------')
                        match i:
                            case '1':
                                def agregar_lista():
                                    modulos_textos.listaopc()
                                    m=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                                    print('------------------------------------')
                                    match m:
                                        case '1':
                                            print('------LISTA PRODUCTOS------')
                                            for key, value in productos.items():
                                                print(key, ' PRECIO: ', value,'€')
                                            print('------------------------------------')
                                            agregar_lista()
                                        case '2':
                                            def productol():
                                                try:
                                                    k=input('Dime el producto: ')
                                                    lista_deseosa[k]=productos[k]
                                                    print('------------------------------------')
                                                    print('1. AÑADIR OTRO PRODUCTO')
                                                    print('2. VOLVER')
                                                    v = input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                                                    print('------------------------------------')
                                                    match v:
                                                        case '1':
                                                            productol()
                                                        case '2':
                                                            agregar_lista()
                                                except:
                                                    modulos_textos.except_carrilis()
                                                    rt = input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                                                    print('------------------------------------')
                                                    match rt:
                                                        case '1':
                                                            productol()
                                                        case '2':
                                                            agregar_lista()
                                            productol()
                                            agregar_lista()
                                        case '3':
                                            lista_deseos()
                                        case _:
                                            agregar_lista()
                                agregar_lista()
                            case '2':
                                print('------LISTA DESEOS------')
                                for key, value in lista_deseosa.items():#recorremos el dict sus key y values
                                    print(key, ' PRECIO: ', value,'€')
                                print('------------------------------------')
                                def eliminarproductoli():
                                    print('¿DESEA ELIMINAR ALGUN PRODUCTO?')
                                    print('1. ELIMINAR PRODUCTO')
                                    print('2. VOLVER')
                                    eliminarl=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')

                                    match eliminarl:
                                        case '1':
                                            try:
                                                eliminarl=input('DIME EL PRODUCTO: ')
                                                del lista_deseosa[eliminarl]
                                                print('------TU NUEVA LISTA------')
                                                for key, value in lista_deseosa.items(): 
                                                    print(key, ' PRECIO: ', value,'€')
                                                print('---------------------------')
                                                eliminarproductoli()
                                            except:
                                                print('-------------------------------')
                                                print('EL PRODUCTO NO ESTA EN LA LISTA')
                                                print('-------------------------------')
                                                eliminarproductoli()
                                        case '2':
                                            pass
                                        case _:
                                            eliminarproductoli()
                                eliminarproductoli()
                                lista_deseos()
                            case '3':
                                self.carrito_lista()
                    lista_deseos()
                case '3':
                    self.pantalla_principal()
                case _:
                    self.carrito_lista()


class Cliente(Persona): 
    def __init__(self): 
        super().__init__()
        print('------REGISTRO AUTOMATICO------')
        print('INICIO AUTOMATICO PROCESO REGISTRO....')
        self.nombre=input('INTRODUZCA SU NOMBRE: ')
        self.direccion=input('INTRODUZCA DIRECCION: ')
        self.pais=input('INTRODUZCA PAIS: ')
        def emailpe():
            self.email=input('INTRODUZCA UN EMAIL VÁLIDO EL EMAIL: ')
            comprobacion="@" in self.email
            if comprobacion == True:
                pass
            else:
                emailpe()
        emailpe()
        def tlecom():
            try:
                self.tlf=int(input('INTRODUZCA UN TELÉFONO VÁLIDO: '))
            except:
                tlecom()
        tlecom()

        print('------------------------------------')
        
    def muestradatos(self): #sobreescritura

        #esto es una sobreescritura la debemos hacer por que en caso de que tengamos admin o trabajador los datos mostrados seran distintos

        print(f'BUENAS {self.nombre.upper()} SU DIRECCION ES: {self.direccion.upper()} Y VIVE EN {self.pais.upper()} CON NUMERO DE TLF {self.tlf}')
        print('------------------------------------')
        self.pantalla_principal()
    
    def pantalla_principal(self): #la pantalla principal es distinta depediendo de la persona
        modulos_textos.texto_principal()
        final=input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
        print('------------------------------------')

        if self.pais.lower() == 'españa': #iva españa
            iva = 1.21
        elif self.pais.lower() == 'francia': #iva francia
            iva = 1.11
        else: #iva fijo resto de paises
            iva = 1.41

        match final:
            case '1':
                self.muestradatos()
            case '2':
                self.carrito_lista()
            case '3':
                
                            
                
                def pagos():
                    modulos_textos.realizar_pago()
                    pago = input('INTRODUZCA EL NUMERO DE LA ACCION A REALIZAR: ')
                    print('------------------------------------')
                    
                    match pago: 
                        case '1':
                            print('------FACTURA------')
                            for key, value in carrito_compra.items(): 
                                print(key, ' PRECIO: ', value,'€')
                                
                            #en caso de que el pago sea de francia o españa tiene un iva determinado los demas paises un iva base
                            pago_total=round(sum(carrito_compra.values())*iva,2)
                            print(f'EL TOTAL DE SU CESTA ES:{pago_total}€')
                            print(f'SE HA ENVIADO LA FACTURA A SU TLF {self.tlf} Y A SU EMAIL {self.email}')
                            print('------------------------------------')
                            self.pantalla_principal()
                        case '2':
                            self.pantalla_principal()
                        case _:
                            pagos()
                pagos()
            case '4':
                if round(sum(carrito_compra.values())*iva,2) == 0:
                    print(f'AUN NO SE HA COMPLETADO NINGUNA COMPRA')
                    print('------------------------------------')
                else: 
                    print(f'SE HA ENVIADO EL SEGUIMIENTO DE SU PEDIDO A SU EMAIL {self.email}')
                    print('------------------------------------')
                self.pantalla_principal()
            case '5':
                SystemExit #finalizar
            case _:
                self.pantalla_principal()

#Las dos siguientes clases no tienen metodos ni funciones son dos clases Hijas para en caso de tener un admin o trabajadores poder hacer el codigo de manera que sea distinto para estas dos.

class Admin(Persona): #clase sin uso pero en caso de que sea necesario se creara su codigo para la misma
    def __init__(self):
        super().__init__()
        print('------GESTION DE PEDIDOS------')
        print('INICIO AUTOMATICO PROCESO REGISTRO....')
        self.usuario=input('INTRODUZCA USUARIO: ')
        self.contraseña=input('INTRODUZCA CONTRASEÑA: ')

class Trabajador(Persona):
    def __init__(self):
        super().__init__()
        print('------GESTION DE PEDIDOS------')
        print('INICIO AUTOMATICO PROCESO REGISTRO....')
        self.nombre=input('INTRODUZCA SU NOMBRE: ')
        self.nif=input('INTRODUZCA NIF: ')
        self.idtrabajador=input('INTRODUZCA ID DE TRABAJADOR: ')

inicio()
