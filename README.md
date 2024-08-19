# Financial data compaction

## Objective
The goal of this project is to build a feature that parses the relationships between cells or sets of cells that define the budget, synthesizing it to its essentials.

## Approach

### 1. Data Class Design
I defined a `FinancialCategory` data class to represent each financial metric (e.g., Product Sales, Cost of Goods Sold). This class includes:
- **Name**: The name of the financial category.
- **Present Value**: The starting value for the category.
- **Growth Rate**: The assumed percentage increase (if applicable).

### 2. Algorithm
The algorithm follows these steps:
- Read the csv and extract financial categories and their values.
- Identify growth rates by analyzing the data.
- Capture the findings in the `FinancialCategory` data class.

### 3. Scope for expansion
- Improve parsing algorithm to be more dynamic.
- Marketing expenses are constant for a given period of time, identify categories that cannot be projected with a growth rate and have a type to indentify them in the data class.
- Define methods for `FinancialCategory` data class that can project values for future based on growth rate.
- Serialize the financial data to JSON for saving or sharing.
- Identify key ratio values such as: 
    - Marketing ratio - Marketing expenses / Total Sales.
    - Salary ratio - Staff salaries / Total Sales.

## Example data class after processing the sheet

### Stored instances
```python
FinancialCategory(name='Product Sales', present_value=80000.0, growth_rate=4.0)
FinancialCategory(name='Service Sales', present_value=20000.0, growth_rate=5.0)
FinancialCategory(name='Total Sales', present_value=100000.0, growth_rate=4.21)
FinancialCategory(name='Cost of Goods Sold', present_value=60000.0, growth_rate=3.37)
FinancialCategory(name='Marketing', present_value=5000.0, growth_rate=9.09)
FinancialCategory(name='Staff salaries', present_value=20000.0, growth_rate=6.58)
FinancialCategory(name='Total Operating Expenses', present_value=85000.0, growth_rate=4.34)
FinancialCategory(name='Net Income', present_value=15000.0, growth_rate=3.82)
