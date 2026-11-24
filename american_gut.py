"""Project: American Gut Survey Explorer
Author: Kenia Garcia
Course: BIN601
Description:
This program retrieves survey information from NCBI BioSample
records associated with the American Gut Project, filters the
responses for a selected survey question, and exports the results
to a CSV file.
"""
import argparse
import requests
import pandas as pd
from pathlib import Path
import re


# Read BioSample accession numbers from an input text file
def read_sample_ids(input_file):

    # Open the input file and read each line
    with open(input_file, "r") as file:
        sample_ids = [line.strip() for line in file if line.strip()]

    # Keep only valid NCBI BioSample accession formats
    sample_ids = [
        sample_id for sample_id in sample_ids
        if re.fullmatch(r"(SAMEA|SAMN|SAMD)\d+", sample_id)
    ]

    # Remove duplicate IDs
    sample_ids = list(dict.fromkeys(sample_ids))

    return sample_ids
# Test reading the first input file
# Retrieve a selected survey response from one BioSample
def get_sample_response(sample_id, question):

    url = "https://www.ebi.ac.uk/biosamples/samples/" + sample_id

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        values = data.get("characteristics", {}).get(question)

        if values:
            return values[0].get("text", "")

        return ""

    except requests.RequestException as error:
        print("Error retrieving", sample_id, ":", error)
        return ""


# Process all BioSample IDs

# Process all BioSample IDs
if __name__ == "__main__":

    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description="Retrieve American Gut survey responses from NCBI BioSamples."
    )

    parser.add_argument(
        "input_file",
        help="Path to a text file containing BioSample IDs"
    )

    parser.add_argument(
        "--question",
        default="antibiotic_history",
        help="Survey question to retrieve"
    )

    args = parser.parse_args()

    # Read BioSample IDs from the selected input file
    input_file = Path(args.input_file)

    sample_ids = read_sample_ids(input_file)

    if not sample_ids:
        print("No valid BioSample IDs found.")
        raise SystemExit(1)

    question = args.question

    results = []

    # Retrieve the selected survey response for each sample
    for sample_id in sample_ids:

        answer = get_sample_response(sample_id, question)

        results.append({
            "Sample_ID": sample_id,
            "Question": question,
            "Response": answer
        })

        print("Processed:", sample_id)

    # Export results to a CSV file
    output_file = Path(__file__).resolve().parent / f"{question}_results.csv"

    pd.DataFrame(results).to_csv(output_file, index=False)

    print("\nTotal samples processed:", len(results))
    print("CSV saved to:", output_file)
