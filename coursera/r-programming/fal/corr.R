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
