# PriorityEngine Class
# Responsible for calculating task priority.

# Features:
# - calculate_score(task)
# - assign_label(score)

# Encapsulation:
# - uses internal attribute _emergency_weight

# Business Logic:
# - considers emergency flag
# - considers deadline proximity

# This class does NOT:
# - access database
# - handle HTTP request