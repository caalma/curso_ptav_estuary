#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Autor: https://github.com/caalma
# Licencia: CC0 1.0 Universal

from sys import argv
from subprocess import Popen, PIPE
from os import makedirs
from shutil import rmtree
import yaml
from datetime import datetime

ayuda = """
Generador de GIFs Animados con letras.
Actualizado: 2022-07-21 - 01:27:26

Requiere:
    imagemagick

Modo de uso:
    {script} listar_fuentes
                                   # actualiza el listado de tipografía con
                                   # todas las instaladas en el sistema operativo.
                                   # graba el listado en fuentes_disponibles.txt

    {script} crear_gif "texto" clave_seteo
                                   # crea un gif animado mediante el texto proporcionado
                                   # y la clave de un seteo disponible en seteos.yml
"""

def mostrar_ayuda(salir=True):
    print(ayuda.format(**{
        'script': __file__
    }))
    if salir:
        exit()

def letra_a_fotograma(cfg):
    if cfg['signo'] == ' ':
        cmd = "convert -size {i_ancho}x{i_alto} xc:'{c_fondo}' {i_nombre}".format(**cfg)
    else:
        cmd = "convert -size {i_ancho}x{i_alto} -gravity center -background '{c_fondo}' -fill '{c_figura}' -font '{f_fuente}' -pointsize {f_medida} label:'{signo}' {i_nombre}".format(**cfg)

    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    err = p.stderr.read().decode('utf8')
    out = p.stdout.read().decode('utf8')

    if err:
        print(err)
        mostrar_ayuda(True)

    return True


def fotogramas_a_gif(texto, seteo):
    with open('seteos.yml', 'r') as f:
        seteos = yaml.safe_load(f)
        if not seteo in seteos:
            mostrar_ayuda(True)

    cfg = seteos[seteo]
    ruta_tmp = '.tmp-fotogramas/'
    ahora = datetime.now()
    instante = int(ahora.timestamp())
    arc_nombre = f'animacion-{instante}.gif'

    makedirs(ruta_tmp, exist_ok=True)

    for i in range(0, len(texto)):
        cfg_ftg = cfg.copy()
        cfg_ftg['f_fuente'] = cfg['f_fuente'][i % len(cfg['f_fuente'])]
        cfg_ftg['f_medida'] = cfg['f_medida'][i % len(cfg['f_medida'])]
        cfg_ftg['c_fondo'] = cfg['c_fondo'][i % len(cfg['c_fondo'])]
        cfg_ftg['c_figura'] = cfg['c_figura'][i % len(cfg['c_figura'])]
        cfg_ftg['signo'] = texto[i]
        cfg_ftg['i_nombre'] = f'{ruta_tmp}{i:06d}.png'
        letra_a_fotograma(cfg_ftg)

    cfg_anim = cfg.copy()
    cfg_anim['arc_nombre'] = arc_nombre
    cfg_anim['ruta_tmp'] = ruta_tmp

    cmd = ' '.join(
        ['convert -dispose none -delay 0 -size {i_ancho}x{i_alto} 0 xc:transparent',
         '-dispose previous -delay {i_retardo} {ruta_tmp}*.png -loop {i_repeticiones}',
         '{arc_nombre}'])

    p = Popen(cmd.format(**cfg_anim), shell=True, stdout=PIPE, stderr=PIPE)
    err = p.stderr.read().decode('utf8')
    out = p.stdout.read().decode('utf8')

    if err:
        print(err)
    else:
        print(arc_nombre)

    rmtree(ruta_tmp, ignore_errors=True)

def listar_fuentes_tipograficas_disponibles():
    cmd = 'convert -list font'
    p = Popen(cmd, shell=True, stdout=PIPE)
    text = p.stdout.read().decode('utf8').strip().split('\n')
    k = ' Font: '
    fuentes = [l.replace(k, '').strip() for l in text if k in l]
    fuentes.remove('.')

    with open('fuentes_disponibles.txt', 'w') as f:
        f.write('\n'.join(sorted(fuentes)))


if __name__ == '__main__':
    if len(argv) < 2:
        mostrar_ayuda()

    elif argv[1] == 'crear_gif':
        if len(argv) < 4:
            mostrar_ayuda()
        texto = argv[2]
        seteo = argv[3]
        fotogramas_a_gif(texto, seteo)
    elif argv[1] == 'listar_fuentes':
        listar_fuentes_tipograficas_disponibles()
    else:
        mostrar_ayuda()
