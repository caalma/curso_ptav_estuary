#!/usr/bin/python3
# -*- coding:utf-8 -*-

from sys import argv
from os import listdir
from os.path import exists, isdir, isfile, splitext, join
import json
from configuracion import formatos_permitidos

texto_ayuda = """
Ejemplo de uso:

{archivo_script} ../audio/ archivo.json

Requiere que se le indique un ruta de carpeta.
Dicha ruta debe contener carpetas con archivos para samples.
Opcionalmente puede indicarsele un nombre de archivo para grabar el json. En caso de no hacerlo el nombre por defecto es samples.json .
Los formatos permitidos para samples son: {formatos_permitidos} .

"""


def mostrar_ayuda(error=None, exit_=False):
    if error:
        print(f'---- ERROR\n{error}\n----')
    print(texto_ayuda.format(
        archivo_script=argv[0],
        formatos_permitidos=', '.join(formatos_permitidos.keys())
    ))

    if exit_:
        exit()


def crear_json_de_samples(ruta, archivo_json):
    if not exists(ruta):
        mostrar_ayuda('La ruta indicada no existe.', True)
    elif not isdir(ruta):
        mostrar_ayuda('La ruta indicada no es una carpeta.', True)
    else:
        la = [nomb for nomb in listdir(ruta) if isdir(f'{ruta}{nomb}')]
        lsamples = []

        for c in la:
            ruta_c = f'{ruta}{c}'
            lac = listdir(ruta_c)

            for n, arc in enumerate(sorted(lac)):
                ruta_c_ar = f'{ruta_c}/{arc}'

                if isfile(ruta_c_ar):
                    arc_extension = splitext(arc)[-1].strip('.')

                    if arc_extension in formatos_permitidos:
                        item =  {
                            'type': formatos_permitidos[arc_extension],
                            'bank': c,
                            'n': n,
                            'url': f'{c}/{arc}'
                        }
                        lsamples.append(item)

        with open(join(ruta, archivo_json), 'w') as f:
            f.write(json.dumps(lsamples, indent=4))


if __name__ == '__main__':

    if len(argv) < 2:
        mostrar_ayuda()
    else:
        archivo = 'samples.json' if len(argv) < 3 else argv[2]
        crear_json_de_samples(argv[1], archivo)
