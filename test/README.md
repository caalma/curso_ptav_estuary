# Testeo de formatos multimedia

---

## Formatos de imagen


### bmp

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.bmp"

Hydra - **SI**

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.bmp");src(s0).out()


### ico

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.ico"

Hydra - **SI**

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.ico");src(s0).out()


### jpg

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.jpg"

Hydra - **SI**

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.jpg");src(s0).out()


### png

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.png"


Hydra - **SI**

Nota: No reconoció la transparencia.

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.png");src(s0).out()


### svg

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.svg"

Hydra - **SI**

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.svg");src(s0).out()


### tiff

CineCer0 - **NO**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.tiff"

Hydra - **NO**

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.tiff");src(s0).out()


### webp

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.webp"

	image "https://caalma.github.io/curso_ptav_estuary/test/imagenes/test_alpha.webp"


Hydra - **SI**

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test.webp");src(s0).out()


No muestra la transparencia.

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/imagenes/test_alpha.webp");src(s0).out()


### gif

CineCer0 - **SI**

	image "https://caalma.github.io/curso_ptav_estuary/test/videos/test.gif"

Hydra - **SI**

Sólo muestra el primer fotograma, si es GIF Animado.

	s0.initImage("https://caalma.github.io/curso_ptav_estuary/test/videos/test.gif");src(s0).out()


---

## Formatos de audio

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


## Formatos de video


### mov

Encoder: Lavf58.29.100

CineCer0 - **SI**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.mov"

Hydra - **SI**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.mov");src(s0).out()


### mov con alpha

Encoder: Lavf58.29.100

CineCer0 - **??**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.mov"

Hydra - **??**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.mov");src(s0).out()



### mp4

Encoder: Lavf58.29.100

CineCer0 - **SI**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.mp4"

Hydra - **SI**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.mp4");src(s0).out()


### mkv

Encoder: Lavc58.54.100 libx264

CineCer0 - **SI**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.mkv"

Hydra - **SI**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.mkv");src(s0).out()


### webm

Encoder: Lavc58.54.100 libvpx-vp9

CineCer0 - **SI**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.webm"

Hydra - **SI**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.webm");src(s0).out()


### webm (con alpha)

Encoder: Lavf58.29.100 libvpx-vp9

CineCer0 - **??**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.webm"

Hydra - **??**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.webm");src(s0).out()


### avi

Encoder: Lavf58.29.100

CineCer0 - **NO**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.avi"

Hydra - **NO**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.avi");src(s0).out()


### avi (con alpha)

Encoder: Lavf58.29.100

CineCer0 - **??**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.avi"

Hydra - **??**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test_alpha.avi");src(s0).out()


### ogg

Encoder: Lavc58.54.100 libtheora

CineCer0 - **SI**

	video "https://caalma.github.io/curso_ptav_estuary/test/videos/test.ogg"

Hydra - **SI**

	s0.initVideo("https://caalma.github.io/curso_ptav_estuary/test/videos/test.ogg");src(s0).out()
