import markdown2
from weasyprint import HTML
import os

def markdown_to_pdf(markdown_file):
    """
    Convert a Markdown file to a PDF file with rendered HTML formatting.

    Args:
        markdown_file (str): Path to the input Markdown file.
    """
    try:
        # Check if the markdown file exists
        if not os.path.exists(markdown_file):
            print(f"Error: {markdown_file} does not exist.")
            return

        # Read the Markdown content
        with open(markdown_file, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()

        # Convert Markdown to HTML
        html_content = markdown2.markdown(markdown_text)

        # Generate output PDF filename
        base_name = os.path.splitext(markdown_file)[0]
        output_pdf = f"{base_name}_pdf.pdf"

        # Render HTML content to PDF using WeasyPrint
        HTML(string=html_content).write_pdf(output_pdf)
        print(f"PDF created successfully: {output_pdf}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory = os.getcwd()  # Get the current working directory
    for file_name in os.listdir(directory):
        if file_name.endswith('.md'):  # Process only Markdown files
            markdown_to_pdf(file_name)
