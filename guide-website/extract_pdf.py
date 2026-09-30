import fitz  # PyMuPDF
import os

pdf_path = r"f:\clients\daria\First_Year_Guide_Daria.pdf"
output_dir = r"f:\clients\daria\guide-website\public\pdf_images"
text_output_path = r"f:\clients\daria\guide-website\extracted_text.txt"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    
    with open(text_output_path, "w", encoding="utf-8") as text_file:
        for page_index in range(len(doc)):
            page = doc[page_index]
            
            # Extract text
            text = page.get_text()
            text_file.write(f"--- PAGE {page_index + 1} ---\n")
            text_file.write(text)
            text_file.write("\n\n")
            
            # Extract images
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                image_filename = f"page_{page_index + 1}_img_{img_index + 1}.{image_ext}"
                image_filepath = os.path.join(output_dir, image_filename)
                
                with open(image_filepath, "wb") as image_file:
                    image_file.write(image_bytes)
                    
    print(f"Successfully extracted text to {text_output_path}")
    print(f"Successfully extracted images to {output_dir}")
except Exception as e:
    print(f"An error occurred: {e}")
