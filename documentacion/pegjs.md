# PEGjs

> ACLARACIÓN:
> + Este contenido está en construcción. Cualquier sugerencia será bienvenida.


Librería javascript desarrollada para parsear textos.
Originalmente creado por David Majda.
Actualmente mantenida bajo el nombre de _peggyjs_ por Joe Hildebrand.

## Referencias

+ https://pegjs.org
+ https://peggyjs.org

## Documentación

### Estructura
La estructura del parser consta de dos bloques:

1. variables y funciones javascript
2. reglas del lenguaje

El orde de los bloques es estrictamente ese. Pero el primer bloque es opcional pudiendo desarrollarse el parser sin utilizar funciones y variables de javascript extras.

### Bloque javascript

El bloque javascript contendrá todas las funciones y variables que necesitemos para el parser. Todos esos elementos serán accesibles desde el bloque de retorno o devolución de valor ubicado, opcionalmente, en cada una de las reglas.

### Reglas

Las reglas consisten en variables, con una sintaxis similar a la utilizada en javascript. Estas variables funcionarán como símbolos para segmentar los patrones que queramos reconocer en el texto que interpretemos con el parser.

Cada regla consta de un nombre, un signo igual, uno o varios patrones y un bloque de salida o devolución de resultado. Este último bloque es opcional y su contenido es código javascript. Un ejemplo de esa estructura seria:

	color = 'rojo' { return 'https://es.wikipedia.org/wiki/Rojo' }



[ ... ]




## Ejemplos comentados

Estos ejemplos pueden probarse directamente desde https://pegjs.org/online o https://peggyjs.org/online .


### Estructura básica


#### Reglas básicas

La regla inicializadora es la primera en aparecer.
Normalmente debería contener una lista de posibles candidatos inicializadores de frase. Para ello deben separarse las reglas con la '/' que simboliza al 'or' lógico.

	inicializadora = simbolo_1 / simbolo_espacio / simbolo_a1 / simbolo_a2
	simbolo_espacio = '-'
	simbolo_1 = "aca" { return "en este lugar" }
	simbolo_a1 = "estE" { return "esté" }
	simbolo_a2 = "Este" { return "este" }

#### Selectores

	letras_mayusculas = [A-Z]*

	letras_minusculas = [a-z]*

	letras_desde_b_hasta_k = [b-k]*

	letras_mayusculas_y_minusculas = [A-Za-z]*

	letras_mayusculas_y_minusculas_otra_forma = [A-z]*

	digitos = [0-9]*

	digitos_desde_4_a_8 = [4-8]*

	letras_expandidas_y_numeros = ([A-z0-9] / letras_especiales)*
	letras_especiales = 'ñ'i / 'á'i / 'é'i / 'í'i / 'ó'i / 'ú'i

#### Reconocimiento básico

	{
		// acá se agregan funciones y variables de entorno
		let letra = {
    		'a': 'letra A',
			'b': 'letra B'
		}
		//alert('hola');
	}

	// aquí se colocan las reglas del lenguaje

	todos = (texto_estricto / texto_may_min
          / enteros / separadores / constantes
          / ignorar
          )*

	texto_estricto = 'Texto'
	texto_may_min = 'teXtO'i

	enteros = n:( digitos / negativos ) { return parseInt(n) }
	digitos = n:([0-9]+) { return n.join('') }
	negativos = s:('-'?) n:digitos { return s + n }

	constantes = l:('a' / 'b') { return letra[l] }

	separadores = ' ' / ','
	ignorar = . { return '' }

#### Flotantes con coma o punto

	// admite número no completo
	// nota: aunque corta el numero en la cifra 20 aprox
	// al convertirlo a flotante por característica interna de javascript

	flotante = pe:entero* se:sepf pd:entero*
               { return parseFloat(pe.join('') + '.' + pd.join('')) }
	entero = [0-9]
	sepf = '.' / ','

#### Separar palabras
	frase = f:(palabra espacio?)* { return f.map(function(v){ return v[0] }) }
	palabra = p:(letra+) { return p.join('') }
	letra = [A-z] / letra_especial
	letra_especial = 'ñ'i / 'á'i / 'é'i / 'í'i / 'ó'i / 'ú'i
	espacio = (' ' / '\n' / ',')+
	punto = ('.')

