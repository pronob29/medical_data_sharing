library(ggplot2)

# Read data
data <- # Read data
  data <- read.csv("side_by_side.csv")

# Add row number column to data
data$row_num <- rep(1:6, each=4)

# Define the desired order of categories
ordered_categories <- c("Very Comfortable", "Comfortable", "Neutral", "Uncomfortable", "Very Uncomfortable")

# Create a new column with the ordered factor
data$Category <- factor(data$Category, levels = ordered_categories)

# Create plot with faceted subplots
myplot <- ggplot(data = data, aes(x = Category, y = Count, fill = "row")) +
  geom_bar(stat = "identity", alpha = 0.7) +
  facet_wrap(~Variable, ncol = 4) +
  scale_fill_manual(values = "#4b6aa4") +
  ylim(0, 250) +
  labs(x = "\n Trust in Mechanisms for Clinical Data Access and Use", y = "Frequency\n", fill = "") +
  theme(plot.title = element_text(),
        axis.title.x = element_text(face = "bold", colour = "darkgreen", size = 12),
        axis.title.y = element_text(face = "bold", colour = "darkgreen", size = 12),
        strip.text.x = element_blank(),
        axis.text.x = element_text(angle = 45, hjust = 1)) +
  guides(fill = FALSE)

myplot
# save the plot as PNG file
ggsave("side_by_side.png", myplot, width=10, height=10)
