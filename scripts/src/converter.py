import subprocess
from .constants import SRC_DIR, RAW_FILES_DIR, CONVERTED_FILES_DIR


def dbc2dbf(file):
    dbc2csv_path = SRC_DIR + "/dbc2csv.R " + RAW_FILES_DIR + " " + CONVERTED_FILES_DIR + " " + file

    try:
        print(subprocess.call("/usr/local/bin/Rscript --vanilla " + dbc2csv_path, shell=True))
    except:
        print("(R) Error converting " + file)

    return

