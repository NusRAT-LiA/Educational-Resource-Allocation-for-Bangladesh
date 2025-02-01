import os
import random
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

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

def generate_education_data(num_institutions=1000, start_year=2010, end_year=2021):
    fake = Faker()
    np.random.seed(42)

    # ====== Institutional Base Data ======
    institutions = []
    for _ in range(num_institutions):
        inst_type = np.random.choice(
            ['Secondary School', 'College', 'Madrasah'],
            p=[0.65, 0.25, 0.10]
        )
        division = np.random.choice(bangladesh_divisions)
        
        institution = {
            'EIIN': fake.unique.bothify("#######"),
            'Institution_Name': f"Ins_{random.randint(1, 1000)}" + (" School" if inst_type == 'Secondary School' else 
                                                " College" if inst_type == 'College' else " Madrasah"),
            'Institution_Type': inst_type,
            'Management': np.random.choice(['Public', 'Private'], p=[0.15, 0.85]),
            'Establishment_Year': np.random.randint(1950, 2020),
            'Division': division,
            'District' : np.random.choice(bangladesh_districts[division]),
            
            # Madrasah Specific
            'Madrasah_Type': np.random.choice(['Dakhil', 'Alim', 'Fazil', 'Kamil'], p=[0.7, 0.15, 0.1, 0.05]) if inst_type == 'Madrasah' else None,
            
            # College Specific
            'College_Type': np.random.choice([
                'School and College', 'Higher Secondary', 
                'Degree (Pass)', 'Degree (Honors)', 'Masters'
            ], p=[0.3, 0.25, 0.2, 0.15, 0.1]) if inst_type == 'College' else None,
            
            # Initial Quality Indicators (2010 baseline)
            'Computer_Facility_2010': np.random.choice([0,1], p=[0.4, 0.6]) if inst_type == 'College' else np.random.choice([0,1], p=[0.7, 0.3]),
            'Internet_2010': 0  # Will evolve over years
        }
        institutions.append(institution)

    # ====== Yearly Time-Series Data ======
    full_data = []
    current_year = datetime.now().year
    budget_mean = 25000000  # 25 million BDT
    budget_std = 10000000
    
    for inst in institutions:
        for year in range(start_year, end_year + 1):
            # Base population growth
            students = max(100, int(np.random.normal(
                500 if inst['Institution_Type'] == 'Secondary School' else 800, 
                200
            ) * (1.03 ** (year - 2010))))
            
            # Gender ratios with temporal improvement
            female_student_pct = np.clip(np.random.normal(
                54.67 if inst['Institution_Type'] == 'Secondary School' else 
                50.37 if inst['Institution_Type'] == 'College' else 33.42,
                5 + (year-2010)*0.3  # Reducing variance over time
            ), 30, 70)
            

            prob = 0.9492 + 0.005 * (year - 2010)
            prob = min(max(prob, 0), 1)


            # Quality indicator progression
            quality = {
                'TSR': np.clip(np.random.normal(
                    34 - (year-2010)*0.5 if inst['Institution_Type'] == 'Secondary School' else
                    27 + (year-2010)*0.3 if inst['Institution_Type'] == 'College' else 20,
                    2
                ), 15, 60),
                
                'Computer_Facility': inst['Computer_Facility_2010'] * (1 + 0.1*(year-2010)),
                'Internet_Access': min(1, inst['Internet_2010'] + 0.12*(year-2010)),

                'Electricity_Access': np.clip(np.random.normal(0.7 + 0.03*(year-2010), 0.1), 0, 1),
                # 'Girls_Toilet': np.random.choice([0,1], p=[
                #     1 - (0.9492 + 0.005*(year-2010)), 
                #     0.9492 + 0.005*(year-2010)
                # ])
                'Girls_Toilet': np.random.choice([0, 1], p=[1 - prob, prob])

            }

            # Academic performance
            dropout_rate = np.clip(np.random.normal(
                35.66 - 0.8*(year-2010) if inst['Institution_Type'] == 'Secondary School' else
                21.14 - 0.5*(year-2010) if inst['Institution_Type'] == 'College' else 40.00 - 1.2*(year-2010),
                3
            ), 5, 50)

            # Financial metrics
            # budget = np.random.lognormal(
            #     mean=np.log(2e7 * (1.05 ** (year-2010))),
            #     sigma=0.5
            # )
            budget = max(0, np.random.normal(budget_mean, budget_std))

            yearly_data = {
                **inst,
                'Year': year,
                'Total_Students': students,
                'Female_Students': int(students * female_student_pct/100),
                'Disabled_Students': int(np.random.normal(students*0.05, students*0.01)),
                'Teachers': max(5, int(students / quality['TSR'])),
                'TSR': quality['TSR'],
                'Dropout_Rate': dropout_rate,
                'Completion_Rate': 100 - dropout_rate,
                'Pass_Rate': np.clip(np.random.normal(
                    83.04 + 0.3*(year-2010) if 'School' in inst['Institution_Type'] else 
                    77.78 + 0.4*(year-2010), 3
                ), 60, 99),
                'Computer_Facility': quality['Computer_Facility'],
                'Internet_Access': quality['Internet_Access'],
                'Electricity_Access': quality['Electricity_Access'],
                'Girls_Toilet': quality['Girls_Toilet'],
                'Budget': budget,
                'Community_Contribution': budget * np.random.uniform(0.01, 0.1),
                # 'SPI': np.random.normal(500, 100),  # Student Performance Index
                # 'TPI': np.random.normal(30, 5),     # Teacher Performance Index
                'Solar_System': np.random.choice([0,1], p=[0.9, 0.1]) if year < 2015 else np.random.choice([0,1], p=[0.7, 0.3])
            }

            # Remove institution-specific type if not applicable
            if yearly_data['Institution_Type'] != 'Madrasah':
                yearly_data['Madrasah_Type'] = None
            if yearly_data['Institution_Type'] != 'College':
                yearly_data['College_Type'] = None

            full_data.append(yearly_data)

    df = pd.DataFrame(full_data)
    
    # ====== Post-Processing ======
    # Convert probabilities to binary outcomes
    df['Computer_Facility'] = df['Computer_Facility'].apply(lambda x: 1 if x > 0.5 else 0)
    df['Internet_Access'] = df['Internet_Access'].apply(lambda x: 1 if x > 0.5 else 0)
    
    # Format financial metrics
    financial_cols = ['Budget', 'Community_Contribution']
    df[financial_cols] = df[financial_cols].applymap(lambda x: round(x, 2))
    
    # Add metadata
    df['Data_Source'] = "BANBEIS 2021, APSC Report, DPE Statistics"
    
    return df

# Generate dataset (100 institutions × 12 years = 1200 rows)
education_df = generate_education_data()
output_path = os.path.join(os.getcwd(), "education_data.csv")
education_df.to_csv(output_path, index=False)