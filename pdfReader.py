import pdfplumber


def pdf_text_and_image_extracter(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(len(pdf.pages)):
            page=pdf.pages[page_num]
            text=page.extract_text()

            # extract image data
            image=page.images

            print(f"Page :{page_num +1} Text: ")
            print(text)

            print(f"Page {page_num +1} Images: ")

            for img_num,img in enumerate(image):
                try:
                    img_data=img['stream'].get('data')

                    print(f"Image {img_num +1}: {len(img_data)} bytes")
                except:
                    print("pdf has no image data")



pdf_path="./cruise_form.pdf"
pdf_text_and_image_extracter(pdf_path)