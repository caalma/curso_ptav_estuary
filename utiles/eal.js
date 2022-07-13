/*
 * Estuary Ajuste Local
 *
 * Modo de uso:
 * una vez cargado a la consola javascript del browser,
 * utilizar alguna de estas funciones con valores flotantes entre 0 y 1.
 *
 *--  EAL.verInterfaz(0.5);
 *--  EAL.verVisuales(0.2);
 *
 * Otra forma de cargarlo a la página de forma local es agregando el siguiente código en la consola de javascript del broser:
 *
 *-- (function(){ let s = document.createElement('script'); s.src = 'https://caalma.github.io/curso_ptav_estuary/utiles/eal.js'; document.body.appendChild(s); })()
 *
*/

var EAL = EstuaryAjusteLocal = {
    verInterfaz : (v=1)=>{
	for(let x of ['header', 'page', 'terminal', 'footer']){
	    document.getElementsByClassName(x)[0].style = `opacity:${v}`;
	}},
    verVisuales : (v=1)=>{
	for(let x of document.getElementsByClassName('canvas-or-svg-display')){
	    x.style =`opacity:${v}`;
	}
    }
}
