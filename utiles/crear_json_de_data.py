#!/usr/bin/python3
# -*- coding:utf-8 -*-

from sys import argv
from os import listdir
from os.path import exists, isdir, isfile, splitext, join, realpath
import json
from subprocess import Popen, PIPE
from configuracion import formatos_permitidos

texto_ayuda = """
Ejemplo de uso:

{archivo_script} ../audio/ archivo.json

Requiere que se le indique un ruta de carpeta.
Dicha ruta debe contener carpetas con archivos para samples.
Opcionalmente puede indicarsele un nombre de archivo para grabar el json. En caso de no hacerlo el nombre por defecto es data.json .
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

def obtener_datos(ruta):
    ruta = realpath(ruta)
    cmd = f'cd "{ruta}"; AT=/tmp/x; for AU in $(find -type f); do ffprobe $AU 2> $AT && echo "$AU, " $(grep "Stream" $AT) ", " $(grep "Duration" $AT) ; done'
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    error = p.stderr.read()
    if not error:
        lineas = p.stdout.read().decode('utf8').strip().split('\n')
        data = []
        for l in lineas:
            d = l.split(',')
            obj = { 'filename': d[0].strip() }
            for prop in d[1:]:
                d = prop.split(': ')
                k = d[0].strip().lower()
                if k == 'Duration':
                    obj['duration'] = d[1].strip()
                elif k == 'bitrate':
                    obj['bitrate'] = d[1].strip()
                elif 'hz' in k:
                    obj['hz'] = k.split(' ')[0]
                elif 'channel' in k:
                    obj['channels'] = k.split(' ')[0]
                elif 'stream' in k:
                    if d[1].lower() == 'audio':
                        obj['encoder'] = d[2].split(' ')[0]

            data.append(obj)
        return data
    else:
        return None


def crear_json_con_data(ruta, archivo_json):
    if not exists(ruta):
        mostrar_ayuda('La ruta indicada no existe.', True)
    elif not isdir(ruta):
        mostrar_ayuda('La ruta indicada no es una carpeta.', True)
    else:
        datos = obtener_datos(ruta)
        ldata = []
        for dat in datos:
            arc_extension = splitext(dat['filename'])[-1].strip('.')
            if arc_extension in formatos_permitidos:
                ldata.append(dat)

        with open(join(ruta, archivo_json), 'w') as f:
            f.write(json.dumps(ldata, indent=4))


if __name__ == '__main__':

    if len(argv) < 2:
        mostrar_ayuda()
    else:
        archivo = 'data.json' if len(argv) < 3 else argv[2]
        crear_json_con_data(argv[1], archivo)
