import os
from PIL import Image
def convert_images_to_pdf(image_paths, output_filename):
    pdf_pages = []    
    for path in image_paths:
        if not os.path.exists(path):
            print(f"Warning: '{path}' not found. Skipping.")
            continue  
        try:
            img = Image.open(path).convert('RGB')
            pdf_pages.append(img)
            print(f"Processed: {path}")
        except Exception as e:
            print(f"Error processing '{path}': {e}")
    if not pdf_pages:
        print("No valid images were found to convert.")
        return
    first_image = pdf_pages[0]
    rest_of_images = pdf_pages[1:]
    first_image.save(
        output_filename,
        save_all=True,
        append_images=rest_of_images
    )
    print(f"\nSuccess! PDF saved as: {output_filename}")
if __name__ == "__main__":
    input_images = ["image1.jpg", "image2.png"] 
    output_file = "output.pdf"    convert_images_to_pdf(input_images, output_file)
