Para este lab estoy subiendo dos archivos uno llamado Main.py en donde esta el codigo utilizando el concurrency y otro llamado MainWithoutConcurrency.py que es el codigo sin la concurrencia. 
El que no tiene concurrencia dura aproximadamente 33-40 segundos, mientras que en el otro logre que durara entre 4 a 3 segundos. 

Me di cuenta que el problema de perfomance era dado por un error de IO por lo tanto use threadpoolexecutor. 
