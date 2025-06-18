# 1st normal form

Let's first look at the requirements for *first normal form*:
- **Atomicity:** Each column must contain only indivisible values - no lists, sets, or multiple values in one cell.
- **Uniqueness of rows:** Each row should be unique.
- **Same data type per column:** Each column should contain data of the same type (e.g., all dates, all integers).

## Analysis

The python file *first.py* contains code to see if all requirements are met.  
*While atomicity often requires manual inspection, I programmatically flag suspicious patterns using the code. This won’t catch all cases but will help me find find common atomicity violations like embedded lists or compound fields.*

## physiological_cycles.csv

✅ Atomic values: All columns to have atomic values. No lists or multiple values in a single field.  
✅ Uniqueness of rows: There are no duplicate rows.  
✅ Consistent data types: Each column appears to contain uniform types.

## workouts.csv

✅ Atomic values: All columns to have atomic values. No lists or multiple values in a single field.  
✅ Uniqueness of rows: There are no duplicate rows.  
✅ Consistent data types: Each column appears to contain uniform types.

## sleeps.csv

✅ Atomic values: All columns to have atomic values. No lists or multiple values in a single field.  
✅ Uniqueness of rows: There are no duplicate rows.  
✅ Consistent data types: Each column appears to contain uniform types.

## Conclusion

No changes are needed since the data files are already in first normal form.