/*
 * Estuary Ajuste Local
 *
 * Ver documentación en:
 * https://github.com/caalma/curso_ptav_estuary/utiles/eal.md
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
