library(party)

data <- read.csv(file="D:/data_plus_clust.csv", header=TRUE, sep=";")
data <- data[,c('control.','answer','matrix_clust10_class','matrix_clust20_class',
                 'embedded_clust10_class','embedded_clust20_class')]
colnames(data) <- c('c','answer','m10','m20','e10','e20')
data[,'m10']<- as.factor(data[,'m10'])
data[,'m20']<- as.factor(data[,'m20'])
data[,'e10']<- as.factor(data[,'e10'])
data[,'e20']<- as.factor(data[,'e20'])
data[,'c']<- as.factor(data[,'c'])

endeavour <- glm(answer ~ m20+e10,data,family='binomial' )
summary(endeavour)
logit_pred = predict(endeavour,type='response')

t <- ctree(answer ~ m20+e10,data=data)
plot(t)
tree_pred = predict(t,type='response')

dd = data.frame(logit_pred,tree_pred,data[,'answer'])
write.csv(dd,'D:/predictions.csv')
