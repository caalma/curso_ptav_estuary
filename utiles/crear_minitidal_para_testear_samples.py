#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Autor: https://github.com/caalma
# Licencia: CC0 1.0 Universal

from sys import argv
from os.path import basename, splitext
import json
import requests

texto_ayuda = """
Ejemplo de uso:

{archivo_script} "https://caalma.github.io/curso_ptav_estuary/audio/samples.json" codigo.minitidal

Requiere que se le indique una URL correspondiente a un listado de samples en formato json para minitidal.
"""


def mostrar_ayuda(error=None, exit_=False):
    if error:
        print(f'---- ERROR\n{error}\n----')
    print(texto_ayuda.format(
        archivo_script=argv[0]
    ))

    if exit_:
        exit()


def crear_minitidal_para_testear_samples(url, archivo):
    dat_json = json.loads(requests.get(url).content)

    dat_dict = {}
    for audio in dat_json:
        if not audio['bank'] in dat_dict:
            dat_dict[audio['bank']] = 0
        dat_dict[audio['bank']] += 1


    minitidal_test_lineas = []
    for banco, cantidad in dat_dict.items():
        minitidal_test_lineas.append(f'  -- n "0 .. {cantidad}" # s "{banco}" # gain 0.8')

    minitidal_test_lineas.append('  s ""')

    minitidal_test_bloque = [
        f'-- !reslist "{url}" ',
        "stack ["
    ] + [',\n'.join(minitidal_test_lineas)] + [
        "]"
    ]

    with open(archivo, 'w') as f:
        f.write('\n'.join(minitidal_test_bloque))

if __name__ == '__main__':
    if len(argv) < 2:
        mostrar_ayuda()
    else:
        url = argv[1]
        nombre_sample = splitext(basename(url))[0]
        archivo = f'{nombre_sample}-test.minitidal' if len(argv) < 3 else argv[2]
        crear_minitidal_para_testear_samples(url, archivo)
