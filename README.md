
# **YAML-Driven Data Pipeline (DPS)**

A modular, configurable, and dataset-agnostic data cleaning system controlled entirely through a YAML rules file.

This project demonstrates how to design a **mini data-pipeline** without hardcoding logic.
All cleaning steps—missing value handling, encoding, scaling, column dropping—are defined in `settings.yaml`.
The pipeline reads these rules and applies transformations dynamically.

---

## **📁 Project Structure**

```
yaml-driven-data-pipeline/
│
├── config/
│   └── settings.yaml          # Cleaning rules (YAML-driven)
│
├── data/
│   ├── raw/                   # Input CSV files
│   └── processed/             # Cleaned output files
│
├── artifacts/
│   └── explore_dataset.txt    # Dataset profile report
│
├── src/
│   ├── explore_dataset.py     # Utility to profile dataset
│   └── data_cleaner.py        # Main rule-based cleaning pipeline
│
├── requirements.txt
└── README.md
```

---

## **🚀 Features**

### ✔ **1. YAML-Based Rules (No Hardcoding)**

All pipeline logic is configured using:

```
config/settings.yaml
```

Allowing full flexibility without changing Python code.

### ✔ **2. Missing Value Handling**

Supports:

* `median`
* `mode`

### ✔ **3. Column Dropping**

Any unwanted columns can be removed through YAML.

### ✔ **4. Encoding**

Supports:

* **Label Encoding**
* **One-Hot Encoding**

### ✔ **5. Feature Scaling**

Supports:

* **StandardScaler**
* **MinMaxScaler**

### ✔ **6. Dataset Exploration**

The `explore_dataset.py` script automatically generates:

* Dataset shape
* Column data types
* Missing values
* Unique counts
* Numerical stats
* Categorical stats

Saved to:

```
artifacts/explore_dataset.txt
```

---

## **📝 Example YAML Configuration**

```yaml
missing_values:
  strategy:
    Age: median
    Embarked: mode

drop_columns:
  - Cabin
  - Ticket
  - Name

encoding:
  strategy:
    Sex: label
    Embarked: onehot
    Pclass: onehot

scaling:
  strategy:
    Fare: standard
    Age: standard

target_column: Survived

validation:
  drop_duplicates: true
  enforce_schema: false
```

---

## **⚙ How to Run the Pipeline**

### **1. Place your raw dataset**

```
data/raw/your_file.csv
```

### **2. Generate Dataset Exploration Report**

```bash
python src/explore_dataset.py
```

### **3. Run the Data Cleaning Pipeline**

```bash
python src/data_cleaner.py
```

### Output stored at:

```
data/processed/cleaned_<dataset>.csv
```

---

## **📦 Requirements**

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## **🎯 Purpose of the Project**

* To practice real-world data cleaning workflows
* To simulate how production ML pipelines use **config files instead of hardcoded logic**
* To prepare for ML engineer workflows involving:

  * Data validation
  * Feature engineering
  * Pipeline automation
  * Config-driven transformations

---

## **📌 Future Enhancements**

* Add schema validation
* Add logging system
* Add CLI interface
* Add train/validation split support
* Add support for custom transformations
* Add exportable transformation report

---

## **👤 Author**

**Abdul Rahman Shaikh**


