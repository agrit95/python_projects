from spire.pdf import *
from spire.xls import *
from datetime import datetime

# Define an extract_table_data function to extract table data from PDF
def extract_table_data(pdf_path, xlsx_path):
    # Create an instance of the PdfDocument class
    doc = PdfDocument()

    try:
        doc.LoadFromFile(pdf_path)

        # Create an instance of the PdfTableExtractor class
        extractor = PdfTableExtractor(doc)

        # Create an instance of the workbook class
        workbook = Workbook()

        # Remove the default 3 worksheets
        workbook.Worksheets.Clear()

        # Iterate through the pages in the PDF document
        for page_index in range(doc.Pages.Count):

            # Get tables within each page
            tables = extractor.ExtractTable(page_index)

            if tables is not None and len(tables) > 0:

                # Iterate through tables
                for table_index, table in enumerate(tables):

                    # Create a new workbook for each table
                    worksheet = workbook.CreateEmptySheet()

                    # Set the workbook name
                    worksheet.Name = f'Table {
                        table_index + 1} of Page {page_index + 1}'

                    row_count = table.GetRowCount()
                    col_count = table.GetColumnCount()

                    # Extract data from each table and append the data to the table_data list
                    for row_index in range(row_count):
                        for col_index in range(col_count):
                            data = table.GetText(row_index, col_index)

                            # Check if the data matches the date format m-d-yy
                            try:
                                # Conver the date from m-d-yy to the desired foramt yyyy-mm-dd
                                parsed_date = datetime.strptime(data, '%m-%d-%y')
                                data = parsed_date.strftime('%Y-%m-%d')
                            except:
                                # If it's not a date, leave it as is
                                pass    

                            worksheet.Range[row_index+1,
                                            col_index+1].Value = data.strip()

                    # Auto adjust column widths of the worksheet
                    worksheet.Range.AutoFitColumns()


        # Save the workbook to the specified Excel file
        workbook.SaveToFile(xlsx_path, ExcelVersion.Version2016)

    except Exception as e:
        print(f'Error occured: {str(e)}')
        return None


# Example usage
pdf_path = 'SaleData.pdf'
output_path = 'sale_data.xlsx'

extract_table_data(pdf_path, output_path)
