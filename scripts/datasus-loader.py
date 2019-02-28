import src.filters as filters
import src.downloader as downloader
from src.utils import build_file_path
from src.converter import dbc2dbf


# todo: mapear ranges e retornar msg quando não tem
def main():
    print('iniciando...')

    for date in filters.getDateRange():
        for type in filters.get_types():
            for state in filters.states():
                print('Selected date: ' + date)
                print('Selected type: ' + type)
                print('Selected state: ' + state)

                src_file, filename = build_file_path(filters.system(), type, date, state)
                downloader.download(src_file, filename)

                dbc2dbf(filename)
                # load into db


# Let`s rock!
main()
