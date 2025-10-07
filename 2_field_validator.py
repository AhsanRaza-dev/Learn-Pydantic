from pydantic import BaseModel,EmailStr,Field
from typing import List, Dict, Optional, Annotated

# there is a scienario where the hospital typed a mou with the company that their company employees will get free health checkups so we have to validate that the email provided is from the company domain only like @company.com

# we can achieve this by using a custom validator
from pydantic import field_validator

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

    @field_validator('email')
    @classmethod
    def validate_company_email(cls, value):
        valid_domains = ['curiologix.com' ,'allzone.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of the following: {", ".join(valid_domains)}')
        return value