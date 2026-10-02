"""
Educational hematology data-analysis workflow.

All data are synthetic.
The review criteria below are illustrative programming rules only
and are NOT validated clinical decision rules.
"""

import pandas as pd
import matplotlib.pyplot as plt

FLAG_COLUMNS = [
    "flag_blasts",
    "flag_atypical_lymphocytes",
    "flag_immature_granulocytes",
    "flag_platelet_clumps",
]

def load_data(path="synthetic_cbc_data.csv"):
    df = pd.read_csv(path)

    numeric_cols = [
        "wbc", "hb", "plt", "neut_abs",
        "lymph_abs", "mono_abs", "eos_abs", "baso_abs",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def apply_demo_review_rule(df):
    """
    Apply a simplified, illustrative smear-review trigger.

    This demonstrates how multiple analytical conditions can be
    combined programmatically. It is not a clinical rule.
    """
    numerical_trigger = (
        (df["wbc"] < 2.0)
        | (df["wbc"] > 30.0)
        | (df["hb"] < 8.0)
        | (df["plt"] < 80)
        | (df["plt"] > 800)
        | (df["neut_abs"] < 1.0)
    )

    flag_trigger = df[FLAG_COLUMNS].any(axis=1)

    out = df.copy()
    out["numerical_trigger"] = numerical_trigger
    out["flag_trigger"] = flag_trigger
    out["demo_smear_review"] = numerical_trigger | flag_trigger
    return out

def print_summary(df):
    print("\nCBC descriptive summary")
    print("-----------------------")
    print(
        df[[
            "wbc", "hb", "plt", "neut_abs",
            "lymph_abs", "mono_abs", "eos_abs", "baso_abs"
        ]].describe().round(2)
    )

    print("\nReview queue summary")
    print("--------------------")
    print(df["demo_smear_review"].value_counts())

    print("\nSamples entering the illustrative review queue")
    print("------------------------------------------------")
    cols = [
        "sample_id", "wbc", "hb", "plt", "neut_abs",
        "analyzer_comment", "numerical_trigger",
        "flag_trigger", "demo_smear_review",
    ]
    print(df.loc[df["demo_smear_review"], cols].to_string(index=False))

def make_plots(df):
    plt.figure()
    plt.scatter(df["wbc"], df["plt"])
    plt.xlabel("WBC (×10^9/L)")
    plt.ylabel("Platelets (×10^9/L)")
    plt.title("Synthetic CBC dataset: WBC vs platelets")
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.hist(df["hb"], bins=8)
    plt.xlabel("Hemoglobin (g/dL)")
    plt.ylabel("Number of samples")
    plt.title("Synthetic hemoglobin distribution")
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.scatter(df["neut_abs"], df["lymph_abs"])
    plt.xlabel("Absolute neutrophils (×10^9/L)")
    plt.ylabel("Absolute lymphocytes (×10^9/L)")
    plt.title("Synthetic differential count")
    plt.tight_layout()
    plt.show()

def main():
    df = load_data()
    df = apply_demo_review_rule(df)
    print_summary(df)
    make_plots(df)

if __name__ == "__main__":
    main()
