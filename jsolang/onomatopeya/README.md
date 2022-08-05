# JSoLang Onomatopeya

> ACLARACIÓN:
> + Actualmente no están todas las características implementadas.
> + Los samples no están editados.

`Onomatopeya` es un JSoLang con fines lúdicos.

Este JSoLang, para utilizar con Estuary, utiliza MiniTidal como lenguaje destino.

Su funcionalidad es limitada ya que emplea un grupo reducido de funciones y modificadores de los disponibles en minitidal.

Consiste en un catálogo de palabras onomatopéyicas que funcionan como símbolos para reproducir samples de audio análogos.

Admite apilado de patrones para que suenen en simultaneo. Los modificadores afectan a cada capa.

Entre los modificadores incluidos están el volumen, paneo, duración del ciclo, silenciar todo.

La posición de los modificadores es indistinta pudiendo estar entremezcladas con los propios samples.

Algunos modificadores, como el volumen y el paneo sonacumulativos.

El código del JSoLang Onomatopeya está [aquí](./onomatopeya.peg).


## Características

El guión bajo '_' comenta las palabras anulándolas si fueran funcionales.

### Silenciar

Capa

	h!
	H!

Todo

	0!

### Cálculo de volumen

	( (( (((
	) )) )))

### Cálculo de paneo

	< << <<<
	> >> >>>

### Cálculo de ritmo

	+ ++ +++
	- -- ---

Ritmo nulo

	-

Ritmo inverso

	-- --- ----

### Aceleración del ciclo

	/2 /3

### Ralentización del ciclo

	*2 *3

### Samples sonoros

La llamada a los audios no distingue entre mayúsculas y minúsculas.
Pero cualquier otra palabra o signo que no coincida con los instrumentos o los modificadores directamente será ignorada pudiendo estar presente por caracter estético del texto.

Al llamar a los audios puede agregarse de forma sufija y posfija. El entero sufijo actua como multiplicador del audio y el posfijo como index selector dentro del banco de audio solicitado.

	aahh arg auu baaa bbbddd beep biiubiuu biukbuik blublu braam bruubrr chuinn
	chukun clik cocoococoo crack crash crish cuak dindundin fiui fuifuifuii fuuhh
	gluglu gruar grugrr guauguau guiin hiiee iaaaa inkoon iuiuiuiu iuueu ja je jiik
	jojujujuju kash oh oink pashh piopi pop prrrprrr punch punn shaa shii shsh
	snrrrss srisisi tak tang tictac tilintilin tinb tink tinkunbin tinsh tirariru
	tiruriruin tling tomtom tonb tonk toomm trikint tritiing triuuii trraass
	trritrri trtrtrtr tuk tulinnn turip tuum uiiuuu uops uow yuayua zick zizizizi

### Sample silencio

Este sample solamente acepta el prefijo multiplicador.

	=

### Separador de capas

	.



## Requerimientos

Este banco de samples con onomatopeyas las asociadas. Debe importarse desde la consola de Estuary con el siguiente comando:

	!reslist "https://caalma.github.io/curso_ptav_estuary/jsolang/onomatopeya/audios/samples.json"



## Ejemplo de uso

Una capa:

	##onomatopeya
	)))(((()))
	2tink4 2zick 4=  tonb4 POP1 2Pop2 3Chukun =
	><<<>><<<<>>>>>>
	_H!

Varias capas:

	##onomatopeya
	2tink 3= 3tuk1  tuum <<<>>>> .
	*5 auu3 grugrr _h! .
	/3 tictac2 )) <<<<<<
	_0!

Varias capas y comentado:

	##onomatopeya

	estos son los sonidos de la primer capa
	2tink 3= 3tuk1  tuum

	acá se calcula el paneo de esta capa
	<<<>>>>

	los puntos separan las capas
	.

	esto aligera 5 veces el patrón
	*5

	otro patrón de sonidos
	auu3 grugrr

	esto es un silencio de capa comentado
	_h!

	acá se calcula el volumen de esta capa
	()((

	separamos otra capa
	.

	con esto ralentizamos 3 veces la capa
	/3

	tictac2 )) <<<<<<

	este es un silencio total comentado,
	para silenciar todo quitarle el guión bajo
	_0!


## Créditos
Los audios fueron obtenidos de https://pixabay.com/sound-effects/ y editados utilizando Audacity.
