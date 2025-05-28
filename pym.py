# Definimos una clase que nos sirva para guardar y utilizar nuestras
# funcios
class tools:
    def generar_df_ventas(fecha, n_ventas):
        """
        Genera un DataFrame de ventas simuladas para una fecha específica.

        Parámetros:
        -----------
        fecha : str
            Fecha de las ventas en formato 'YYYY-MM-DD'.
        n_ventas : int
            Número de registros (ventas) a generar.

        Retorna:
        --------
        df_ventas : pandas.DataFrame
            DataFrame con las columnas: 'Fecha', 'Producto', 'Clave', 'Cantidad', 'Precio', 'Total', 'Sucursal'.
            Cada fila representa una venta simulada con datos aleatorios.

        Ejemplo de uso:
        ---------------
        df = generar_df_ventas('2025-01-01', 1000)
        """

        import pandas as pd
        import random as r
        
        # ========================== Parte I ==========================
        # Definicion de las listas
        abcdario = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
            ]

        papelerias = [
            'Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta',
            'CU', 'Zócalo', 'Narvarte', 'Santa Fé', 'Polanco',
            'Centro'
            ]

        lineas = [
            'Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
            'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
            'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
            'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas'
            ]

        # =========================== Parte II ==========================
        # Definimos listas vacias que posteriormente iremos llenando
        # con los datos de cada venta mediante la funcion append()
        # y el bucle for

        fechas = []
        productos = []
        claves = []
        cantidades = []
        precios = []
        totales = []
        sucursales = []

        # ========================= Parte III ==========================
        # Repetimos un bucle for 1000 veces, donde en cada iteracion
        # o cada vuelta, agregamos un nuevo elemento a cada lista
        for i in range(n_ventas):
            # Zona de definicion de variables
            producto = r.choice(lineas)
            clave = r.choice(abcdario) + r.choice(abcdario) + r.choice(abcdario) + '-' + str(r.randint(1, 9)) + str(r.randint(1, 9)) + str(r.randint(1, 9)) 
            cantidad = r.randint(1, 50)
            precio = round(r.randint(1, 10000) * r.random(), 2)
            total = round(precio * cantidad, 2)
            sucursal = r.choice(papelerias)

            # Agregamos los datos a las listas
            fechas.append(fecha)
            productos.append(producto)
            claves.append(clave)
            cantidades.append(cantidad)
            precios.append(precio)
            totales.append(total)
            sucursales.append(sucursal)

        # ========================= Parte IV ==========================
        # Definimos un diccionario donde las claves seran los nombres
        # de las columnas y los valores seran las listas que llenamos
        dict_pre_ventas = {
            "Fecha": fechas,
            "Producto": productos,
            "Clave": claves,
            "Cantidad": cantidades,
            "Precio": precios,
            "Total": totales,
            "Sucursal": sucursales
        }

        # ========================== Parte V ==========================
        # Creamos el dataframe con la funcion de pandas pd.DataFrame()
        df_ventas = pd.DataFrame(dict_pre_ventas)
    
        # Retornamos el dataframe
        return df_ventas

    def inicializar_bbdd(df):
        """
        Inicializa la base de datos y crea la tabla 'ventas' con los datos de un DataFrame.

        Parámetros:
        -----------
        df : pandas.DataFrame
            DataFrame con la información de ventas a subir. Debe contener las columnas:
            'Fecha', 'Producto', 'Clave', 'Cantidad', 'Precio', 'Total', 'Sucursal'.

        Retorna:
        --------
        None

        Ejemplo de uso:
        ---------------
        inicializar_bbdd(df)
        """
        import sqlite3 as sql
        import pandas as pd

        # Creamos la conexion o la base de datos
        conn = sql.connect('ventas.db')
        # Subimos el dataframe a la base de datos
        df.to_sql('ventas', conn, if_exists='replace', index=False)
        # Guardamoscambios y cerramos la conexion
        conn.commit()
        conn.close()

        print("Base de datos inicializada y datos subidos correctamente.")

    # Esencialmente es el mismo codigo de la funcion anterior
    # con la unica diferencia del valor asignado al parametro if_exists
    def subir_df(df):
        """
        Agrega los datos de un DataFrame a la tabla 'ventas' existente en la base de datos.

        Parámetros:
        -----------
        df : pandas.DataFrame
            DataFrame con la información de ventas a agregar. Debe contener las columnas:
            'Fecha', 'Producto', 'Clave', 'Cantidad', 'Precio', 'Total', 'Sucursal'.

        Retorna:
        --------
        None

        Ejemplo de uso:
        ---------------
        subir_df(df)
        """
        import sqlite3 as sql
        import pandas as pd

        # Creamos la conexion o la base de datos
        conn = sql.connect('ventas_pruebas.db')
        # Subimos el dataframe a la base de datos
        df.to_sql('ventas_pruebas', conn, if_exists='append', index=False)
        # Guardamoscambios y cerramos la conexion
        conn.commit()
        conn.close()

        print("Dataframe subido correctamente a la base de datos.")
            

    # Como un extra podemos definir una función para hacer consultas a nuestra tabla
    def consultar_bbdd(query):
        """
        Realiza una consulta SQL sobre la base de datos 'ventas.db' y devuelve el resultado como DataFrame.

        Parámetros:
        -----------
        query : str
            Consulta SQL a ejecutar sobre la base de datos.

        Retorna:
        --------
        consulta : pandas.DataFrame
            DataFrame con el resultado de la consulta.

        Ejemplo de uso:
        ---------------
        resultado = consultar_bbdd("SELECT * FROM ventas")
        """
        import sqlite3 as sql
        import pandas as pd

        # Creamos la conexion o la base de datos
        conn = sql.connect('ventas_pruebas.db')
        # Hacemos una consulta a la tabla ventas
        consulta = pd.read_sql_query(query, conn)
        # Cerramos la conexion
        conn.close()

        return consulta