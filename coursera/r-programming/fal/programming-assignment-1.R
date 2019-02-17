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

# Write a function that takes a directory of data files 
# and a threshold for complete cases and calculates the 
# correlation between sulfate and nitrate for monitor 
# locations where the number of completely observed cases 
# (on all variables) is greater than the threshold. The 
# function should return a vector of correlations for the 
# monitors that meet the threshold requirement. If no 
# monitors meet the threshold requirement, then the function 
# should return a numeric vector of length 0. A prototype 
# of this function follows

corr <- function(directory, threshold = 0){
  i <- 1L
  correlations <- c()
  repeat{
    if(i < 10){
      i <- paste("00", i, sep = '')
    }
    else if(i < 100){
      i <- paste("0", i, sep = '')
    }
    
    file_location <- paste(directory, "/", i, ".csv", sep = '')
    
    if(file.exists(file_location)){
      all_data <- as.data.frame(read.csv(file_location))
      is_data_complete <- complete.cases(all_data)
      passed <- TRUE == (sum(is_data_complete) >= threshold)
      
      if(passed){
        nitrate_cor <- all_data[, "nitrate"]
        nitrate_cor <- nitrate_cor[is_data_complete]
        sulfate_cor <- all_data[, "sulfate"]
        sulfate_cor <- sulfate_cor[is_data_complete]
        correlations <- c(correlations, cor(nitrate_cor, sulfate_cor))
      }
      
    } else {
      break
    }
    
    i <- as.numeric(i) + 1
  }
  
  correlations
  
}

