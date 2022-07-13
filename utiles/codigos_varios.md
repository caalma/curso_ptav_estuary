# Automatizaciones útiles

## Secuencia a video

	ffmpeg -f image2 -pattern_type glob -i 'p*.jpg' -b 8000k -r 25 ../naranjo.mp4

	ffmpeg -f image2 -pattern_type glob -i './png/*.png' -b 8000k -r 25 ./$(basename $(pwd)).mov

## Secuencia a gif

	convert png_/*.png $(basename $(pwd)).gif


## Procesar muchas carpetas

	raiz=$(pwd); for carpeta in *;do cd $carpeta; echo $(pwd); imagen_reducir 1000;  cd $raiz; done


	raiz=$(pwd); for carpeta in *;do cd $carpeta; echo $(pwd); ffmpeg -f image2 -pattern_type glob -i './*.jpg' -b 8000k -r 6 ../$(basename $(pwd)).mov; cd $raiz; done


## Obtener característica de todos los audios/videos masivamente

### Calidad, Encoder, Duracion y bitrate

	AT=/tmp/x; for AU in $(find -type f); do ffprobe $AU 2> $AT && echo "${AU}, " $(grep 'Stream' $AT) ", " $(grep 'Duration' $AT) ; done > data_audios.txt

## Actualización con Git para Github

	Gr="./utiles/"; Gm="Ajuste de contenido"; git add "$Gr" && git commit -m "$Gm" && git push