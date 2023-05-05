library(ggplot2)
library(gridExtra)

# read the CSV file
data <- read.csv("linear_regression.csv", header = TRUE)

# drop NA values
data <- na.omit(data)

# create a grid of plots
grid <- grid.arrange(
  ggplot(data, aes(x=techScore, y=complexScore)) + 
    geom_point() + 
    geom_smooth(method = "lm", color = "darkgreen") +
    labs(title="Techscore vs. ComplexScore", 
         x="Techscore", y="ComplexScore"),
  
  ggplot(data, aes(x=techScore, y=health_literacy_score)) + 
    geom_point() + 
    geom_smooth(method = "lm", color = "darkgreen") +
    labs(title="Techscore vs. Health Literacy Score", 
         x="Techscore", y="Health Literacy Score"),
  
  ggplot(data, aes(x=techScore, y=age)) + 
    geom_point() + 
    geom_smooth(method = "lm", color = "darkgreen") +
    labs(title="Techscore vs. Age", 
         x="Techscore", y="Age"),
  
  ggplot(data, aes(x=techScore, y=race)) + 
    geom_point() + 
    labs(title="Techscore vs. Race", 
         x="Techscore", y="Race"),
  
  ncol=2, nrow=2, widths=c(5,5)
)

# save the plot as PNG file
ggsave("bivariate_analysis.png", grid, width=10, height=10)
