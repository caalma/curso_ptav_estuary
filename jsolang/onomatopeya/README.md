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

La llamada a los audios no distingue entre mayúsculas y minúsculas.
Pero cualquier otra palabra o signo que no coincida con los instrumentos o los modificadores directamente será ignorada pudiendo estar presente por caracter estético del texto.

Al llamar a los audios puede agregarse de forma sufija y posfija. El entero sufijo actua como multiplicador del audio y el posfijo como index selector dentro del banco de audio solicitado.

El código del JSoLang Onomatopeya está [aquí](./onomatopeya.peg).


## Características

	##onomatopeya

	_silenciar
	shh!

	_volumen
	( (( (((
	) )) )))

	_paneo
	< << <<<
	> >> >>>

	_duracion_del_ciclo
	/2 /3
	*2 *3

	_ritmo_aumentado
	+ ++ +++
	- -- ---

	_ritmo_negativo

	_samples_sonoros
	aahh arg auu baaa bbbddd beep biiubiuu biukbuik blublu braam bruubrr chuinn
	chukun clik cocoococoo crack crash crish cuak dindundin fiui fuifuifuii fuuhh
	gluglu gruar grugrr guauguau guiin hiiee iaaaa inkoon iuiuiuiu iuueu ja je jiik
	jojujujuju kash oh oink pashh piopi pop prrrprrr punch punn shaa shii shsh
	snrrrss srisisi tak tang tictac tilintilin tinb tink tinkunbin tinsh tirariru
	tiruriruin tling tomtom tonb tonk toomm trikint tritiing triuuii trraass
	trritrri trtrtrtr tuk tulinnn turip tuum uiiuuu uops uow yuayua zick zizizizi


	_sample_silencio
	=

	_separador_de_capas FALTA
	;

## Requerimientos

Esta banco de samples con onomatopeyas asociadas. Debe importarse desde la consola de Estuary con el siguiente comando:

	!reslist "https://caalma.github.io/curso_ptav_estuary/jsolang/onomatopeya/audios/samples.json"


## Ejemplo de uso

	##onomatopeya
	(((())))))
	2tink2 3shii4 == zick POP1 2pop2 3=
	><<<>><<<<>>>>>>
	H!

## Créditos
Los audios fueron obtenidos de https://pixabay.com/sound-effects/ y editados utilizando Audacity.
