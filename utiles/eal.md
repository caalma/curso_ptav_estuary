# Estuary Ajuste Local

Ajuste que permite variar la visibilidad de los componentes de la página web Estuary para realizar livecoding colaborativo.

##   Modo de uso:
1. Acceder a la web https://estuary.mcmaster.ca/
2. Abrir la consola de de javascript del browser, presionando Ctrl+Shit+I o F12, o buscando el botón en el menu de utilidades del browser.
3. Pegar el siguiente código en la de javascript del browser:

		(function(){ let s = document.createElement('script'); s.src = 'https://caalma.github.io/curso_ptav_estuary/utiles/eal.js'; document.body.appendChild(s); })()

4. En la misma consola utilizar las funciones `verInterfaz` o `verVisuales` del objeto `EAL`. Por ejemplo:

- `EAL.verInterfaz(0.5);`
- `EAL.verVisuales(0.2);`

5. Los valores aceptados en esas funciones son números decimales entre 0 y 1.
