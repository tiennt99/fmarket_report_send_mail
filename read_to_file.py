import pandas as pd

def excel_to_email_body(file_path):
    # Read Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Convert DataFrame to HTML format
    email_body = df.to_html(index=False)

    return email_body

# Example usage
file_path = '/home/tiennguyen/Desktop/research/ck/tool/bao_cao.xlsx'
email_body = excel_to_email_body(file_path)
print(email_body)  #