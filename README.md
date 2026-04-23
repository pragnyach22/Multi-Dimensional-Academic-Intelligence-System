# Multi-Dimensional-Academic-Intelligence-System
Overview

The present project is an analysis of academic performances of the students based on various criteria like marks, attendance, and assignments.
The project uses various python libraries like numpy and pandas for statistical analysis and pattern detection.

Objective
Construction of a system that:

Generates student data
Classifies the students depending upon their performance
Does statistical analysis
Detects academic performance pattern
Draws conclusions from the final system

Technology Used
Python
Numpy
Pandas
Matplotlib
Math Library
Random Library

Data Structure
Student data comprises of
(Student ID, Marks, Attendance, Assignment, Performance Index)

Features
Data Generation
Generation of data for each student using the random library
Marks → range (0-100)
Attendance → range (0-100)
Assignment → range (0-50)
Performance index
performance index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)

✔ Academic performance along with attendance is taken into account
✔ Log function restricts the effect of attendance on performance

Classification
Criteria → Category
marks < 40 or attendance < 50	At Risk
40 to 70	average
71 to 90	good
marks > 90 and attendance > 80	Top Performer

Statistical Analysis
Mean (numpy)
Median (numpy)
Standard deviation (manual calculation)
correlation between marks and attendance

Normalization
normalized = (x – min)/ (max-min)

Pattern Detection
Consistency → std deviation < 15
Attendance at risk → 3+ students have attendance < 50%
Academic success → Top performers ≥ 2

📊 Output

The program shows:

Student DataFrame
Categorized Dictionary
Statistics Summary
Tuple → (mean, std_dev, max_marks)
Insight from system finally:
Stable Academic System
Moderate Performance
Attention is Necessary
▶️ How to Execute the Program
Required packages installation:
pip install numpy pandas matplotlib
Execute the program:
python your_file_name.py
Input the last digit of your roll number when asked.
📈 Sample Output
Mean = 67.4
Median = 70
Standard Deviation = 18.2
Correlation = 0.63

Tuple = (67.4, 18.2, 92)

Performance status finally = Moderate Performance
🎓 Outcome of Learning
Acquired skills of using NumPy and Pandas for data analysis
Got to know about data structures like lists, tuples, dictionaries
Classifying and Normalizing
Doing statistics manually
Knowledge about data analysis systems

