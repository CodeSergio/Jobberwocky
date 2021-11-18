from pydantic import BaseModel, EmailStr, Field

class jobpost(BaseModel):
    name: str = Field(example="Python developer Jr.")
    salary: int = Field(example=100000)
    country: str = Field(example="Argentina")
    skills:  list = Field(example=["Python","Flask"])

class jobalert(BaseModel):
    alert_term: str = Field(example="Python")
    email: EmailStr = Field(example="user@domain.com")