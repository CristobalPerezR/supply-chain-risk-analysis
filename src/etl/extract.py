import pandas as pd

def extract_from_csv(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, encoding='latin1')
        print(f"Extraídas {len(df)} filas desde {path}")
        return df
    except Exception as e:
        raise ValueError(f"Error en extracción: {e}")