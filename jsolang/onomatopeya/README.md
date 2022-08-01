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
	/2 *2
	/3 *3

	_samples_sonoros
	aahh arg auu baaa bbbddd beep biiubiuu biukbuik blublu braam bruubrr chuinn chukun clapclap clik cocoococoo crack crash crish cuak dindundin fiui fuifuifuii gluglu gruar grugrr guauguau guiin iaaaa inkoon iuiuiuiu iuueu ja je jiik jojujujuju juuhh kash krikri mmm oh oink pashh piopi pop prrrprrr punch shiiee shiushi shiuushaaa shshsh srisisi tak tictac tilintilin tinb tink tinkunbin tinsh tirariru tiruriruin tling tomtom tonk toomm trikint tritiing triuuii trraass trritrri trtrtrtr tuk tulinnn turip tutuntutun tuum uauuau uiiuuu uops uow zick zizizizi

	_sample_silencio
	=

	_separador_de_capas
	;

## Requerimientos

Esta banco de samples con onomatopeyas asociadas. Debe importarse desde la consola de Estuary con el siguiente comando:

	!reslist "https://caalma.github.io/curso_ptav_estuary/jsolang/onomatopeya/samples/samples.json"


## Créditos
Los audios fueron obtenidos de https://pixabay.com/sound-effects/ y editados utilizando Audacity.