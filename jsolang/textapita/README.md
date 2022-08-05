# JSoLang Textapita


> ACLARACIÓN: Actualmente no están todas las características implementadas.


**Textapita** escribe textos utilizando loops de videos.

Este JSoLang, para utilizar con Estuary, utiliza CineCer0 como lenguaje destino.

Los textos a escribir deben colocarse entre corchetes `[ ]`.
Los signos permitidos para la escritura son las letras de la a `a` la `z`, más la `ñ` y el ` ` (espacio).
Todas las letras admiten mayúscula y minúscula, estas variantes posibilitan el cambio de tamaño de la letra.
Los ` ` (espacios) son representados como signos random (en cada evaluación del código) sin animación.

El signo punto `.` , fuera de los corchetes,  sirve para generar más de una línea de texto.

Además admite **modificadores** que varian la animación o composición de los textos.
Pueden ubicarse indistintamente antes o después del texto a escribir pero siempre fuera de los corchetes `[ ]`.
Los modificacores son aplicados a cada línea individualmente.

Modificadores de animación:

+ ondula-y
+ ondula-x
+ giratorias

Modificadores de composición:

+ izquierda
+ centro
+ derecha


Cualquier otro signo escrito será ignorado por el parser.

El código del JSoLang **Textapita** está [aquí](./textapita.peg).


## Ejemplos:

Una línea de texto:

	##textapita
	[Ja je Ji Ño ñu]

Dos lineas de texto:

	##textapita
	[Primera] .
	[segundA]

Limpia la salida:

	##textapita
	[]

Con modificadores:

	##textapita
	centro [texTapita] ondula-y


## FALTA

+ Implementar separación de lineas.
+ Implementar modificadores.
