library(ggplot2)
library(gridExtra)

# read the CSV file
data <- read.csv("linear_regression.csv", header = TRUE)

# drop NA values
data <- na.omit(data)

# create a grid of plots
grid <- grid.arrange(
  ggplot(data, aes(x=techScore, y=complexScore)) + 
    geom_point(aes(color=race)) + 
    geom_smooth(method = "lm", color = "darkgreen") +
    labs(title="Techscore vs. ComplexScore", 
         x="Techscore", y="ComplexScore"),
  
  ggplot(data, aes(x=techScore, y=health_literacy_score)) + 
    geom_point(aes(color=race)) + 
    geom_smooth(method = "lm", color = "darkgreen") +
    labs(title="Techscore vs. Health Literacy Score", 
         x="Techscore", y="Health Literacy Score"),
  
  ggplot(data, aes(x=techScore, y=age)) + 
    geom_point(aes(color=race)) + 
    geom_smooth(method = "lm", color = "darkgreen") +
    labs(title="Techscore vs. Age", 
         x="Techscore", y="Age"),
  
  ncol=3, nrow=1, widths=c(5,5,5)
)

# save the plot as PNG file
ggsave("bivariate_analysis.png", grid, width=15, height=5)

