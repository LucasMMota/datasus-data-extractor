### DataSUS downloader
This project aims to access a given DataSUS system databse and download its data into a local or remote repository (on a Data Staging).

Example:
 
`python datasus-loader.py --fromSystems='SIA,SIH,SINASC' --toDatabase='<mongo-dbase-name>'
--filterFrom='01/2010' --filterTo='12/2011' --filterUF='SP,RJ'`
###Steps

#####Extraction

* connect to FTP (whether necessary do it before)
* Download file into `raw-files`

#####Transform
* Convert (through R script) and save into `converted-files`
* Deletes source (`.dbc`)

#####Load
* Save into a chosen Data Staging Database (decide which?)



#####Questions:
* Needs filters (data) to download the files
* which DB use?
    - needs research and references (maybe casandra)
* which transformation would it be necessary (like data quality)?
    - Victor can handle this
* It will be a hardcoded system on script, it should make it possible to chose wich Datasus system to access.


#####Todos
* apresentar no trabalho todo o layout dos arquivos do datasus
    - pedir pro victor fazer isso
* e explicar como funcionar
* explicar constituicao do FTP, nome dos arquivos por TIPO UF Data

