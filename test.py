# Calculate AGI and repair any negative values
def calc_AGI(wages, interest, unemployment):
    AGI = abs(wages) + abs(interest) + abs(unemployment)
    return AGI

# Calculate deduction depending on single, dependent or married
def get_deduction(status):
    if status == 0:
        return 6000
    elif status == 1:
        return 12000
    elif status == 2:
        return 24000
    else:
        return 6000
# Calculate taxable but not allow negative results
def calc_taxable(agi, deduction):
    taxable = agi - deduction
    return max(taxable, 0)

# Calculate tax for single or dependent
def calc_tax(status, taxable):
    if status == 0 or status == 1:
        if taxable <= 10000:
            tax = taxable * 0.10
        elif taxable <= 40000:
            tax = 1000 + (taxable - 10000) * 0.12
        elif taxable <= 85000:
            tax = 4600 + (taxable - 40000) * 0.22
        else:
            tax = 14500 + (taxable - 85000) * 0.24
    else:
        if taxable <= 20000:
            tax = taxable * 0.10
        elif taxable <= 80000:
            tax = 2000 + (taxable - 20000)* 0.12
        else:
            tax = 9200 + (taxable - 80000) * 0.22
    return round (tax)

# Calculate tax due and check for negative withheld
def calc_tax_due(tax, withheld):
    withheld = max(withheld, 0)
    tax_due = tax - withheld
    return tax_due

if __name__ == '__main__':
    # Step #1: Input wages, interest, unemployment, status, withheld
        wages, interest, unemployment, status, withheld = map(int, input().split())

    # Step $2: Calculate AGI
        agi = calc_AGI(wages, interest, unemployment)
print(f"AGI: ${agi:,}")
    
deduction = get_deduction(status)
print(f'Deduction: ${deduction:,}')
    
taxable = calc_taxable(agi,deduction)
print(f'Taxable income: ${taxable:,}')
    
tax = calc_tax(status, taxable)
print(f'federal tax: ${tax:,}')
    
tax_due = calc_tax_due(tax, withheld)
print(f' Tax due: ${tax_due:,}')