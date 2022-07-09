# Automatizaciones útiles

## Secuencia a video

	ffmpeg -f image2 -pattern_type glob -i 'p*.jpg' -b 8000k -r 25 ../naranjo.mp4

	ffmpeg -f image2 -pattern_type glob -i './png/*.png' -b 8000k -r 25 ./$(basename $(pwd)).mov

## Secuencia a gif

	convert png_/*.png $(basename $(pwd)).gif


## Procesar muchas carpetas

	raiz=$(pwd); for carpeta in *;do cd $carpeta; echo $(pwd); imagen_reducir 1000;  cd $raiz; done


	raiz=$(pwd); for carpeta in *;do cd $carpeta; echo $(pwd); ffmpeg -f image2 -pattern_type glob -i './*.jpg' -b 8000k -r 6 ../$(basename $(pwd)).mov; cd $raiz; done


## Obtener las característica de todos los audios/videos desde la carpeta actual

	AT=/tmp/x; for AU in $(find -type f); do ffprobe $AU 2> $AT && grep 'Stream' $AT;done > tipos_de_samples.txt

## Actualización con Git para Github

	Gr="./utiles/"; Gm="Ajuste de contenido"; git add "$Gr" && git commit -m "$Gm" && git push


## Generar videos transparentes con kdenlive

1 - Elegir el video a usar y aplicarle la transparencia por efecto de transformación o por imagen png transparente.
2 - Configurar el "Modo de Composición" (en las utilidades del bloque de pistas).
3 - Exportar eligiendo desde el grupo de "Videos transparentes" entre : mov, webm (vp9).
