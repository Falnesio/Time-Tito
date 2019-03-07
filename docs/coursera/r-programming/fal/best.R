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

lowest_in_state <- function(database, state, outcome){
  state_data <- database[, "state"] == state
  state_data <- database[state_data, ]
  lowest <- min(state_data[, outcome])
  candidates <- state_data[, outcome] == lowest
  candidates <- state_data[candidates, ]
  winner <- candidates[order(candidates$hospital)]
  return(winner[[1]])
}

best <- function(state, outcome){
  database <- getdata()
  check_args(database, state, outcome)
  lowest_in_state(database, state, outcome)
}
