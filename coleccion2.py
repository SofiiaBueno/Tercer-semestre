import pickle
import os


ARCHIVO_TEXTO = "cartas_info.txt"
ARCHIVO_BINARIO = "cartas_stats.bin"

def crear_archivos_iniciales():
   
    try:
        
        if not os.path.exists(ARCHIVO_TEXTO):
            with open(ARCHIVO_TEXTO, 'w', encoding='utf-8') as f:
                f.write("nombre | tipo\n") 
            print(f"creado archivo de texto: {ARCHIVO_TEXTO}")

        
        if not os.path.exists(ARCHIVO_BINARIO):
            with open(ARCHIVO_BINARIO, 'wb') as f:
                pickle.dump({}, f)
            print(f" creado archivo binario: {ARCHIVO_BINARIO}")
            
    except Exception as e:
        print(f"error al iniciar archivos: {e}")

def agregar_carta():
    
    print("\n Agregar nueva carta")
    
    
    while True:
        nombre = input("nombre de la carta: ").strip()
        if not nombre:
            try:
                raise ValueError("el nombre de la carta no puede estar vacio.")
            except ValueError as e:
                print(e)
        else:
            break
            
    tipo = input("Tipo (monstruo, magica, trampa, etc): ").strip()

    while True:
        try:
            ataque = int(input("Valor de Ataque (con numero): ").strip())
            defensa = int(input("Valor de Defensa (con numero): ").strip())
            break 
        except ValueError:
            print("El ataque y la defensa deben ser valores enteros, intenta otra vez")
    
   
    try:
        with open(ARCHIVO_TEXTO, 'a', encoding='utf-8') as f:
            f.write(f"{nombre} | {tipo}\n")
        print(f"datos de texto de '{nombre}' guardados.")
    except IOError as e:
        print(f"error al escribir el archivo de texto: {e}")
        return 
    
    
    datos_binarios = {}
    try:
        with open(ARCHIVO_BINARIO, 'rb') as f:
            datos_binarios = pickle.load(f)
            
   
    except (FileNotFoundError, EOFError) as e:
        print(f"error al leer el binario ({e}). iniciara con la carta actual.")
        
        datos_binarios = {} 
        
    except Exception as e:
        print(f" ERROR al leer el binario: {e}")
        return 

    datos_binarios[nombre] = [ataque, defensa]
    
    try:
        with open(ARCHIVO_BINARIO, 'wb') as f:
            pickle.dump(datos_binarios, f)
        print(f"Estadísticas de '{nombre}' guardadas en binario.")
        
    except Exception as e:
        print(f" ERROR  al escribir en el binario: {e}")

    finally:
        print("Proceso de agregar completado.")

def mostrar_coleccion():
    
    print("\n Colección: ")
    
    try:
        
        with open(ARCHIVO_TEXTO, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if not contenido or contenido.count('\n') <= 1:
                print("la colección está vacía.")
            else:
                print(contenido)

    
    except FileNotFoundError:
        print(f"error: el archivo '{ARCHIVO_TEXTO}' no existe.")
    except Exception as e:
        print(f"error al leer el archivo de texto: {e}")


def mostrar_stats_binarios():
    
    print("\n Estadísticas de ataques y Defensa (binarios) ")
    
    try:
        
        with open(ARCHIVO_BINARIO, 'rb') as f:
            datos = pickle.load(f)

        if not datos:
            print("no hay estadísticas guardadas.")
            return

        
        print("{:<25} | {:<5} | {:<5}".format("Nombre", "Ataque", "Defensa"))
        
        
        for nombre, stats in datos.items():
            
            print("{:<25} | {:<5} | {:<5}".format(nombre, stats[0], stats[1]))
            
    
    except FileNotFoundError:
        print(f" el archivo '{ARCHIVO_BINARIO}' no existe.")
    except EOFError:
        print("el archivo binario existe, pero esta vacio.")
    except Exception as e:
        print(f"error al leer el archivo binario: {e}")



def menu_principal():
   
    crear_archivos_iniciales()
    
    while True:
        
        print(" COLECCION DIGITAL YU-GI-OH! ")
        
        print("1. agregar carta (texto y binario)")
        print("2. mostrar colección (texto")
        print("3. mostrar estadísticas (binario)")
        print("4. salir")
        
        opcion = input("elige una opción: ").strip()

        if opcion == '1':
            agregar_carta()
        elif opcion == '2':
            mostrar_coleccion()
        elif opcion == '3':
            mostrar_stats_binarios()
        elif opcion == '4':
            print("se termino la hora del D-D-D-D DUELO. bai")
            break
        else:
            print("error. elige un número del 1 al 4.")


if __name__ == "__main__":
    menu_principal()