# Logistics Data Analysis and Visualization

## Week 3 Task

This project demonstrates exploratory data analysis, statistical analysis, and visualization of a hypothetical logistics dataset using Python.

### Objectives
- Explore logistics delivery records.
- Calculate descriptive statistics and distributions.
- Analyze correlations and relationships.
- Compare delivery performance and shipping costs.
- Identify operational patterns, cost drivers, and possible bottlenecks.
- Develop data-driven logistics recommendations.

### Structure
```text
data/
  logistics_data.csv
src/
  data_analysis.py
  visualizations.py
README.md
requirements.txt
```

The dataset contains 300 hypothetical shipment records covering region, vehicle type, weather, traffic, priority, distance, shipment volume, delivery time, shipping cost, customer rating, and on-time status. A small number of missing values are intentionally included for analysis.

### Analysis
The Python scripts perform data-quality checks, missing-value handling, descriptive statistics, IQR-based outlier detection, group comparisons, and correlation analysis.

### Visualizations
The visualization script creates a delivery-time distribution, regional delivery-time comparison, vehicle-cost comparison, distance-versus-delivery-time scatter plot, and correlation heatmap.

### Run
```bash
pip install -r requirements.txt
python src/data_analysis.py
python src/visualizations.py
```
