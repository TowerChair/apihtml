from typing import Optional
from pydantic import BaseModel


class Data(BaseModel):
    data: Optional[str]
   