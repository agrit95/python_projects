from spire.pdf import *
from spire.xls import *


# Define an extract_table_data function to extract table data from PDF
def extract_table_data(pdf_path):
    # Create an instance of the PdfDocument class
    doc = PdfDocument()
    try:
        doc.LoadFromFile(pdf_path)
        # Create a list to store the extracted table data
        table_data = []

        # Create an instance of the PdfTableExtractor class
        extractor = PdfTableExtractor(doc)

        # Iterate through the pages in the PDF document
        for page_index in range(doc.Pages.Count):
            # Get tables within each page
            tables = extractor.ExtractTable(page_index)
            if tables is not None and len(tables) > 0:
                # Iterate through tables
                for table_index, table in enumerate(tables):
                    row_count = table.GetRowCount()
                    col_count = table.GetColumnCount()

                    table_data.append(
                        f'Table {table_index + 1} of Page {page_index + 1}:\n')

                    # Extract data from each table and append the data to the table_data list
                    for row_index in range(row_count):
                        row_data = []
                        for col_index in range(col_count):
                            data = table.GetText(row_index, col_index)
                            row_data.append(data.strip())
                        table_data.append("  ".join(row_data))  # Join the row data and add it to table_data
                    table_data.append('\n')  # Add a newline character after each row
        return table_data

    except Exception as e:
        print(f'Error occured: {str(e)}')
        return None


# Define a save_table_data_to_text function to save the table data extracted from a PDF to a text file
def save_table_data_to_text(table_data, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(table_data))
        print(f'Table data saved to {output_path} successfully!!!')
    except Exception as e:
        print(f'Error occured while saving table data: {str(e)}')


# Example usage
pdf_path = 'SaleData.pdf'
output_path = 'sale_data.txt'

data = extract_table_data(pdf_path)
if data:
    save_table_data_to_text(data, output_path)