from pydantic import BaseModel,EmailStr,Field
from typing import List, Dict, Optional, Annotated

# Basemodel is used to create data models with validation
# EmailStr is used to validate email fields
# Field is used to provide additional metadata and validation for model fields
# List, Dict, Optional are used to define types for fields
# Annotated is used to add metadata to types
# Here we are creating a Patient model with various fields and validations 


class Patients(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50,title="Full Name", description="The full name of the patient",examples=["Ahsan", "Raza"])] #this is showing the title and description also specifying the min and max length of the name using Field & Annotated

    age: int = Field(..., gt=0, lt=120, description="Age of the patient in years") # Field with a constraint that it must be greater than 0 and less than 120

    email:EmailStr # EmailStr will validate the email format

    phone: Optional[str] = None # Optional field can be None or can be skipped

    married: Optional[bool] = None # Optional field can be None or can be skipped

    allergies: List[str] = Field(max_length=5) # List of strings with a maximum length of 5

    medications: Dict[str, str] # Dictionary with string keys and string values

    height: float = Field(..., gt=0, strict= True,description="Height in centimeters") # Field with a constraint that it must be greater than 0 and description for documentation and strict to ensure type is float

    weight: float = Field(..., gt=0,strict= True, description="Weight in kilograms") # Field with a constraint that it must be greater than 0 and description for documentation and strict to ensure type is float

    bmi: float = Field(..., gt=0, description="Body Mass Index") # Field with a constraint that it must be greater than 0 and description for documentation

    blood_type: str = Field(..., pattern="^(A|B|AB|O)[+-]$", description="Blood type (A+, A-, B+, B-, AB+, AB-, O+, O-)") # Field with a regex constraint to match valid blood types

    conditions: List[str] = [] # List of strings with a default empty list

    emergency_contact: Dict[str, str] # Dictionary with string keys and string values

# Function to insert patient data and return the patient object
def insert_data(patient: Patients):
    return patient

# Example usage
patient_info = {
    "name": "John Doe",
    "age": 30,
    "email": "ahsanaj695@gmail.com",
    "phone": "123-456-7890",
    "married": False,
    "allergies": ["Peanuts", "Penicillin"],
    "medications": {"Aspirin": "100mg", "Lisinopril": "10mg"},
    "height": 175.5,
    "weight": 70.0,
    "bmi": 22.7,
    "blood_type": "O+",
    "conditions": ["Hypertension"],
    "emergency_contact": {"name": "Jane Doe", "relation": "Spouse", "phone": "123-456-7890"},
    
    }

# Creating a Patients object and inserting data
patient = insert_data(Patients(**patient_info))
print(patient)

