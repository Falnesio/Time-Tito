# Write a function that reads a directory full of files and reports 
# the number of completely observed cases in each data file. The 
# function should return a data frame where the first column is the 
# name of the file and the second column is the number of complete 
# cases. A prototype of this function follows

complete <- function(directory, id = 1:332){
  list_of_ids <- c()
  list_of_lengths <- c()
  for(i in id){
    if(i < 10){
      i <- paste("00", i, sep = '')
    }
    else if(i < 100){
      i <- paste("0", i, sep = '')
    }
    file_location <- paste(directory, "/", i, ".csv", sep = '')
    all_data <- as.data.frame(read.csv(file_location))
    complete_data <- complete.cases(all_data)
    list_of_ids <- c(list_of_ids, as.numeric(i))
    list_of_lengths <- c(list_of_lengths, sum(complete_data))
  }
  
  table <- data.frame(id = list_of_ids, nobs = list_of_lengths)
  print(table)
}
