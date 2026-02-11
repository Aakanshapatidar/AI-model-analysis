# AI-model-analysis
# AI Model Performance & Cost Analysis Dashboard

## Project Overview
This project focuses on analyzing and comparing the performance of various AI models based on
multiple parameters such as intelligence score, pricing, latency, and context window capacity.
The objective is to extract meaningful insights from the data and present them through a
clear, interactive, and visually appealing Power BI dashboard.

The project demonstrates an end-to-end data analytics workflow, including data cleaning using
Python and data visualization using Power BI.

---

## Project Objectives
- To clean and preprocess raw AI model performance data
- To analyze relationships between intelligence, price, latency, and context window
- To create an interactive and colorful dashboard for decision-making
- To present insights in a business-friendly and visual manner

---

## Tools & Technologies Used
- **Python** – for data cleaning and preprocessing
- **Pandas** – handling missing values, duplicates, and data transformation
- **Power BI** – dashboard creation and data visualization
- **CSV Dataset** – source data
- **GitHub** – project version control and sharing

---

## Dataset Description
The dataset contains information about different AI models with the following attributes:

- **Model**: Name of the AI model  
- **Intelligence Index**: Performance score of the model  
- **Price (USD per 1M Tokens)**: Cost associated with the model  
- **Context Window (K)**: Maximum number of tokens supported  
- **Latency (First Answer Chunk / s)**: Response time of the model  

---

## Data Cleaning & Preprocessing
Data cleaning was performed using Python and Pandas to ensure accuracy and consistency.

The following steps were applied:
- Checked and handled missing values
- Removed duplicate records
- Converted numerical columns to proper data types
- Standardized context window values into thousands (K)
- Filled missing Intelligence Index values using mean-based imputation
- Saved a cleaned dataset for visualization

This step ensured that the data was reliable and ready for analysis.

---

## Power BI Dashboard Description

### KPI Cards
- Average Intelligence Index  
- Average Price per 1M Tokens  
- Maximum Context Window  
- Total Number of AI Models  

<p style="font-size:12px;">
These KPIs provide a quick summary of overall dataset performance.
</p>
<p align="center">
  <img src="images/kpi.png" width="600">
</p>
---

### Bar Chart – Intelligence Index by Model
<p style="font-size:12px;">
Displays the average intelligence score for each AI model.
Helps identify high-performing models.
</p>

<p align="center">
  <img src="images/grap.png" width="600">
</p
---

### Column Chart – Price per 1M Tokens by Model
<p style="font-size:12px;">
Shows a cost comparison across different AI models.
Useful for identifying affordable and premium models.
</p>

<p align="center">
  <img src="images/bgraph.png" width="600">
</p
---

### Bar Chart – Context Window by Model
<p style="font-size:12px;">
Compares the maximum context window capacity of each model.
Highlights models suitable for long-context tasks.
</p>

<p align="center">
  <img src="images/bar.png" width="600">
</p
---

### Line Chart – Latency by Model
<p style="font-size:12px;">
Illustrates response time differences among models.
Lower latency indicates faster responses.
</p>

<p align="center">
  <img src="images/line.png" width="600">
</p
---

### Scatter Plot – Price vs Intelligence Index
<p style="font-size:12px;">
Demonstrates the relationship between model performance and cost.
Bubble size represents context window capacity.
</p>

<p align="center">
  <img src="images/boolune.png" width="600">
</p
---

### Donut Chart – Context Window Distribution
<p style="font-size:12px;">
Shows how AI models are distributed across different context window ranges.
</p>

<p align="center">
  <img src="images/dono.png" width="600">
</p
---

### Comparison Table
<p style="font-size:12px;">
Provides a detailed comparison of all AI models with conditional formatting
for easier interpretation.
</p>

<p align="center">
  <img src="images/table.png" width="600">
</p

---

## Dashboard Design Approach
- Dark premium background theme
- Colorful visuals for better readability
- Meaningful color coding for insights
- Designed to be LinkedIn and resume friendly

---

## Key Insights
- Higher intelligence AI models generally come at higher costs
- Some mid-range models offer a good balance between performance and price
- Larger context windows are associated with advanced models
- High intelligence does not always mean high latency

---

## Conclusion
The analysis of the AI model performance dataset reveals important insights into the trade-offs
between intelligence, cost, latency, and context window capacity.

While higher-performing models tend to be more expensive, some models provide a balanced
combination of strong performance, reasonable pricing, and acceptable latency. Models with
larger context windows are ideal for complex tasks but may not be necessary for all use cases.

Overall, there is no single best AI model for every scenario. The optimal choice depends on
specific business requirements and use cases.

<p align="center">
  <img src="images/Screenshot 2026-01-25 151850.png" width="600">
</p
---

## Project Files
- Cleaned dataset (CSV)
- Python data cleaning script
- Power BI dashboard file (.pbix)

---

## Author
**Aakansha Patidar**

---

## Acknowledgement
This project was created as part of a data analytics learning journey to gain
hands-on experience in real-world data analysis and visualization.



