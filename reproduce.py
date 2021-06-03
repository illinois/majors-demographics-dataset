import pandas as pd
import numpy as np
import glob
import math

data = []
for filename in glob.glob("www.dmi.illinois.edu/stuenr/ethsexres/*.xls"):  # iterate
    year_data = pd.read_excel(
        filename, skiprows=4, header=[0, 1], na_values=["", np.NaN, "nan", float("nan")]
    ).convert_dtypes()

    filename = filename.replace("new", "")
    year = filename[-6:-4]
    term = filename[-8:-6]

    # Add useful cols
    term_mapping = {"sp": "spring", "fa": "fall", "su": "summer"}
    year_data["term"] = [term_mapping[term]] * len(year_data)
    year_data["year"] = [year] * len(year_data)

    year_data.columns = year_data.columns.map(  # clean up col names
        lambda col: "_".join(
            [
                x
                for x in (
                    "_".join(c for c in col if "Unnamed" not in c)
                    .replace(" ", "_")
                    .lower()  # lowercase
                    .replace("_(new*)_", "_")  # remove new designation
                ).split(
                    "_"
                )  # get rid of double and triple underscores
                if x
            ]
        )
    )

    data.append(year_data)  # collect

df = pd.concat(data).reset_index()  # combine


# Final cleanup
df["academic_program_code"] = (
    df["academic_program_code"]
    .astype(str)
    .apply(lambda x: x.rstrip())
    .apply(lambda x: np.NaN if x == "nan" or not x.rstrip() else x)
)
df["major_name"] = df["major_name"].astype(str).apply(lambda x: x.rstrip())
df = df.dropna(subset=["academic_program_code"]).reset_index()  # drop useless cols

del df["index"]
del df["level_0"]

df.to_csv("ethsex_all.csv", index=False)  # save
