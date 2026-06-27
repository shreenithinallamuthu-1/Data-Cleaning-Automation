# Data Cleaning Automation


##  Internship Details

| Field | Details |
|-------|---------|
| **Intern ID** | CITS2445 |
| **Full Name** | Shreenithi Nallamuthu |
| **No. of Weeks** | 4 Weeks |
| **Project Name** | Data Cleaning Automation |
| **Project Scope** | A Project Scope document for data cleaning automation explicitly defines the boundaries, deliverables, and requirements of the script or pipeline you are building. It ensures you focus on core data quality issues without succumbing to scope creep. |

---



##  Features

- Collects user information through terminal input.
- Saves raw data into a CSV file.
- Automatically injects a duplicate record for testing.
- Cleans missing and empty values.
- Standardizes names, cities, and email formatting.
- Validates and cleans numeric age values.
- Replaces invalid ages with the dataset median (or default value).
- Removes duplicate records.
- Saves the cleaned dataset into a new CSV file.
- Displays the cleaned dataset in the terminal.

---

##  Technologies Used

- Python 3.x
- Pandas
- OS Module

---

##  Project Structure

```
.
├── main.py
├── data_cleaning_automation.csv   # Generated raw dataset
├── cleaned_user_data.csv          # Generated cleaned dataset
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/automated-data-cleaning.git
```

### 2. Navigate to the project directory

```bash
cd automated-data-cleaning
```

### 3. Install dependencies

```bash
pip install pandas
```

---

##  How to Run

Execute the Python script:

```bash
python main.py
```

The program will ask you to enter details for **3 users**.

Example:

```
Enter Name: john doe
Enter Age: 22
Enter Email: JOHN@GMAIL.COM
Enter City: new york
```

You can intentionally leave fields blank or enter invalid values to test the cleaning process.

---

##  Data Cleaning Process

The automation performs the following steps:

### 1. Handles Missing Values

- Empty Name → `Unknown`
- Empty Email → `Not Provided`
- Empty City → `Unknown`

---

### 2. Standardizes Text

Before:

```
john doe
new york
JOHN@GMAIL.COM
```

After:

```
John Doe
New York
john@gmail.com
```

---

### 3. Validates Age

- Converts Age to numeric.
- Invalid values become missing.
- Missing ages are replaced with:
  - Dataset median age
  - Default value **30** if every age is invalid.

Example:

| Input | Output |
|--------|--------|
| twenty | 30 |
| "" | 25 (median) |
| 22 | 22 |

---

### 4. Removes Duplicate Records

Automatically detects and removes identical rows.

---

##  Example

### Raw Data

| Name | Age | Email | City |
|------|----|------|------|
| john doe | 22 | JOHN@MAIL.COM | new york |
| | abc | | london |
| Alice | 25 | alice@mail.com | Chennai |
| Alice | 25 | alice@mail.com | Chennai |

---

### Cleaned Data

| Name | Age | Email | City |
|------|----|------|------|
| John Doe | 22 | john@mail.com | New York |
| Unknown | 23 | Not Provided | London |
| Alice | 25 | alice@mail.com | Chennai |

---

##  Output Files

### `data_cleaning_automation.csv`

Contains the raw user-entered data along with an automatically added duplicate record.

### `cleaned_user_data.csv`

Contains the cleaned and processed dataset after all transformations.

---

##  Workflow

```
User Input
     │
     ▼
Save Raw CSV
     │
     ▼
Load CSV
     │
     ▼
Replace Missing Values
     │
     ▼
Standardize Text
     │
     ▼
Validate Age
     │
     ▼
Remove Duplicates
     │
     ▼
Save Cleaned CSV
```

---

##  Learning Objectives

This project demonstrates:

- Data collection using Python
- Reading and writing CSV files
- Data cleaning with Pandas
- Missing value handling
- Data validation
- Duplicate removal
- Data preprocessing automation

---

##  Future Improvements

- Email format validation
- Phone number validation
- Export to Excel format
- Graphical User Interface (GUI)
- Database integration (MySQL/SQLite)
- Logging system
- Data visualization dashboard

---

##  Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

