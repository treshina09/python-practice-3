import os
import csv
import json


# ============================================================
# PRACTICE 6 — OOP Classes
# ============================================================

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        sorted_students = sorted(
            self.students,
            key=lambda x: float(x['final_exam_score']),
            reverse=True
        )
        top10 = sorted_students[:10]

        top10_list = []
        for i in range(len(top10)):
            s = top10[i]
            try:
                top10_list.append({
                    "rank": i + 1,
                    "student_id": s['student_id'],
                    "country": s['country'],
                    "major": s['major'],
                    "final_exam_score": float(s['final_exam_score']),
                    "GPA": float(s['GPA'])
                })
            except ValueError:
                print(f"Warning: could not convert value for student {s['student_id']} — skipping row.")
                continue

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top10_list
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)
        for s in self.result['top_10']:
            print(f"{s['rank']}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


# ============================================================
# PRACTICE 5 — Functions
# ============================================================

def check_files():
    print("Checking file...")
    if os.path.exists('students.csv'):
        print("File found: students.csv")
    else:
        print("Error: students.csv not found.")
        return False
    print("Checking output folder...")
    if os.path.exists('output'):
        print("Output folder already exists: output/")
    else:
        os.makedirs('output')
        print("Output folder created: output/")
    return True


def load_data(filename):
    print("Loading data...")
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            students = list(reader)
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def preview_data(students, n=5):
    print(f"First {n} rows:")
    print("-" * 30)
    for row in students[:n]:
        print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
    print("-" * 30)


def get_top_students(students, n=10):
    sorted_students = sorted(
        students,
        key=lambda x: float(x['final_exam_score']),
        reverse=True
    )
    return sorted_students[:n]


# ============================================================
# MAIN — runs all three practices in sequence
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # PRACTICE 4 — Files and Data Formats
    # --------------------------------------------------------
    print("=" * 30)
    print("PRACTICE 4")
    print("=" * 30)

    # Task 1 — OS module
    print("Checking file...")
    if not os.path.exists('students.csv'):
        print("Error: students.csv not found. Please download the file from LMS.")
        exit()
    print("File found: students.csv")
    print("Checking output folder...")
    if os.path.exists('output'):
        print("Output folder already exists: output/")
    else:
        os.makedirs('output')
        print("Output folder created: output/")

    # Task 2 — Read CSV and preview
    with open('students.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        students = list(reader)

    print(f"Total students: {len(students)}")
    print("First 5 rows:")
    print("-" * 30)
    for row in students[:5]:
        print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
    print("-" * 30)

    # Task 3 — Top 10 Students by Exam Score
    top10 = sorted(students, key=lambda x: float(x['final_exam_score']), reverse=True)[:10]
    print("-" * 30)
    print("Top 10 Students by Exam Score")
    print("-" * 30)
    for i in range(len(top10)):
        s = top10[i]
        print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {float(s['final_exam_score'])} | GPA: {float(s['GPA'])}")
    print("-" * 30)

    # Task 4 — Save to JSON
    result_p4 = {
        "analysis": "Top 10 Students by Exam Score",
        "total_students": len(students),
        "top_10": [
            {
                "rank": i + 1,
                "student_id": top10[i]['student_id'],
                "country": top10[i]['country'],
                "major": top10[i]['major'],
                "final_exam_score": float(top10[i]['final_exam_score']),
                "GPA": float(top10[i]['GPA'])
            }
            for i in range(len(top10))
        ]
    }
    print("=" * 30)
    print("ANALYSIS RESULT")
    print("=" * 30)
    print(f"Analysis        : Top 10 Students by Exam Score")
    print(f"Total students  : {len(students)}")
    print("Top 10 saved to output/result.json")
    print("=" * 30)
    with open('output/result.json', 'w', encoding='utf-8') as f:
        json.dump(result_p4, f, indent=4)
    print("Result saved to output/result.json")

    # --------------------------------------------------------
    # PRACTICE 5 — Functions and Advanced Concepts
    # --------------------------------------------------------
    print()
    print("=" * 30)
    print("PRACTICE 5")
    print("=" * 30)

    # Task 1 — Basic Functions
    check_files()
    students = load_data('students.csv')
    preview_data(students)

    # Task 2 — Analysis Function
    top10_result = get_top_students(students)
    print("-" * 30)
    print("Top 10 Students by Exam Score")
    print("-" * 30)
    for i in range(len(top10_result)):
        s = top10_result[i]
        print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {float(s['final_exam_score'])} | GPA: {float(s['GPA'])}")
    print("-" * 30)

    top5_result = get_top_students(students, 5)
    print("-" * 30)
    print("Top 5 Students by Exam Score")
    print("-" * 30)
    for i in range(len(top5_result)):
        s = top5_result[i]
        print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {float(s['final_exam_score'])} | GPA: {float(s['GPA'])}")
    print("-" * 30)

    # Task 3 — Lambda / Map / Filter
    top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, students))
    gpa_values = list(map(lambda s: float(s['GPA']), students))
    good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, students))

    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)
    print(f"Students with score > 95 : {len(top_scorers)}")
    print(f"GPA values (first 5)     : {gpa_values[:5]}")
    print(f"Students assignment > 90 : {len(good_assignments)}")
    print("-" * 30)

    # Task 4 — Exception Handling test
    load_data('students.csv')
    load_data('wrong_file.csv')

    # --------------------------------------------------------
    # PRACTICE 6 — OOP
    # --------------------------------------------------------
    print()
    print("=" * 30)
    print("PRACTICE 6")
    print("=" * 30)

    fm = FileManager('students.csv')
    if not fm.check_file():
        print("Stopping program.")
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()