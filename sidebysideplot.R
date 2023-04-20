library(ggplot2)

# Read data
data <- read.csv("counts.csv")

# Add row number column to data
data$row_num <- rep(1:6, each=4)

# Create plot with faceted subplots
ggplot(data = data, aes(x = Category, y = Count, fill = "row")) +
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
