# Crystal Violet
cv_control <- c(0.021, 0.094, 0.048, 0.113, 0.036, 0.105, 0.061, 0.095, 0.131, 0.100)
cv_abs     <- c(0.024, 0.183, 0.058, 0.035, 0.114, 0.051, 0.031, 0.091, 0.146, 0.059)
cv_pla     <- c(0.039, 0.101, 0.068, 0.020, 0.024, 0.015, 0.067, 0.074, 0.069, 0.066)
cv_tpu     <- c(0.062, 0.143, 0.204, 0.135, 0.113, 0.067, 0.076, 0.100, 0.083, 0.113)

# Alamar Blue
ab_control <- c(0.070, 0.405, 0.138, 0.085, 0.104, 0.140, 0.089, 0.266, 0.269, 0.230)
ab_abs     <- c(0.070, 0.207, 0.095, 0.117, 0.056, 0.078, 0.000, 0.269, 0.256, 0.235)
ab_pla     <- c(0.073, 0.115, 0.102, 0.146, 0.058, 0.077, 0.246, 0.950, 0.239, NA)
ab_tpu     <- c(0.073, 0.154, 0.102, 0.267, 0.081, 0.090, 0.188, 0.274, 0.278, NA)

# Shapiro - Wilk Test
#Checking the normality of each group
shapiro.test(cv_control)
shapiro.test(cv_abs)
shapiro.test(cv_pla)
shapiro.test(cv_tpu)

shapiro.test(ab_control)
shapiro.test(ab_abs)
shapiro.test(ab_pla)
shapiro.test(ab_tpu)

# Levene Test
# Chech if variances are equal among normal data groups
install.packages("car")
library(car)

cv_values <- c(cv_control, cv_abs, cv_pla, cv_tpu)

cv_group <- factor(c(
  rep("Control", length(cv_control)),
  rep("ABS", length(cv_abs)),
  rep("PLA", length(cv_pla)),
  rep("TPU", length(cv_tpu))
))

cv_df <- data.frame(Group = cv_group, Absorbance = cv_values)

leveneTest(Absorbance ~ Group, data = cv_df)

# ANOVA test
# Check if means are different between any two groups
cv_anova <- aov(Absorbance ~ Group, data = cv_df)

summary(cv_anova)

# TuckeyHSD Test
# Check which groups specifically have different means
TukeyHSD(cv_anova)

# Krsukal-Willis
# Check if unequal variances or non normal data has different medians
ab_values <- c(ab_control, ab_abs, ab_pla, ab_tpu)

ab_group <- factor(c(
  rep("Control", length(ab_control)),
  rep("ABS", length(ab_abs)),
  rep("PLA", length(ab_pla)),
  rep("TPU", length(ab_tpu))
))

ab_df <- data.frame(Group = ab_group, Absorbance = ab_values)

kruskal.test(Absorbance ~ Group, data = ab_df)