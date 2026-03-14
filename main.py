import os
import time

import pandas as pd
from alert import apply_conditional_formatting
from dotenv import load_dotenv
from extract_data import extract_data
from get_excel import get_excel
from picture import export_excel_to_image

load_dotenv()

RTR_URL = os.getenv("RTR_LINK")
P2P_URL = os.getenv("P2P_LINK")


def main():
    start_time = time.time()
    get_excel(RTR_URL, "data/Mobileum - CRP Tracker -RTR.xlsx")
    get_excel(P2P_URL, "data/Mobileum  - CRP Tracker - P2P.xlsx")
    print(f"Excel files downloaded in {time.time() - start_time:.2f} seconds.")
    time.sleep(2)  # Optional: Wait for a moment to ensure files are fully saved

    df = pd.read_excel(
        "data/Mobileum  - CRP Tracker - P2P.xlsx", sheet_name="CRP Action Items"
    )
    df1 = pd.read_excel(
        "data/Mobileum - CRP Tracker -RTR.xlsx", sheet_name="Action Items - CRP"
    )
    outdf = pd.read_excel("data/Final Template.xlsx")
    summary_df = extract_data(df, df1, outdf)
    with pd.ExcelWriter(
        "data/Final Template.xlsx",
        engine="openpyxl",
        mode="a",
        if_sheet_exists="overlay",
    ) as writer:
        summary_df.to_excel(
            writer,
            sheet_name="Sheet1",
            startrow=3,
            startcol=3,
            index=False,
            header=False,
        )
    print(
        f"Summary data written to Excel file successfully in {time.time() - start_time:.2f} seconds."
    )
    apply_conditional_formatting()
    print(f"Conditional formatting applied in {time.time() - start_time:.2f} seconds.")
    print("Excel file updated with summary data and conditional formatting applied.")
    export_excel_to_image(
        "data/Final Template.xlsx",
        "C:\\Users\\prave\\OneDrive\\Desktop\\work\\summary_image.png",
        "Sheet1",
        "A1:I5",
    )
    print("Excel file exported as image successfully.")
    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    main()
