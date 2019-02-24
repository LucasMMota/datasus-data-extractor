#python daasus-loader.py --fromSystems='SIA,SIH,SINASC' --toDatabase='<mongo-dbase-name>'
#--filterFrom='01/2010' --filterTo='12/2011' --filterUF='SP,RJ'
# filters

# todo: mapear ranges e retornar msg quando não tem

import subprocess

def getPath(system, type, date, UFFilter):

    filename = type+UFFilter+date+'.dbc'
    path = 'ftp://ftp.datasus.gov.br/dissemin/publicos/'+system+'/200801_/Dados/'+filename

    print('Path: ')
    print(path)
    return path

#Gets range data to read available files
def getDateRange(fromFilter, toFilter):
    return ['1701']

def download(filePath):
    return True

def getSystem():
    return 'SIASUS'

def getTypes():
    return ['AD']

def getDateFrom():
    return ['02/2017']

def getDateTo():
    return ['02/2017']

def getUFs():
    return ['SP']

def extractUFsFiles(system, type, ufs, date):
    for uf in ufs:
        srcFile = getPath(system, type, date, uf)

        print('Downloading ' + srcFile)
        download(srcFile)

        # convert
        # load into db

def extractTypesFiles(system, types, ufs, date):
    for type in types:
        extractUFsFiles(system, type, ufs, date)


def main():

    print('iniciando...')

    system = getSystem()
    types = getTypes()
    UFs = getUFs()

    fromFilter = getDateFrom()
    toFilter = getDateTo()

    for range in getDateRange(fromFilter, toFilter):
        date = range

        extractTypesFiles(system, types, UFs, date)


# Let`s rock!
main()
