import src.filters as filters
import src.downloader as downloader
from src.utils import build_file_path, get_downloaded_size
from src.converter import dbc2dbf


# todo: mapear ranges e retornar msg quando não tem
#nao baixar tudo de novo se para o script
#fazer um script so de apagar dbc
def main():
    print('iniciando...')

    for date in filters.getDateRange():
        for type in filters.get_types():
            for state in filters.states():
                print('Selected date: ' + date)
                print('Selected type: ' + type)
                print('Selected state: ' + state)

                dowloaded_size = get_downloaded_size()
                if dowloaded_size >= filters.getDownloadLimit():
                    print("Download limit reached: " + str(dowloaded_size))
                    print("Stopping...")
                    exit(1)

                src_file, filename = build_file_path(filters.system(), type, date, state)
                downloader.download(src_file, filename)

                dbc2dbf(filename)
                # load into db


# Let`s rock!
main()
