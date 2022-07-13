/*
 * Estuary Ajuste Local
 *
 * modo de uso:
 *  EAL.verInterfaz(0.5);
 *  EAL.verVisuales(0.2);
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
