possible_outcomes <- c("heart attack", "heart failure", "pneumonia")

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

show_ranked <- function(database, state, outcome, num){
  state_data <- database[, "state"] == state
  state_data <- database[state_data, ]
  data_to_order <- state_data[, c("hospital", outcome)]
  winner <- data_to_order[order(data_to_order[,2], data_to_order$hospital),]
  if(num == "worst"){num <- length(winner[,2]) - sum(winner[,2] == 1000)}
  if(num == "best"){num <- 1}
  winner <- data.frame(winner [num,])
  winner <- c(winner[,c("hospital")], state)
  return(winner)
}


rankall <- function(outcome, num = "best"){
  list_to_return <- c()
  database <- getdata()
  if( outcome %in% possible_outcomes){
  } else{
    stop("invalid outcome")
  }
  states <- unique(database[, "state"])
  states <- states[order(states)]
  for(i in states){
    list_to_return <- rbind(list_to_return, show_ranked(database, i, outcome, num))
  }
  list_to_return <- data.frame(list_to_return)
  colnames(list_to_return) <- c("hospital", "state")
  return(list_to_return)
}

