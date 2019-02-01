# roda só uma ver na vida pra baixar, depois nao precisa mais
#install.packages("read.dbc")

#ativa a lib
library("read.dbc")

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