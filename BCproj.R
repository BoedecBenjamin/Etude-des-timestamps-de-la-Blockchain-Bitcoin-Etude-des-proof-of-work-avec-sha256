require(vcd)
require(MASS)

library(anytime)

donneeBrute <- read.csv2("C:\\Users\\benja\\Desktop\\ESILV\\Cryptofinance\\timestamps5.csv",header = FALSE)
debut <- anytime(donneeBrute$V1[1])
fin <- anytime(donneeBrute$V1[length(donneeBrute$V1)])
donneeFiltre <- list()
for (i in seq(1,length(donneeBrute$V1) - 1))
{
  temp <- donneeBrute$V1[i+1] - donneeBrute$V1[i]
  if((temp >= 120) & (temp < 7200))
  {
    donneeFiltre <- c(donneeFiltre,temp)
  }
}

Dcrit<- 1.3581/sqrt(108616)

control <- abs(rexp(length(donneeFiltre)))
ks.test(unlist(donneeFiltre),control)

donnee <- unlist(donneeFiltre)




fit1 <- fitdistr(donnee, "exponential")
fit2 <- fitdistr(control, "exponential")

ks.test(donnee, "pexp", fit1$estimate)
ks.test(control, "pexp", fit2$estimate)

hist(donnee, freq = FALSE, breaks = 100)
curve(dexp(x,fit1$estimate), col = "blue", add = TRUE)

