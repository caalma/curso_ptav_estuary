# Automatizaciones útiles

## Secuencia a video

	ffmpeg -f image2 -pattern_type glob -i 'p*.jpg' -b 8000k -r 25 ../naranjo.mp4

	ffmpeg -f image2 -pattern_type glob -i './png/*.png' -b 8000k -r 25 ./$(basename $(pwd)).mov

## Secuencia a gif

	convert png_/*.png $(basename $(pwd)).gif


## Procesar muchas carpetas

	raiz=$(pwd); for carpeta in *;do cd $carpeta; echo $(pwd); imagen_reducir 1000;  cd $raiz; done


	raiz=$(pwd); for carpeta in *;do cd $carpeta; echo $(pwd); ffmpeg -f image2 -pattern_type glob -i './*.jpg' -b 8000k -r 6 ../$(basename $(pwd)).mov; cd $raiz; done


## Recortar y redimensionr video

	arc_a='video.mp4';
	arc_z='video_rr.mp4';
	rc_ancho=720;
	rc_alto=720;
	rc_x=280;
	rc_y=0;
	rd_ancho=-1;
	rd_alto=500;
	ffmpeg -i "$arc_a" -vf "crop=${rc_ancho}:${rc_alto}:${rc_x}:${rc_y},scale=${rd_ancho}:${rd_alto}" -c:v libx264 -crf 1 "$arc_z"


## Obtener característica de todos los audios/videos masivamente

### Calidad, Encoder, Duracion y bitrate

	AT=/tmp/x; for AU in $(find -type f); do ffprobe $AU 2> $AT && echo "${AU}, " $(grep 'Stream' $AT) ", " $(grep 'Duration' $AT) ; done > data_audios.txt


## Actualización con Git para Github

	Gr="./utiles/"; Gm="Ajuste de contenido"; git add "$Gr" && git commit -m "$Gm" && git push


--
