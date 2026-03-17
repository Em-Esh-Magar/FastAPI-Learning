from pydantic import field_validator, BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    address: str
    email: EmailStr

    @field_validator('email')
    @classmethod
    def email_validation(cls, value):
        valid_email = 'gmail.com'
        check = value.split('@')[-1]

        if check != valid_email:
            raise ValueError("Not correct")

        print(value)
        return value

    @field_validator('age', mode='after')
    @classmethod
    def age_validation(cls, value):
        if value < 0 or value > 100:
            raise ValueError("Age Not correct")

        print(value)
        return value


def show(user):
    print(user.name)


# Correct one
user_info1 = {
    'name': 'Ram',
    'age': 59,
    'address': 'KTM',
    'email': 'ram@gmail.com'
}

user = User(**user_info1)
show(user)

temp = user.model_dump()
print(temp)
print(type(temp))

temp2 = user.model_dump_json()
print(temp2)
print(type(temp2))