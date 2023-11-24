import pandas as pd
data = {
    'Student_ID': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    'Course': ['Math', 'English', 'Math', 'Physics', 'English', 'Physics', 'Math', 'English', 'Physics', 'Math'],
    'Score': (80, 85, 90, 75, 88, 92, 78, 80, 94, 85),
    'Hours_Studied': (10, 12, 15, 8, 14, 18, 9, 11, 20, 13)
}

student_data = pd.DataFrame(data)
correlation_per_course = student_data.groupby('Course')[['Hours_Studied', 'Score']].corr().iloc[-1]
strongest_corr_course = correlation_per_course.idxmax()
weakest_corr_course = correlation_per_course.idxmin()
average_data_per_course = student_data.groupby('Course').agg({'Score': 'mean', 'Hours_Studied': 'mean'}).reset_index()
print("Correlation coefficient between 'Hours_Studied' and 'Score' for each course:")
print(correlation_per_course)

print("\nCourse with the strongest correlation: ", strongest_corr_course[0])
print("Course with the weakest correlation: ", weakest_corr_course[0])

print("\nAggregated data - Average score and average hours studied for each course:")
print(average_data_per_course)

