#python datasus-loader.py --fromSystems 'SIA,SIH,SINASC' --toDatabase '<mongo-dbase-name>'
#--filterFrom '01/2010' --filterTo '12/2011' --filterUF 'SP,RJ'
# filters

# todo: mapear ranges e retornar msg quando não tem

import subprocess
import src.filters as filters
import src.downloader as downloader

def getPath(system, type, date, state):

    filename = type + state + date + '.dbc'
    path = 'ftp://ftp.datasus.gov.br/dissemin/publicos/'+system+'/200801_/Dados/'+filename

    print('Path: ')
    print(path)
    return path


def main():
    print('iniciando...')

    for date in filters.getDateRange():
        for type in filters.get_types():
            for state in filters.states():
                srcFile = getPath(filters.system(), type, date, state)
                print('\nDownloading ' + srcFile)
                downloader.download(srcFile)

                # convert
                # load into db


# Let`s rock!
main()
