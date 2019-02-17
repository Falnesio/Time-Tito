# Write a function named 'pollutantmean' that calculates the mean of a pollutant (sulfate or nitrate) 
# across a specified list of monitors. The function 'pollutantmean' takes three arguments: 'directory', 
# 'pollutant', and 'id'. Given a vector monitor ID numbers, 'pollutantmean' reads that monitors' particulate
# matter data from the directory specified in the 'directory' argument and returns the mean of the pollutant
# across all of the monitors, ignoring any missing values coded as NA. A prototype of the function is as follows

pollutantmean <- function(directory, pollutant, id = 1:332){
  mean_list <- c()
  weight_list <- c()
  for(i in id){
    if(i < 10){
      i <- paste("00", i, sep = '')
    }
    else if(i < 100){
      i <- paste("0", i, sep = '')
    }
    file_location <- paste(directory, "/", i, ".csv", sep = '')
    all_data <- as.data.frame(read.csv(file_location))
    polution_data <- all_data[, pollutant]
    complete_data <- polution_data[!is.na(polution_data)]
    mean_list <- c(mean_list, mean(complete_data))
    weight_list <- c(weight_list, length(complete_data))
  }
  
  weighted.mean(mean_list, weight_list)
  
}