# American Gut Survey Explorer

## Project Description

This project converts an R Shiny application into a standalone Python command-line script. The program retrieves survey information from NCBI BioSample records associated with the American Gut Project, filters the records for a selected survey question, and exports the results to a CSV file.

The script allows users to provide text files containing NCBI BioSample accession numbers and retrieve survey responses using the NCBI BioSamples API.

## Project Files

- `american_gut.py` – Main Python script used to retrieve and filter survey responses.
- `input/sample_id_1.txt` – First example input file containing BioSample accession numbers.
- `input/sample_id_2.txt` – Second example input file containing BioSample accession numbers.
- `input/sample_id_3.txt` – Third example input file containing BioSample accession numbers.
- `antibiotic_history_results.csv` – CSV output containing sample IDs and their survey responses.

## Requirements

The program requires Python 3 and the following Python packages:

- requests
- pandas

Install the required packages using:

```bash
pip install requests pandas
```

## How to Run the Program

Open a terminal and navigate to the project folder.

Run the script using an input text file:

```bash
python american_gut.py input/sample_id_1.txt
```

Other example input files can be selected:

```bash
python american_gut.py input/sample_id_2.txt
```

```bash
python american_gut.py input/sample_id_3.txt
```

## Survey Question

The default survey question retrieved by the program is `antibiotic_history`.

A different survey question can be specified using the `--question` argument:

```bash
python american_gut.py input/sample_id_1.txt --question antibiotic_history
```

## Output

The program exports the retrieved survey information into a CSV file.

The output contains three columns:

- `Sample_ID` – NCBI BioSample accession number.
- `Question` – Survey question retrieved.
- `Response` – Corresponding survey response.

## Data Source

NCBI BioSamples API: https://www.ebi.ac.uk/biosamples/
