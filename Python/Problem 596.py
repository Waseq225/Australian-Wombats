import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby('class').size().reset_index(name='count')
    filtered_classes = class_counts[class_counts['count'] >= 5]
    return filtered_classes.drop(['count'], axis = 1)
