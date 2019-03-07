getdata <- function(){
  hospitals <- read.csv("rprog_data_ProgAssignment3-data/outcome-of-care-measures.csv", colClasses = "character")  
  hospitals <- data.frame(hospitals[,c(2, 7, 11, 17, 23)])
  
  fix_for_nas <- function(x){
    get_this <- x[, c(3, 4, 5)]
    change_this <- "Not Available" == get_this
    get_this[change_this] <- 1000
    put_this <- sapply(get_this, as.numeric)
    return(put_this)
  }
  
  hospitals[,3:5] <- fix_for_nas(hospitals)
  colnames(hospitals) <- c("hospital", "state", possible_outcomes)
  return(hospitals)
}


possible_outcomes <- c("heart attack", "heart failure", "pneumonia")

check_args <- function(x, state, outcome){
  if( state %in% x[,2]){
  } else{
    stop("invalid state")
  }
  if( outcome %in% possible_outcomes){
  } else{
    stop("invalid outcome")
  }
}

show_ranked <- function(database, state, outcome, num){
  state_data <- database[, "state"] == state
  state_data <- database[state_data, ]
  data_to_order <- state_data[, c("hospital", outcome)]
  winner <- data_to_order[order(data_to_order[,2], data_to_order$hospital),]
  if(num == "worst"){num <- length(winner[,2]) - sum(winner[,2] == 1000)}
  if(num == "best"){num <- 1}
  winner <- winner [num,]
  return(winner$hospital)
}

rankhospital <- function(state, outcome, num){
  database <- getdata()
  check_args(database, state, outcome)
  show_ranked(database, state, outcome, num)
}