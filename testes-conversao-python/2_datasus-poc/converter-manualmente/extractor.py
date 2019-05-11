# import shutil
# import urllib2
# from contextlib import closing
import canmatrix.convert as cv

datasus_basedir = 'ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/dados/'
os_basedir = '/Users/lucas/Documents/Pos-POLI/Monografia-2019/datasus-data-extractor/pyhton/'

dsus_file = 'CIH-CR.dbc.dbc'

# extraction
# with closing(urllib2.urlopen(datasus_basedir+dsus_file)) as r:
#     new_file_downloaded = os_basedir+dsus_file
#     with closing(open(new_file_downloaded, 'wb')) as f:
#         shutil.copyfileobj(r, f, )
#         print(r)
#         print(f)

# convertion
cv.mainConvert(
    '/Users/lucas/Documents/Pos-POLI/Monografia-2019/datasus-data-extractor/pyhton/ERSP1807.dbc',
    '/Users/lucas/Documents/Pos-POLI/Monografia-2019/datasus-data-extractor/pyhton/ERSP180.dbf')

#
# import cantools
# from pprint import pprint
# db = cantools.database.load_file('/Users/lucas/Documents/Pos-POLI/Monografia-2019/datasus-data-extractor/pyhton/ERSP1807.dbc')
# print(db.messages)
# #
# # example_message = db.get_message_by_name('ExampleMessage')
# # pprint(example_message.signals)
