# 🍕 Dominos Delivery Time Analysis (Case Study)   

## 📌 Project Overview      
This project analyzes delivery time performance of a Dominos store to evaluate whether it meets the company’s Service Level Agreement (SLA).    

Dominos measures store performance using the **95th percentile of delivery time**, which must be **less than 31 minutes**.            
If orders exceed 31 minutes, the pizza is given **free**, causing revenue loss.      

In this project, I analyze order data, calculate delivery times, evaluate SLA compliance, identify problem hours, and provide actionable business insights.       

---

## 🎯 Problem Statement      
Kanav owns a Dominos franchise. Dominos has informed him that:         
- The **95th percentile of delivery time must be < 31 minutes**          
- Failure to meet this metric may result in losing the franchise            

The goal is to analyze historical order data and help Kanav understand:            
- Whether the store meets the SLA     
- How much revenue is being lost      
- Which hours cause the most delays       
- What actions should be taken        

---

## 📂 Dataset    
- **File Name:** `diminos_data.csv`   
- **Columns Used:**      
  - `order_id`        
  - `order_placed_at`        
  - `order_delivered_at`           

Delivery time is **not directly available** and is calculated during analysis.

---

## 🧠 Approach & Methodology

### 1️⃣ Data Loading & Cleaning       
- Loaded CSV data using Pandas             
- Converted timestamp columns to datetime format            
- Removed invalid delivery times             

### 2️⃣ Feature Engineering      
- Calculated delivery time (in minutes) using:         

  delivery_time = order_delivered_at - order_placed_at

- Extracted order hour for peak-hour analysis      

### 3️⃣ Key Metrics Calculated         
- **95th percentile delivery time**         
- Number and percentage of late deliveries (> 31 minutes)         
- Hour-wise 95th percentile performance         

### 4️⃣ Business Analysis           
- Identified peak hours causing SLA violations        
- Estimated revenue leakage due to free pizzas        
- Provided operational recommendations         

---

## 📊 Key Insights         
- The 95th percentile delivery time indicates whether the store meets SLA          
- A small number of extreme delays significantly affect performance           
- Certain hours consistently violate the 31-minute threshold         
- Late deliveries directly contribute to revenue loss          

---

## 🛠️ Recommendations        
- Increase delivery staff during peak hours          
- Optimize delivery routes and zones             
- Monitor and reduce extreme delivery delays            
- Improve operational readiness during high-demand periods             

---

## 🏁 Conclusion          
This analysis helps determine whether the store is compliant with Dominos SLA requirements.           
By addressing peak-hour delays and reducing extreme outliers, the store can improve delivery performance, reduce revenue loss, and protect its franchise.         

---

## 🧑‍💻 Technologies Used       
- Python       
- Pandas         
- NumPy         
- Google Colab / Jupyter Notebook          

---

## 📁 Repository Structure
├── diminos_data.csv  
├── Diminos Case Study.ipynb      
├── README.md        

---

## ✍️ Author
**Gunasekhar**
