import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_records(count):
    records_list = []

    for num in range(1, count + 1):
        marks = random.randint(0, 100)
        attendance=random.randint(0,100)
        assignment=random.randint(0,50)

        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        record=(num, marks, attendance, assignment, performance_index)
        records_list.append(record)

    return records_list

def group_learners(records):
   group_map={
       "At Risk":[],
        "Average":[],
        "Good":[],
        "Top Performer":[]
   }

   for entry in records:
       learner_id, marks, attendance, assignment, performance_index = entry

       if marks<40 or attendance<50:
           group_map["At Risk"].append(learner_id)
       elif 40<=marks<=70:
           group_map["Average"].append(learner_id)
       elif 71<=marks<=90:
           group_map["Good"].append(learner_id)
       elif marks>90 and attendance>80:
           group_map["Top Performer"].append(learner_id)

   return group_map

def compute_metrics(table):
    marks_array=table["marks"].values
    avg_marks=np.mean(marks_array)
    mid_marks=np.median(marks_array)
    var_value=sum((x-avg_marks)**2 for x in marks_array)/len(marks_array)
    deviation=math.sqrt(var_value)
    relation=np.corrcoef(table["marks"], table["attendance"])[0][1]
    min_val=np.min(marks_array)
    max_val=np.max(marks_array)
    table["normalized_marks"]=[(x-min_val)/(max_val-min_val) for x in marks_array]
    return avg_marks, mid_marks, var_value, deviation, relation,table

def evaluate_trends(table,deviation,group_map):
    observations=[]

    if deviation<15:
        observations.append("Consistent Performance ")
    
    low_attend_count=len(table[table["attendance"]<50])
    if low_attend_count>3:
        observations.append("Attendance Risk")
    
    if len(group_map["Top Performer"])>=2:
        observations.append("High Achievement")

    if deviation <15 and low_attend_count <=3:
        system_status="Stable Academic System"
    elif len(group_map["Top Performer"])>=2:
        system_status="Moderate Performance"
    else:
        system_status="Critical Attention Required"

    return observations, system_status

last_digit=int(input("Enter the last digit of your roll number: "))
total_students=last_digit if last_digit>0 else 10

students_records=create_records(total_students)
data_frame=pd.DataFrame(students_records, columns=["learner_id", "marks", "attendance", "assignment", "performance_index"])
grouped_learners=group_learners(students_records)
avg_marks, mid_marks, var_value, deviation, relation, data_frame=compute_metrics(data_frame)
result_tuple=(avg_marks, deviation, data_frame["marks"].max())
observations, system_status=evaluate_trends(data_frame, deviation, grouped_learners)

print("Students Table")
print(data_frame)
print("\nGrouped Learners:")
print(grouped_learners)
print("\nAnalysis Report")
print(f"mean:{avg_marks}")
print(f"median:{mid_marks}")
print(f"deviation:{deviation}")
print(f"correlation:{relation}")
print("\nTuple Result")
print(result_tuple)
print("\nObservations")
print(observations)
print("\nFinal Status")
print(system_status)

plt.hist(data_frame["marks"],bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()