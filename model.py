from dataclasses import dataclass

#data class to hold information about various categories 
@dataclass
class FinancialCategory:
    name: str
    present_value: float
    growth_rate: float