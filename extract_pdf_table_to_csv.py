from spire.pdf import *
from spire.xls import *
import os

# Define a function to extract data from PDF tables to CSV


def extract_table_data_to_csv(pdf_path, csv_path):
    # Create an instance of the PdfDocument class
    doc = PdfDocument()

    try:
        # Load a PDF Document
        doc.LoadFromFile(pdf_path)

        # Create an instance of the PdfTableExtractor class
        extractor = PdfTableExtractor(doc)

        # Create an instance the workbook class
        workbook = Workbook()

        # Remove the default 3 worksheet
        workbook.Worksheets.Clear()

        # Iterate through the pages in the PDF Document
        for page_index in range(doc.Pages.Count):

            # Extract tables from each page
            tables = extractor.ExtractTable(page_index)
            if tables is not None and len(tables) > 0:

                # Iterate through the extracted tables
                for table_index, table in enumerate(tables):
                    # Create a new worksheet for each table
                    worksheet = workbook.CreateEmptySheet()

                    row_count = table.GetRowCount()
                    col_count = table.GetColumnCount()

                    # Extract data from the table and populate the worksheet
                    for row_index in range(row_count):
                        for col_index in range(col_count):
                            data = table.GetText(row_index, col_index)
                            worksheet.Range[row_index+1,
                                            col_index+1].Value = data.strip()

                    csv_name = csv_path + \
                        f'Table {table_index +
                                 1} of the page {page_index+1}'+'.csv'

                    # Save each worksheet to a separate CSV file
                    worksheet.SaveToFile(csv_name, ",", Encoding.get_UTF8())
    except Exception as e:
        print(f'Error occured: {str(e)}')


# Example Usage
pdf_path = 'SaleData.pdf'
csv_path = 'CSV/'

extract_table_data_to_csv(pdf_path, csv_path)
