# Testeo de formatos multimedia



---

## Referencias Rápidas

| IMAGEN | CineCer0 | Hydra | Notas |
|:-------|:--------:|:-----:|:------|
| bmp    | si       | si    | |
| gif    | si       | si    | |
| ico    | si       | si    | |
| jpg    | si       | si    | |
| png    | si       | si    | En Hydra no muestra la transparencia correctamente. |
| svg    | si       | si    | |
| tiff   | no       | no    | |
| webp   | si       | si    | En Hydra no muestra la transparencia correctamente. |


| AUDIO  | MiniTidal | Notas |
|:-------|:---------:|:------|
| aiff   | no        | |
| flac   | si        | |
| m4a    | si        | |
| mp3    | si        | |
| ogg    | no        | |
| wav    | si        | |


| VIDEO  | CineCer0 | Hydra | Notas |
|:-------|:--------:|:-----:|:------|
| avi    | no       | no    | |
| mkv    | si       | si    | |
| mov    | si       | si    | |
| mp4    | si       | si    | |
| ogg    | si       | si    | |
| webm   | si       | si    | |


| VIDEO con TRANSPARENCIA  | CineCer0 | Hydra | Notas |
|:-------------------------|:--------:|:-----:|:------|
| mov    | no       | ??    | |
| webm   | si       | si    | |


---


## Códigos de las pruebas para IMÁGENES


### bmp

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.bmp"

Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.bmp");src(s0).out()


### ico

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.ico"

Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.ico");src(s0).out()


### jpg

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.jpg"

Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.jpg");src(s0).out()


### png

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.png"


Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.png");src(s0).out()


### svg

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.svg"

Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.svg");src(s0).out()


### tiff

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.tiff"

Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.tiff");src(s0).out()


### webp

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.webp"

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test_alpha.webp"


Hydra

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.webp");src(s0).out()

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test_alpha.webp");src(s0).out()


### gif

CineCer0

	image "https://caalma.github.io/curso_ptav_estuary/test/videos/test.gif"

Hydra

Sólo muestra el primer fotograma, si es GIF Animado.

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/videos/test.gif");src(s0).out()


---

## Códigos de las pruebas para AUDIOS


Importar los samples desde el input de consola en Estuary:

	!reslist "https://caalma.github.io/curso_ptav_estuary/test/audios/samples.json"


### wav

Minitidal

	s "testwav"


### aiff

Minitidal

	s "testaiff"


### flac

Minitidal

	s "testflac"


### mp3

Minitidal

	s "testmp3"


### m4a

Minitidal

	s "testm4a"


### ogg

Minitidal

	s "testogg"


---


## Códigos de las pruebas para VIDEOS


### mov

Encoder: Lavf58.29.100

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.mov"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.mov");src(s0).out()


### mov (con alpha)

Encoder: Lavf58.29.100

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.mov"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.mov");src(s0).out()



### mp4

Encoder: Lavf58.29.100

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.mp4"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.mp4");src(s0).out()


### mkv

Encoder: Lavc58.54.100 libx264

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.mkv"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.mkv");src(s0).out()


### webm

Encoder: Lavc58.54.100 libvpx-vp9

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.webm"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.webm");src(s0).out()


### webm (con alpha)

Encoder: Lavf58.29.100 libvpx-vp9

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.webm"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.webm");src(s0).out()


### avi

Encoder: Lavf58.29.100

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.avi"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.avi");src(s0).out()



### ogg

Encoder: Lavc58.54.100 libtheora

CineCer0

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.ogg"

Hydra

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.ogg");src(s0).out()
