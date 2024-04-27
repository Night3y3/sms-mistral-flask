from langchain_core.pydantic_v1 import BaseModel,Field
from typing import Optional

class ExpenseSchema(BaseModel):
    amount: Optional[str] = Field(title="expense", description="Expense made in the transaction")
    merchant: Optional[str] = Field(title="merchant", description="Merchant name whom the transaction was made")
    currency: Optional[str] = Field(title="currency", description="Currency of the transaction")