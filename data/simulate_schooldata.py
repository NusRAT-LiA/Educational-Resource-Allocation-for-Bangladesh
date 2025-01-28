import pandas as pd
import random
import numpy as np

# Define number of schools
num_schools = 100

# Define divisions, districts, and upazilas
bangladesh_divisions = ["Dhaka", "Chattogram", "Khulna", "Rajshahi", "Barishal", "Sylhet", "Rangpur", "Mymensingh"]
bangladesh_districts = {
    "Dhaka": ["Dhaka", "Narayanganj", "Gazipur", "Manikgonj", "Munshigonj", "Narsingdi", "Tangail", "Kishorgonj", "Faridpur", "Gopalgonj", "Madaripur", "Rajbari", "Shariatpur"],
    "Chattogram": ["Chattogram", "Cox's Bazar", "Rangamati", "Bandarban", "Khagrachhari", "Feni", "Lakshmipur", "Comilla", "Noakhali", "Brahmanbaria", "Chandpur"],
    "Khulna": ["Khulna", "Bagherhat", "Sathkhira", "Jessore", "Magura", "Jhenaidah", "Narail", "Kushtia", "Chuadanga", "Meherpur"],
    "Rajshahi": ["Natore", "Rajshahi", "Sirajganj", "Pabna", "Bogura", "Chapainawabganj", "Naogaon", "Joypurhat"],
    "Barishal": ["Barishal", "Patuakhali", "Bhola", "Pirojpur", "Barguna", "Jhalokati"],
    "Sylhet": ["Habiganj", "Moulvibazar", "Sunamganj", "Sylhet"],
    "Rangpur": ["Rangpur", "Gaibandha", "Nilphamari", "Kurigram", "Lalmonirhat", "Dinajpur", "Thakurgaon", "Panchagarh"],
    "Mymensingh": ["Mymensingh", "Netrakona", "Jamalpur", "Sherpur"]
}

for _ in range(num_schools):
        region = np.random.choice(regions)
        urban_rural = np.random.choice([0, 1], p=[0.7, 0.3])  # 70% rural
        flood_prone = np.random.choice([0, 1], p=[0.6, 0.4]) if urban_rural else np.random.choice([0, 1], p=[0.3, 0.7])

# Parameters for distributions
budget_mean = 25000000  # Adjusted to a typical school budget
budget_std = 10000000  # Log-normal scale for more realistic variation
pass_rate_mean = 98.51  # Based on the pass rate of 98.51% (ResearchGate, 2016-2021 Report)
pass_rate_std = 1  # Small standard deviation to reflect the slight variance in pass rates
dropout_rate_mean = 37.81  # Mean dropout rate (Youth Policy Forum, 2017 Report)
dropout_rate_std = 5  # Some variation
students_mean = 500  # Based on the average number of students per secondary school (BANBEIS, Bangladesh Education Statistics 2021)
students_std = 50  # Adjusted to reflect variation in school size
student_teacher_ratio_mean = 44.73  # Reported student-teacher ratio (Youth Policy Forum, 2017 Report)
student_teacher_ratio_std = 5  # Some variation

# References for data
# references = {
#     "Average Number of Students per School": "BANBEIS, Bangladesh Education Statistics 2021",
#     "Dropout Rate": "Youth Policy Forum, 2017 Report",
#     "Pass Rate": "ResearchGate, 2016-2021 Report",
#     "Education Budget Allocation": "Centre for Policy Dialogue (CPD), FY 2025 Education Budget",
#     "Student-Teacher Ratio": "Youth Policy Forum, 2017 Report"
# }

# Initialize data structure
data = {
    "Region": [],
    "School_Name": [],
    "School_Type": [],
    "Education_Level": [],
    "Num_Students": [],
    "Gender_Ratio": [],
    "Num_Teachers": [],
    "Student_Teacher_Ratio": [],
    "Num_Disabled_Students": [],
    "Num_Classrooms": [],
    "Num_Labs": [],
    "Num_Toilets": [],
    "Drinking_Water_Access": [],
    "Electricity_Access": [],
    "Internet_Access": [],
    "Digital_Devices": [],
    "Num_Textbooks_Distributed": [],
    "Digital_Content_Access": [],
    "Library_Facilities": [],
    "Num_Library_Books": [],
    "Pass_Rate": [],
    "Dropout_Rate": [],
    "Average_Test_Scores": [],
    "Enrollment_Rate": [],
    "Poverty_Rate": [],
    "Midday_Meal_Program": [],
    "Scholarships_Provided": [],
    "Population_Density": [],
    "Urban_Rural": [],
    "Road_Accessibility": [],
    "Flood_Prone_Area": [],
    "Cyclone_Prone_Area": [],
    "Extracurricular_Activities": [],
    "Parent_Teacher_Association": [],
    "Community_Contribution": [],
    "References": [],  # Add reference column
}

