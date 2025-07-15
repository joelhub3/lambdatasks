from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class OnboardUserEventRoot(BaseModel):
    system_id: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = Field()
    preferred_username: Optional[str] = Field()
    related_accounts: list[AccountItem] = Field(default_factory=list)
    contact_info: ContactInfo
    payment_id: str


class AccountItem(BaseModel):
    id: str
    user_description: str


class ContactInfo(BaseModel):
    preferred_language: Optional[str]
    email: Optional[str]
    address: Optional[Address] = Field(default_factory=Address)
    phone: Optional[str]


class Address(BaseModel):
    home_address1: str
    home_address2: Optional[str] = Field()
    city: str
    state: str = Field(default="")
    country_code: str = Field(default="US")
