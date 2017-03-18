library(twitteR)
library(wordcloud)
library(dplyr)
#install.packages("dplyr")
#install.packages("tm")
source("H:\\Rutilities\\twitterlogin.R")
setup()

#myTweets<-userTimeline("zerohedge", n=100)
#myTweets <- searchTwitteR("hillary",n=10000)
myTweets <- searchTwitteR("realdonaldtrump",n=1000)

tweetTexts<-unlist(lapply(myTweets, function(t) { t$text}))
SELLTweets <- tweetTexts[grep("SELL",tweetTexts,ignore.case=TRUE)]
BUYTweets <- tweetTexts[grep("BUY",tweetTexts,ignore.case=TRUE)]

set.seed(1234)
sellwords<-unlist(strsplit(SELLTweets, " "))
sellwords<-tolower(sellwords)
sell_words<-sellwords[-grep("http|@", sellwords)]
wordcloud(sell_words, min.freq=2)
buywords<-unlist(strsplit(BUYTweets, " "))
buywords<-tolower(buywords)
buy_words<-sellwords[-grep("http|@", buywords)]
wordcloud(buy_words, min.freq=2)
class(myTweets)
myTweets.filter()

BUYSELL <- function(x){
  if(is.null(x) || is.null(x$text))
    return(FALSE)
  print(length(x$text))
  if(length( grep("BUY|SELL",x$text , ignore.case = TRUE )  ))
    return(TRUE)
  else
    return(FALSE)
}
cond <- sapply(myTweets, function(x) BUYSELL(x) )
Filtered <- myTweets[cond]


#usefulTweets  <-  lapply(myTweets,BSTweet)
#tweets <- myTweets %>%
#  select(id, statusSource, text, created) %>%
#  extract(text, "text", "(.*?)<") %>%
#  filter(source %in% c("iPhone", "Android"))

myTweets

#myTweets[lapply(l, length) > 0]
#str(myTweets[[1]])
#set.seed(1234)
#tweetTexts<-unlist(lapply(myTweets, function(t) { t$text}))
#words<-unlist(strsplit(tweetTexts, " "))
words<-tolower(words)
#clean_words<-words[-grep("http|@", words)]
#wordcloud(clean_words, min.freq=2)