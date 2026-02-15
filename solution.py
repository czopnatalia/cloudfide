import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # validation
    # new column label
    for char in new_column:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_'):
            return pd.DataFrame([])

    # existing columns labels    
    for col in df.columns:
        for char in str(col):
            if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_'):
                return pd.DataFrame([])     

    # operations
    operator = ''
    for op in ["+", "-", "*"]:
        if op in role:
            operator = op
            break
    
    if not operator:
        return pd.DataFrame([])
    
    # spliting role argument
    parts = role.split(operator)
    if len(parts) != 2:
        return pd.DataFrame([])
    
    col1 = parts[0].strip()
    col2 = parts[1].strip()

    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame([])
    
    for col in [col1, col2]:
        for char in col:
            if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_'):
                return pd.DataFrame([])
            
    # main calculations
    try:
        new_df = df.copy()
        if operator == "+":
            new_df[new_column] = df[col1] + df[col2]
        elif operator == "-":
            new_df[new_column] = df[col1] - df[col2]
        elif operator == "*":
           new_df[new_column] = df[col1] * df[col2] 
        return new_df
    except:
        return pd.DataFrame([])



    
    
    
    
    
    
    
    
    
    
    
    
    return pd.DataFrame([])
