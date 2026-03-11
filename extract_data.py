import pandas as pd


def extract_data(df: pd.DataFrame, df1: pd.DataFrame, outdf: pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        df1 (pd.DataFrame): _description_
        outdf (pd.DataFrame): _description_

    Returns:
        _type_: _description_
    """
    status_counts_P2P = df["Status"].value_counts()
    status_counts_RTR = df1["Status"].value_counts()
    data_P2P = {
        "Completed": status_counts_P2P.get("Completed", 0),
        "Inprogress": status_counts_P2P.get("In Progress", 0),
        "Not started": status_counts_P2P.get("Not Started", 0),
        "Pending Review": status_counts_P2P.get("Pending Review", 0),
        "Sent to Mobileum Review": status_counts_P2P.get("Sent to Mobileum Review", 0),
        "Testing": status_counts_P2P.get("Testing", 0),
    }
    data_RTR = {
        "Completed": status_counts_RTR.get("completed", 0),
        "Inprogress": status_counts_RTR.get("In progress", 0),
        "Not started": status_counts_RTR.get("Not Started", 0),
        "Pending Review": status_counts_RTR.get("Pending Review", 0),
        "Sent to Mobileum Review": status_counts_RTR.get("Sent to Mobileum Review", 0),
        "Testing": status_counts_RTR.get("Testing", 0),
    }
    summary_df: pd.DataFrame = pd.DataFrame([data_P2P, data_RTR], index=["P2P", "RTR"])
    return summary_df
