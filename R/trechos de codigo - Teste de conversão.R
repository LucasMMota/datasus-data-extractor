install.packages("read.dbc")

#ativa a lib
library("read.dbc")

getwd()
setwd("/diretorio-de-trabalho")

#lib datasus R
#devtools::install_github("danicat/read.dbc") dev

# The 'sids.dbc' file is the compressed version of 'sids.dbf' from the "foreign" package.
x <- read.dbc(system.file("files/sids.dbc", package="read.dbc"))
str(x)
summary(x)

# This is a small subset of U.S. National Oceanic and Atmospheric Administration???s (NOAA) storm database.
storm <- read.dbc(system.file("files/storm.dbc", package="read.dbc"))
head(x)
str(x)
# ---------------------
# Don't run!
# The following code will download data from the "Declarations of Death" database for
# the Brazilian state of Parana, year 2013. Source: DATASUS / Brazilian Ministry of Health
url <- "ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES/DOPR2013.dbc"
download.file(url, destfile = "DOPR2013.dbc") # isto vai baixar o arq
dopr <- read.dbc("DOPR2013.dbc")
head(dopr)
str(dopr)
View(dopr)
# ---------------------



#########
# converter arquivos cbd
# Input file name
in.f  <- system.file("files/sids.dbc", package = "read.dbc")
# Output file name
out.f <- tempfile(fileext = ".dbc")

# The call return logi = TRUE on success
if( dbc2dbf(input.file = in.f, output.file = out.f) ) {
  print("File decompressed!")
  file.remove(out.f)
}
out.f



#####
# converter arquivos dbc em csv
# leio o dbc
x <- read.dbc("/Users/lucas/Documents/P??s-POLI/Monografia/ACFSP1803.dbc")
#escrevo o csv
write.csv(x,file="ACFSP1803.csv")

#ver csv salvo
x <- read.csv("/Users/lucas/Documents/P??s-POLI/Monografia/ACFSP1803.csv")
View(x)
str(x)
