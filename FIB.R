#!/usr/bin/env Rscript

library(argparse)
# create parser object
parser <- ArgumentParser()

parser$add_argument("-n", type="integer", 
    help="Number of rabbits after n months",
    metavar="number")
parser$add_argument("-k", type="integer",
    help="Every pair of reproduction age rabbits produces a litter of size k.",
    metavar="number")

args <- parser$parse_args()

wascallywabbits <- function(n,  k){

	options(scipen = 999)

	len <- n
	fibvals <- numeric(len)
	fibvals[1] <- 1
	fibvals[2] <- 1
		for (i in 3:len) { 
   			fibvals[i] <- fibvals[i-1] + fibvals[i-2]*k
	} 

	return(fibvals[args$n])


}

wascallywabbits(args$n, args$k)



