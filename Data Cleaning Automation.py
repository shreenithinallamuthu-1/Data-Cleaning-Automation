import os
import pandas as pd


def collect_user_data():
    """Simulates collecting potentially messy data from the user."""
    print("--- Phase 1: User Data Collection ---")
    print("Enter details for 3 users (feel free to leave things blank or type typos to test the cleaner!)\n")

    data = []
    for i in range(1, 4):
        print(f"--- Entering Data for Record #{i} ---")
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        email = input("Enter Email: ").strip()
        city = input("Enter City: ").strip()

        # Append as a dictionary
        data.append({"Name": name, "Age": age, "Email": email, "City": city})

    # Let's artificially inject a duplicate record to demonstrate automation!
    print("\n[System] Injecting a duplicate record automatically for testing...")
    if data:
        data.append(data[-1])

    # Convert to DataFrame and save to raw CSV
    df_raw = pd.DataFrame(data)
    raw_filename = "data_cleaning_automation.csv"
    df_raw.to_csv(raw_filename, index=False)
    print(f"✔️ Raw data successfully saved to '{raw_filename}'\n")
    return raw_filename


def automated_cleaner(input_file, output_file):
    """Automatically loads, cleans, and saves the data."""
    print("--- Phase 2: Automated Data Cleaning ---")

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    # 1. Load the raw data
    df = pd.read_csv(input_file)
    print(f"📋 Loaded {len(df)} records. Starting cleanup...")

    # 2. Handle missing or whitespace-only values
    # Replace empty strings or spaces with actual NaN values
    df.replace(r"^\s*$", pd.NA, regex=True, inplace=True)

    # Fill missing string columns
    df["Name"] = df["Name"].fillna("Unknown")
    df["Email"] = df["Email"].fillna("Not Provided")
    df["City"] = df["City"].fillna("Unknown")

    # 3. Standardize text casing (Fixes "new york" vs "New York")
    df["Name"] = df["Name"].str.title()
    df["City"] = df["City"].str.title()
    df["Email"] = df["Email"].str.lower()

    # 4. Clean and validate numeric data (Age)
    # Convert non-numeric ages to NaN, then fill with the median age or a default
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    median_age = df["Age"].median()
    # Fallback to 30 if all ages entered were invalid/blank
    fallback_age = int(median_age) if not pd.isna(median_age) else 30
    df["Age"] = df["Age"].fillna(fallback_age).astype(int)

    # 5. Remove exact duplicate rows
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    final_count = len(df)
    print(f"🧹 Removed {initial_count - final_count} duplicate row(s).")

    # 6. Save the polished data
    df.to_csv(output_file, index=False)
    print(f"✨ Cleaned data successfully saved to '{output_file}'\n")

    # Display the final results in the console
    print("--- Final Cleaned Dataset Preview ---")
    print(df)


# --- Execution Flow ---
if __name__ == "__main__":
    raw_csv = collect_user_data()
    cleaned_csv = "cleaned_user_data.csv"
    automated_cleaner(raw_csv, cleaned_csv)
