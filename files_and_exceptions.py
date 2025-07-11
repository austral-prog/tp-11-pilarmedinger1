def read_file_to_dict(filename):
    ventas_por_producto = {} #diccionario vacio pra guardar cada producto con su lista de ventas
    
    try:
        with open(filename, 'r') as file: #abre el archivo en modo lectura, y le pone el nombre file
            linea = file.read() #lee linea del archivo, hay una sola linea asique alcanza
            lista_entrada = linea.split(";") #corta la linea cada vez que hay un ";"
            #entradas es una lista ahora con items asi ['producto1': 100]

            for entrada in lista_entrada: #recorre cada entra de tipo product0:valor
                if entrada == '': #si la entrada esta vacia la saltea
                    continue
                #separamos el prodcuto del valor
                producto, valor = entrada.split(":") #separa en dos variables
                #producto1:100, se convierte en producto=producto1 y valor=100 (ambos son texto)
                valor = float(valor) #cpnvierte el valor a nro (100.0)

                #si el producto no esta en el diccionario, lo agrego con una lista vacia para depsues rellenarla con los numeros
                if producto not in ventas_por_producto:
                    ventas_por_producto[producto] = []

                #agregamos el valor a la lista correspondiente
                ventas_por_producto[producto].append(valor)
        
        #diccionario final con todos los productos y sus listas de ventas
        return ventas_por_producto
    #si no se encuentra el archivo
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no existe.")



def process_dict(data):
    for producto, ventas in data.items():
        total = sum(ventas)
        promedio = total / len(ventas)
        print (f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}") #:.2f es para q sean 2 cofras decimales