#### Separar frases

	parrafo = p:(frase / punto)+ { return p.filter((v)=>{ return v !== '.' }) }
	frase = f:(palabra / sep / ignorar)+ { return f.join('') }
	palabra = l:([a-z]i+) { return l.join('') }
	sep = ' ' / ',' / ';' / ':'
	punto = '.'
	ignorar = '\n' { return '' }

#### Reconocer url mínima

	url = u:(protocolo dominios ruta) { return u.join('') }
	ruta = r:(sepU pal?)+ { return r.map((v)=>{ return v.join('')} ).join('') }
	dominios = d:(pal sepD?)+ { return d.map((v)=>{ return v.join('')} ).join('') }
	protocolo = x:('http' 's'? ) y:('://') {return x.join('') + y}
	sepD = '.'
	sepU = '/'
	pal = s:([a-z]i)+ { return s.join('') }

#### Expandir notaciones

	{
		const acciones = {
			'f': 'fundir',
			'g': 'gratinar',
			'h': 'hervir'
		}
	}

	todo = t:(eval / ignorar)* { return t.join(' ') }
	eval = a:(acc) sep s:(val) ' '? { return a + ' ' + s + ' minutos'}
	sep = ':'
	acc = k:('f' / 'g' / 'h') { return acciones[k] }
	val = s:([0-9]*'.'*[0-9]*) { return s.map((v)=>{ return v.join('')}).join('') }
	ignorar = s:(.+) { return s.join('') }


### Dar formato

Intercalar texto con otros signos

	unido_con_guion = s:(.)* { return s.join('-') }

Espejar el texto

	escritura_inversa = s:(.)* { return s.reverse().join('') }

Generar un palíndromo con el texto

	escritura_palindromica = s:(.)* {
		let d = s.join('');
		let r = s.reverse().join('');
		return d + r
	}

Número siguiente

	entero_siguiente = n:[0-9]+ { return ((v)=>{ return v + 1})(parseInt(n)); }



### Aplicar contadores, numeradores, clasificadores

#### Contador como función global

	{
		function res (s){
			return s.length
		}
	}
	signos = s:(.)* { return res(s) }

#### Contador como función en variable global

	{
		var res = function (s){
			return s.length
		}
	}
	signos = s:(.)* { return res(s) }


#### Contador como función en variable local

	{
		let res = function (s){
			return s.length
		}
	}
	signos = s:(.)* { return res(s) }

#### Contador como función constante

	{
		const res = function (s){
			return s.length
		}
	}
	signos = s:(.)* { return res(s) }

#### Contador como función en objeto

	{
		const o = {
			res: function (s){
				return s.length
			}
		}
	}
	signos = s:(.)* { return o.res(s) }

#### Contador como función anónima sin entorno

	signos = s:(.)* { return ((v) => { return v.length })(s) }


#### Numerador con variable y formateador

	{
		let contador = 0;
	}
	todo = signos*
	signos = s:(.) { contador +=1; return `${contador} - ${s}`}

#### Clasificar y contar signos

	{
		let dat = {'v':[], 'c':[], 'n':[], 's':[]};
		const agr = function(v, g){
    		dat[g].push(v)
		}
		const res = function(){
    		var v, k, sig, can, r = [];
    		for( k in dat ){
      			v = dat[k];
      			sig = v.sort().join('');
      			can = '(' + v.length + ' ' + k + ') >>> ';
      			r.push(can + sig);
			}
           return r
	   }
	}

	ee = (v / c / s / n)* { return res(); }

	v = s:('a'i / 'e'i / 'i'i / 'o'i / 'u'i)
		{ agr(s, 'v') }

	c = s:('b'i / 'c'i / 'd'i / 'f'i
		/ 'g'i / 'h'i / 'j'i / 'k'i
		/ 'l'i / 'm'i / 'n'i / 'ñ'i
		/ 'p'i / 'q'i / 'r'i / 's'i
		/ 't'i / 'v'i / 'w'i / 'x'i
		/ 'y'i / 'z'i )
		{ agr(s, 'c') }

	s = s:( ' ' / '+' / '-' / '*' / '/' / '\\'
		/ '%' / '#' / '@' / '$' / '&' )
		{ agr(s, 's') }

	n = s:([0-9]) { agr(s, 'n') }
