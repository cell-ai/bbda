import pandas as pd
import re

def parse_busco_res(text):
    """
    Parses BUSCO summary text and returns a pandas DataFrame with extracted metrics.

    Parameters:
    text (str): The BUSCO summary output as a string.

    Returns:
    pd.DataFrame: A DataFrame with BUSCO completeness metrics and counts.
    """
    # Extract percentage summary
    summary_line = re.search(r'C:(\d+\.?\d*)%\[S:(\d+\.?\d*)%,D:(\d+\.?\d*)%\],F:(\d+\.?\d*)%,M:(\d+\.?\d*)%,n:(\d+)', text)
    if not summary_line:
        raise ValueError("Could not find summary line in BUSCO output.")

    summary_data = {
        'Complete (%)': float(summary_line.group(1)),
        'Single-copy (%)': float(summary_line.group(2)),
        'Duplicated (%)': float(summary_line.group(3)),
        'Fragmented (%)': float(summary_line.group(4)),
        'Missing (%)': float(summary_line.group(5)),
        'Total BUSCOs': int(summary_line.group(6))
    }

    # Extract counts
    patterns = {
        'Complete BUSCOs': r'(\d+)\s+Complete BUSCOs',
        'Single-copy BUSCOs': r'(\d+)\s+Complete and single-copy BUSCOs',
        'Duplicated BUSCOs': r'(\d+)\s+Complete and duplicated BUSCOs',
        'Fragmented BUSCOs': r'(\d+)\s+Fragmented BUSCOs',
        'Missing BUSCOs': r'(\d+)\s+Missing BUSCOs',
    }

    counts = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if not match:
            raise ValueError(f"Could not find pattern for '{key}' in BUSCO output.")
        counts[key] = int(match.group(1))

    # Combine and return as DataFrame
    data = {**summary_data, **counts}
    return pd.DataFrame([data])
