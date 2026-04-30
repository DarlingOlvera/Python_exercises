Eres un programador senior que debe programar un pequeño programa que acceda a una un diretorio llamado Recetas que se encuentra en el escritorio de un ordenador que puede ser Mac o Windows.
El programa debe continuar hasta que el usuario decida salir.
Se comienza con una Bienvenida al usuario donde se le dan las siguientes opciones:

1. leer recera
   2.crear receta
   3.crear categoría
   4.eliminar receta
   5.eliminar categoria
   6.finalizar programa

si selecciona la opcion 1:
Se debe preguntar en que categoria quiere entrar y mostrar las carpetas dentro de Recetas para que una vez se de el nombre se ingrese a dicha carpeta y se muestren los archivos .txt (recetas), de igual forma se pide el nombre del archivo y se muestra el contenido del mismo en consola

si se selecciona la opción 2:
Se debe pedir la categoria al igual que en la opcion 1 y una vez dentro de la misma se pide el nombre del archivo a crear y despues el contenido que tendrá (verifica que el nombre dado para el archivo no exista antes de crearlo, de ser asi pide un nombre nuevo)

si se selecciona la opcion 3:
solo pide el nombre de la nueva categoria, verifica que no exista dentro de Recetas y crea la carpeta con el nombre de la nueva categoria

si se selecciona la opcion 4:
Se vuelve a pedir nombre de categoria y posteriormente del archivo (como se hace en la opcion 1) y se elimina el archivo

si se selecciona la opcion 5:
Se vuelve a pedir nombre de categoria y se elimina la carpeta, en caso de tener archivos dentro avisar al usuario y volver a preguntar si está seguro que quiere eliminar la categoría

si se selecciona la opcion 6:
se sale del programa

IMPORTANTE:
-limpiar la consola cada vez que se termine el proceso de alguna de las opciones y volver a mostrar el menu inicial

-usar las librerias de Pathlib y System para manejar rutas y limpieza de consola de modo que el programa sea universal para windows o mac

-crear todas las funciones que sean necesarias para hacer el codigo facil de leer y mantener

-poner comentarios que expliquen metodos o cosas importantes como importaciones y funcionalidad de modo que un junior entienda bien que hace el programa y como
