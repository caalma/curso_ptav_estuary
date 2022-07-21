# CineCer0

Lenguaje desarrollado por el equipo de Estuary para experimenta con visuales manipulando videos, imágenes y texto.

## Documentación oficial

+ <https://github.com/dktr0/estuary/blob/dev/client/src/Estuary/Languages/CineCer0/REFERENCE.md>


##  Documentación (no oficial)

> En proceso de construcción. Actualizada : 2022-07-20

CineCer0 es un mini lenguaje de programación para componer visuales mediante videos, imágenes, formas y texto con tipografía.
Está inspirado en [CineVivo](https://github.com/essteban/CineVivo), otro desarrollo para componer visuales y videos.

Funciona desde el browser y está principalmente orientado hacia prácticas de livecoding.
Está siendo desarrollado por el equipo de Estuary.

Su sintaxis es similar a la de Haskell. Utiliza el doble guión medio '--' para indicar comentarios.
Y la composición de los comandos y parámetros es similar tanto a haskell como a tidalcycles.

Su sintaxis admite el encadenamiento de funciones mediante el signo pesos '$', y el anidamiento utilizando paréntesis '()'.

Las sentencias para varios recursos diferentes se separan mediante coma ',' o punto y coma ';'.

Los modificadores se agregan siempre antes del recurso (a la izquieda).


### Métodos de carga

Para cargar recursos de video o imagen se utiliza la función 'video' o 'image' respectivamente seguido de la url (online) del recurso a cargar. Ej:

	video "http://pagina.xyz/video.mp4"

	image "http://pagina.xyz/imagen.png"

Para mostrar textos se usa la función 'text' seguida la cadena de texto a mostrar. Ej:

	text "BlaBlaBla"


### Modificadores

#### Modificadores de POSICIÓN (video, imagen, texto)



Situa el centro del recurso en la posición 'x' relativa. Los valores esperados son cualquier real.

Como convención se sigue: izquierda (-1) a derecha 1

	setPosX [x] $


Situa el centro del recurso en la posición 'y' relativa. Los valores esperados son cualquier real.

Como convención se sigue:  arriba (-1) a abajo 1

	setPosY [y] $


Situa el centro del recurso en la posición 'x' e 'y' relativa.

Los valores y convenciones son iguales a 'setPosX' y 'setPosY'

	setCoord [x] [y] $


Modifica la profundidad variando el índice z del recurso.

Acepta enteros.

Los recursos se apilan en la dirección z según el orden de llegada.

Las posiciones z hacen referencia al entorno de Cinecer0. No modifican la profundidad respecto de otros visualizadores como Hydra o Punctual.

	z (-1)


#### Modificador de AUDIO (videos)


Los video se reproducen con el audio original. En caso de no querer utilizarlo deben mutearse explicitamente.

Los valores aceptados son reales desde 0 hasta 1.

	vol 0.5 $

#### Modificadores para Video e Image


Ancho del recurso. Los valores refieren a una escala respecto del ancho original del recurso.

Acepta cualquier real.

!! DUDA. Con valor 0, oculta el recurso

!! FALLA. Con valores negativos desplaza el recurso hacia la derecha pero mantiene la escala en 1.

!! FALLA. Con imágenes se altera el resultado solo dejando una línea horizontal.

	setWidth 1.2 $


Alias de 'setWidth'

	width 1.2 $


Alto del recurso. Los valores refieren a una escala respecto del alto original del recurso.

Acepta cualquier real.

!! DUDA. Con valor 0, oculta el

!! FALLA. Con valores negativos desplaza el recurso hacia la abajo pero mantiene la escala en 1.

!! FALLA. Con imágenes se altera el resultado solo dejando una línea vertical.

	setHeight 0.7 $


Alias de 'setHeight'

	height 0.7 $


Escala del recurso. Los valores refieren a una escala respecto del alto y el alto original del recurso.

Acepta cualquier real.

!! DUDA. Con valor 0, oculta el recurso

!! FALLA. con valores negativos desplaza el recurso hacia la abajo a la derecha pero mantiene la escala en 1.

	setSize 0.5 $


Alias de 'setSize'

	size 0.5 $


Afecta la opacidad del recurso.

Acepta cualquier real entre 0 y 1.

Como convención se sigue: 0 (transparente) y 1 (opaco)

!! FALLA. Valores negativos opacan el recurso.

	setOpacity 0.8 $


Alias de 'setOpacity'

	opacity 0.8 $


Rota el recurso en los n grados indicados.

Acepta cualquier real.

	setRotate 90 $


Desenfoca el recurso en la cantidad indicada.

Acepta reales positivos.

Como convención se sigue: (n<=0) nítido y (n>0) desenfocado según el valor de n.

	setBlur 10 $


Ajusta el brillo del recurso según el valor indicado.

Acepta reales.

Como convención se sigue: (n=0) negro (0<n<1) oscurecer, (n=1) original y (n>1) aclarar

!! FALLA. Nunca llega al blanco. El máximo apreciable es 25 aprox.

	setBrightness 0.9 $


Ajusta el contraste del recurso según el valor indicado.

Acepta reales.

Como convención se sigue: (n=0) gris medio (0<n<1) reduce el contraste, (n=1) original y (n>1) más contrastado.

!! PROPUESTA. Valores negativo no invierten la imagen.

!! FALLA. El máximo apreciable es 3 aprox.

	setContrast 1.2 $


Convierte a grises el recurso.

Acepta reales entre 0 y 1.

Como convención se sigue: (n=0) color original, (n=1) gris.

	setGrayscale 0.4 $


Ajusta la saturación del recurso.

Acepta reales.

Como convención se sigue: (n=0) desaturado/gris, (n=1) original, (n>1) sobresaturado.

El límite de la saturación está en 55 aprox.

	setSaturate 5 $


Máscara circular.

Acepta reales entre 0 y 1.

Como convención se sigue: (n<=0) sin máscara, (0<n<1) reducción del radio de la máscara , (n=1) circulo de radio 0 (oculta el recurso).

	circleMask 0.7 $


Esta variante, con el agregado del apostrofe "'", admite mover la posición del centro de la máscara.

Acepta tres valores reales. El primero corresponde a la reducción del radio y está limitado a valores entre 0 y 1.

Los dos siguientes corresponden a la posición 'x' e 'y' del centro de la máscara.

Las convenciones de la posición son similares a los de setCoord.

	circleMask' 0.5 1 0.2 $


Máscara cuadrada.

Acepta reales entre 0 y 1.

Como convención se sigue: (n<=0) sin máscara, (0<n<1) reducción del radio de la máscara , (n=1) cuadrado de radio 0 (oculta el recurso).

	sqrMask 0.3 $


Máscara rectangular.

Acepta 4 reales, correspondientes a: arriba, derecha, abajo, izquierda.

Lo valores variarán la reducción que crece hacia el centro.

	rectMask 0.1 0.2 0.3 0.4 $


#### Modificadores para texto

Cambia el tamaño del texto. El valor indicado actua como una escala, similar al 'em' de css.

Acepta reales positivos.

Como convención se sigue: (0<n<1) achican , (n=1) medida original, (n>1) agrandan.

!! FALLA. Los valores negativos fallan sin error mostrando el texto en tamaño natural.

	size 2.3 $


Selecciona la tipografía dentro de las disponibles localmente.

Acepta el nombre real o genérico de una tipografía instalada localmente.

	font "letter" $


Elige el color del texto.

Acepta varios formatos de color: hexadecimal, función rgb y rgba, nombre del color en inglés.

	colour "rgba(100, 0, 20, 0.3)" $
	colour "rgb(0, 200, 0)" $
	colour "blue" $


Elige el color de texto según valores RGB.

Acepta reales entre 0 y 1. Los tres valores asignados corresponden a rojo, verde y azul.

	rgb 0.5 1 0 $


Elige el color del texto según RGBA.

Acepta reales entre 0 y 1. Los cuatro valores requeridos corresponden a: rojo, verde, azul, opaciddad.

	rgba 1 0.5 0.8 0. $5


Elege el color del texto según HSL.

Acepta reales entre 0 y 1. Los tres valores requeridos corresponden a espectro, saturación y luminosidad.

	hsl 0.5 0.8 0.4 $


Elege el color del texto segun HSLA.

Acepta reales entre 0 y 1. Los cuatro valores requeridos corresponden a espectro, saturación, luminosidad y opacidad.

	hsla 0.3 1 0.6 0.5 $


Elege el color del texto segun HSV.

Acepta reales entre 0 y 1. Los tres valores requeridos corresponden a espectro, saturación, valor.

	hsv 0.3 1 0.6 $


Elege el color del texto segun HSV.

Acepta reales entre 0 y 1. Los cuatro valores requeridos corresponden a espectro, saturación, valor.

	hsva 0.3 1 0.6 0.5 $


Aplica el TACHADO del texto.

No requiere argumentos.

	strike $


Activa la NEGRITA en el estilo de texto.

No requiere argumentos.

	bold $


Activa la ITÁLICA en el estilo de texto.

	italic $

#### Modificadores de tiempo (videos)


Cambia el punto de inicio del video.

Aceptar reales. El n asinado representa desplazamiento.

!! DUDA. En que unidad es el desplazamiento.

	natural 10 $


Ajusta la duración (comprimiendo o estirando) del video a la cantidad de ciclos indicada.

Acepta numeros naturales. Los dos valores requeridos son: la cantidad de cíclos y el desplazamiento en fotogramas.

	every 3 0 $


Ajusta la longitud al número de compases más cercano en el tempo de Estuary.

Acepta números naturales. El valor requerido refiere al desplazamiento del punto de inicio del video.

!! FALLA o no está implementada.

	round 4 $


Ajusta la duración al número de compases más cercano múltiplo de 2,4,8,16,etc. para mantener el vídeo sincronizado con el tempo de Estuary.

Acepta números naturales. El valor requerido refiere al desplazamiento del punto de inicio del video.

!! FALLA o no está implementada.

	roundMetre 3 $



Reproduce el vídeo desde la posición inicial (0-1) hasta la posición final (0-1).

Estirando o comprimiendo la longitud para ajustarla al número de ciclos proporcionado como parámetro.

Acepta valores reales y enteros. Los cuatro valores que acepta son:

+ inicio (flotante entre 0 y 1),
+ fin (flotante entre 0 y 1),
+ cantidad de ciclos al que ajustarse (entero positivo),
+ desplazamiento del inicio (entero positivo)

!! FALLA o no está implementada.

	chop 0.2 0.7 2 0 $


Reproduce el vídeo desde la posición inicial (0-1) estirando o comprimiendo su

longitud para ajustarlo al número de ciclos proporcionado como parámetro.

Acepta valores reales y enteros. Los tres valores que acepta son:

+ inicio (flotante entre 0 y 1),
+ cantidad de ciclos al que ajustarse (entero positivo),
+ desplazamiento del inicio (entero positivo)

!! FALLA o no está implementada.

	chop' 0.5 3 1 $


Reproduce el vídeo desde la posición inicial hasta la posición final estirando o comprimiendo su longitud

para ajustarla al número de ciclos proporcionado como parámetro.

Esta función no tiene las posiciones inicial y final normalizadas de 0 a 1.

Acepta valores enteros positivos. Los cuatro valores que acepta son:

+ inicio,
+ fin,
+ cantidad de ciclos,
+ desplazamiento del punto de inicio

!! FALLA o no está implementada.

	chopSecs 3 5 2 0 $


La función snap ajusta la duración del vídeo al número de ciclos más cercano.

Acepta enteros positivos. El valor requerido se refiere al desplazamiento del punto de inicio.

	snap 15 $


La función snapMetre es similar a snap pero ajusta la duración del vídeo a 2,4,8,16,32, etc. ciclos.

Util para exploraciones relacionadas con la música.

Acepta enteros positivos. El valor requerido se refiere al desplazamiento del punto de inicio.

	snapMetre 10 $


Reproduce un segmento del vídeo (de principio a fin en porcentaje).

La velocidad del segmento de vídeo se ajusta a la duración indicada en ciclos.

Acepta valores reales y naturales. Los valores requeridos son:

+ inicio (en porcentaje de 0 a 1),
+ fin (en porcentaje de 0 a 1)
+ cantidad de ciclos al que ajustarse

	seg 0.25 0.75 2 $


Similar a 'seg' pero la duración del segmento está determinada por la velocidad natural.

Acepta valores reales entre 0 y 1. Los valores requeridos son:

+ inicio
+ fin

	freeSeg 0.25 0.75 $


Permite que el vídeo se reproduzca libremente sin ajustar el deplazamiento ni la velocidad.

No requiere valores.

	freeRun $


Permite controlar directamente la velocidad del vídeo.

!! FALLA o no implementado aun.

	rate 2 $


#### Controladores de valor

Genera valores reales entre el valor inical y el final, variándolos de acuerdo a la cantidad de ciclos indicada. Una vez que llegó al valor final se mantiene en ese valor.

Acepta valores reales. El primer valor corresponde a la duración de los ciclos, y los valores siguientes a la cantidad inicial y final esperadas.

Se aplica de manera que su resultado es el argumento de otros modificadores.

	size (ramp 3 0.1 3) $
	rgba 1 0 0.5 (ramp 2 0 1) $


Generador de valores para una señal sinusoidal.

Acepta valores reales. El valore requerido refiere a la cantidad de resultados respecto del ciclo.

	setPosY (sin 0.1) $


Generador periódico acotado.

Acepta reales y un generador. Los valores requeridos son:

+ cantidad más chica,
+ cantidad más grande,
+ señal generadora

```
	size (range 2 0.4 $ sin 0.2) $
```

Genera los valores desde 0 hasta 1.

Acepta reales positvos. El valor requerido refiere a la cantidad de variaciones dentro de un ciclo.

Los ciclos a mayor valor es más lento.

	size (fadeIn 5) $


Genera los valores desde 1 hasta 0.

Acepta reales positvos. El valor requerido refiere a la cantidad de variaciones dentro de un ciclo.

Los ciclos a mayor valor es más lento.

	setPosX (fadeOut 6) $


Actua como un multiplicador y alineador de punto de entrada del video.

Acepta valores real y entero. Los valores requeridos son:

+ multiplicador,
+ desplazamiento

```
	quant 3 0 $ setPosX (sin 0.3) $
```
