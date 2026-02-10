#Pydantic is a Python library used for: Data validation, Data parsing, Type safety
#**Python type hints** to automatically: - Validate data, - Convert data types, - Raise clear errors
#### With Pydantic - Invalid data is caught **early**, - Cleaner code, - Fewer bugs, - Production-ready

from pydantic import BaseModel, ValidationError, Field, EmailStr, field_validator
from typing import Optional


class User(BaseModel):
    name:str = Field(min_length=3, max_length=25)
    age:int = Field(gt=0, lt=20)
    # email: Optional[str] = None
    email:EmailStr = None
    is_active:bool = True
    @field_validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Age must be at least 18')
        return value

try:
    user = User(name = 'Robert Walker', age = 19, email = 'rob@gmail.com',
                is_active = False)
except ValidationError as e:
    print(e)


print(user)
print(user.age)
print(type(user.name))


