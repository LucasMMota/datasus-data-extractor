import subprocess

print('py converting...')
subprocess.call ("/usr/local/bin/Rscript --vanilla ./dbc2csv.R", shell=True)
print('py done')