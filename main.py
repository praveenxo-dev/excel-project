import pandas as pd

from alert import apply_conditional_formatting
from extract_data import extract_data


def main():
    df = pd.read_excel("data/Mobileum  - CRP Tracker - P2P.xlsx", sheet_name="CRP Action Items")
    df1 = pd.read_excel("data/Mobileum - CRP Tracker -RTR.xlsx", sheet_name="Action Items - CRP")
    outdf = pd.read_excel("data/Final Template.xlsx")
    summary_df = extract_data(df, df1, outdf)
    with pd.ExcelWriter(
        "data/Final Template.xlsx", engine="openpyxl", mode="a", if_sheet_exists="overlay"
    ) as writer:
        summary_df.to_excel(
            writer, sheet_name="Sheet1", startrow=5, startcol=3, index=False, header=False
        )
    apply_conditional_formatting()


if __name__ == "__main__":
    main()
