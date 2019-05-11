import ftplib
from .constants import RAW_FILES_DIR, ERROR_LOG_FILES_DIR
from os.path import exists
from os import makedirs


def save_log_on_errors(result, filename):
    if not exists(ERROR_LOG_FILES_DIR):
        makedirs(ERROR_LOG_FILES_DIR)

    if '226' not in result:
        log_name = ERROR_LOG_FILES_DIR+'not-downloaded.txt'
    #else:
    #    log_name = ERROR_LOG_FILES_DIR + 'downloaded.txt'

    with open(log_name, "a") as error_log:
        error_log.write(filename+'\n')


def download(file_path, filename):
    print('File: ' + filename)

    raw_file = RAW_FILES_DIR + '' + filename

    try:
        ftp = ftplib.FTP("ftp.datasus.gov.br")
        ftp.login()
        ftp.cwd(file_path)
        result = ftp.retrbinary("RETR " + filename, open(raw_file, 'wb').write)
        #if_file_is_empty_delete_it(filename)#it's better to delete on local than list all the files in ftp
        ftp.quit()
        save_log_on_errors(result, filename)
    except:
        # file does not exist for given filters
        return
