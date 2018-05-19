#!/usr/bin/python3

import csv
import json
import sys
import os

import arrow

default_row = {
    'Bucle': False,
    'ValorBucle': -1,
    'BucleDes': -1,
    'isPartipacion': False,
    'ValorDataContext': None,
    'ValorFormateado': None,
    'Tag': None
}


class CsvToJSON():
    """docstring for CsvToJSON"""
    def __init__(self):
        self.src = ''
        self.dst = ''
        self.csv = None

    def parse(self, src):
        self.src_dst(src)
        self.read_csv()
        self.write_json()

    def src_dst(self, src):
        if os.path.exists(src) and os.path.isfile(src):
            self.src = os.path.abspath(src)
        else:
            while not os.path.exists(self.src) or not os.path.isfile(self.src):
                self.src = input('Introduce una ruta al archivo CSV: ')
            self.src = os.path.abspath(self.src)
        dirname, filename = os.path.split(self.src)
        rootname = os.path.split(dirname)[0]
        dst_dir = os.path.join(rootname, 'JSON')  # PARAMETROS_JSON
        basename = '.'.join(filename.split('.')[0:-1])
        dst_filename = 'Entidad' + basename + '.json'
        self.dst = os.path.join(dst_dir, dst_filename)

    def read_csv(self):
        headers = ['Campos', 'Def', 'Regs', 'Ini', 'Tipo', 'Decast']
        response = {
            'headers': headers,
            'content': []
        }
        with open(self.src, encoding='iso-8859-1') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for line in reader:
                if line[0].find('#') != 0 and line[0].find('$'):
                    new_row = default_row.copy()
                    for key, row in enumerate(line):
                        if key < len(headers):
                            new_row[headers[key]] = row
                    response['content'].append(new_row)
        self.csv = response
        return response

    def write_json(self):
        response = {
            'NombreFichero': '',
            'fechaCreacion': arrow.now().isoformat(),
            'listaRegistros': self.csv['content']
        }
        with open(self.dst, 'w+') as fp:
            json.dump(response, fp)
        return response


if __name__ == '__main__':
    csv_src = './ELECCIONES/CSV/FDPARTID.csv'
    csv_src = './ELECCIONES/CSV/FDCANDID.csv'
    csv_src = './ELECCIONES/CSV/FDCONLEM.csv'
    csv_src = ''
    obj = CsvToJSON()
    if len(sys.argv) > 1:
        csv_src = sys.argv[1]
    obj.parse(csv_src)