# Generate data
for _ in range(num_schools):
    division = random.choice(bangladesh_divisions)
    district = random.choice(bangladesh_districts[division])
    school_name = f"School_{random.randint(1, 1000)}"
    school_type = random.choice(["Public", "Private", "Madrasa", "NGO-run", "Community"])
    education_level = random.choice(["Primary", "Secondary", "Higher Secondary"])
    
    # Generate realistic number of students based on the mean and std deviation
    num_students = max(50, int(np.random.normal(students_mean, students_std)))  # (BANBEIS, Bangladesh Education Statistics 2021)
    
    # Gender ratio (simulating slightly more balanced or higher female enrollment)
    gender_ratio = round(random.uniform(45, 55), 2)
    
    # Calculate the number of teachers based on the student-teacher ratio
    num_teachers = max(5, int(np.random.normal(num_students / student_teacher_ratio_mean, student_teacher_ratio_std)))  # (Youth Policy Forum, 2017 Report)
    
    # Calculate the student-teacher ratio
    student_teacher_ratio = round(num_students / num_teachers, 2)
    
    # Disabled students (simulate 5% of total students)
    num_disabled_students = random.randint(0, int(num_students * 0.05))
    
    # Infrastructure data (classrooms, labs, toilets, etc.)
    num_classrooms = random.randint(5, 30)
    num_labs = random.randint(0, 5)
    num_toilets = random.randint(2, 20)
    drinking_water_access = random.choice([0, 1])
    electricity_access = random.choice([0, 1])
    internet_access = random.choice([0, 1])
    digital_devices = random.randint(0, 50)
    
    # Textbook distribution and digital content
    num_textbooks_distributed = num_students * random.randint(1, 3)
    digital_content_access = random.choice([0, 1])
    library_facilities = random.choice([0, 1])
    num_library_books = random.randint(0, 5000)
    
    # Pass rate, dropout rate, and average test scores based on distributions
    pass_rate = max(0, min(100, np.random.normal(pass_rate_mean, pass_rate_std)))  # (ResearchGate, 2016-2021 Report)
    dropout_rate = max(0, np.random.normal(dropout_rate_mean, dropout_rate_std))  # (Youth Policy Forum, 2017 Report)
    average_test_scores = max(0, min(100, pass_rate + random.uniform(-10, 10)))
    enrollment_rate = max(50, min(100, pass_rate + random.uniform(-5, 5)))
    
    # Poverty rate (simulate about 30% from low-income families)
    poverty_rate = max(0, min(100, np.random.normal(30, 10)))
    
    # Midday meal program and scholarships
    midday_meal_program = random.choice([0, 1])
    scholarships_provided = random.randint(0, num_students // 10)
    
    # Regional data
    population_density = random.randint(100, 1500)
    urban_rural = random.choice([0, 1])
    road_accessibility = round(random.uniform(0, 20), 2)
    flood_prone_area = random.choice([0, 1])
    cyclone_prone_area = random.choice([0, 1])
    
    # Extracurricular activities and community contributions
    extracurricular_activities = random.choice([0, 1])
    parent_teacher_association = random.choice([0, 1])
    community_contribution = random.randint(0, 1000000)

    # Add references for each school
    reference = random.choice(list(references.values()))

    # Append generated data
    data["Region"].append(f"{district}, {division}")
    data["School_Name"].append(school_name)
    data["School_Type"].append(school_type)
    data["Education_Level"].append(education_level)
    data["Num_Students"].append(num_students)
    data["Gender_Ratio"].append(gender_ratio)
    data["Num_Teachers"].append(num_teachers)
    data["Student_Teacher_Ratio"].append(student_teacher_ratio)
    data["Num_Disabled_Students"].append(num_disabled_students)
    data["Num_Classrooms"].append(num_classrooms)
    data["Num_Labs"].append(num_labs)
    data["Num_Toilets"].append(num_toilets)
    data["Drinking_Water_Access"].append(drinking_water_access)
    data["Electricity_Access"].append(electricity_access)
    data["Internet_Access"].append(internet_access)
    data["Digital_Devices"].append(digital_devices)
    data["Num_Textbooks_Distributed"].append(num_textbooks_distributed)
    data["Digital_Content_Access"].append(digital_content_access)
    data["Library_Facilities"].append(library_facilities)
    data["Num_Library_Books"].append(num_library_books)
    data["Pass_Rate"].append(pass_rate)
    data["Dropout_Rate"].append(dropout_rate)
    data["Average_Test_Scores"].append(average_test_scores)
    data["Enrollment_Rate"].append(enrollment_rate)
    data["Poverty_Rate"].append(poverty_rate)
    data["Midday_Meal_Program"].append(midday_meal_program)
    data["Scholarships_Provided"].append(scholarships_provided)
    data["Population_Density"].append(population_density)
    data["Urban_Rural"].append(urban_rural)
    data["Road_Accessibility"].append(road_accessibility)
    data["Flood_Prone_Area"].append(flood_prone_area)
    data["Cyclone_Prone_Area"].append(cyclone_prone_area)
    data["Extracurricular_Activities"].append(extracurricular_activities)
    data["Parent_Teacher_Association"].append(parent_teacher_association)
    data["Community_Contribution"].append(community_contribution)
    data["References"].append(reference)

# Convert the data dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
df.head()
