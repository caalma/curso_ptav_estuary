/*
 * Estuary Ajuste Local
 *
 * Autor: https://github.com/caalma
 * Licencia: CC0 1.0 Universal
 * Documentación: https://caalma.github.io/curso_ptav_estuary/utiles/eal.html
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
