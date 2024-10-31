# curso-programaci-n10

__Propietario__: Keysy Alfaro 

Aqui estara la correccion de el codigo dado en la clase junto una breve explicacion del por que de  sus errores

Error 1 (sintaxis): en las lineas 6, 8 y 10, hacia falta agregar ":" al final de cada uno, debido a que en python las declaraciones if, elif y else deben de finalizar con un ":"

Error 2: En la linea 16, lo que pasa con el input es que te va a devolver un str o una secuencia de caracteres, es decir, no los convertira en enteros o flotantes automaticamente ya que no es esa su funcion, por lo cual la funcion calcular_promedio intentara sumar estos caracteres, dando asi un error. La correccion a esto sera agregar "float" antes del "input" 
