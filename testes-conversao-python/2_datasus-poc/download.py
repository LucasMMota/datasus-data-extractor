import sys
sys.path.insert(0, "~/Documents/Pos-POLI/Monografia-2019/datasus-data-extractor/src-virtualenv-datasus/lib/python3.7/site-packages/pysus/utilities/")
from pysus.utilities.readdbc import read_dbc

filename = '/Users/lucas/Documents/Pos-POLI/Monografia-2019/datasus-data-extractor/pyhton/ERSP180.dbf'

df = read_dbc(filename, encoding='iso-8859-1')
df.info()

