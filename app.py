import streamlit as st 
from pdf2docx import Converter
from docx import Document
from reportlab.pdfgen import canvas
import tempfile

st.set_page_config(
    page_title="File Conerter",
    page_icon="🔄️", 
    layout = "wide"
    )

st.title("Converter")
st.write("created by Piyush Kumar")

tab1,tab2 = st.tabs(["PDF --> WORD","WORD --> PDF"])

with tab1:
    st.header("PDF --> WORD")
    pdf_file = st.file_uploader("Add your file here",type = ['pdf'],key = ["pdf_to_word"])
    if pdf_file:
        if st.button("convert"):
            with st.spinner("working on it......."):
                with tempfile.NamedTemporaryFile(delete=False, suffix = ".pdf") as temp_pdf:
                    temp_pdf.write(pdf_file.read())
                    pdf_path = temp_pdf.name

                    docx_path = pdf_path.replace(".pdf",".docx")

                    cv = Converter(pdf_path)
                    cv.convert(docx_path)

                    cv.close()

                    with open(docx_path, "rb") as f:
                        st.success("conversion completed...")
                        st.download_button("Download your Word File",f,file_name="piyush_converted.docx")

with tab2:
    st.header("WORD --> PDF")
    docx_file = st.file_uploader("Add your file here",type = ['docx'], key = "word_to_pdf")
    if docx_file:
        if st.button("convert"):
            with st.spinner("working on it......."):
                with tempfile.NamedTemporaryFile(delete=False, suffix = ".docx") as temp_docx:
                    temp_docx.write(docx_file.read())
                    docx_path = temp_docx.name

                    pdf_path = docx_path.replace(".docx",".pdf")

                    doc = Document(docx_path)
                    c = canvas.Canvas(pdf_path)
                    y = 800
                    for p in doc.paragraphs:
                        text = p.text
                        if text.strip():
                            c.drawString(50,y,text)
                            y -= 20
                            if y<50:
                                c.showPage()
                                y=800

                    c.save()

                    with open(pdf_path, "rb") as f:
                        st.success("conversion completed...")
                        st.download_button("Download your PDF File",f,file_name="piyush_converted.pdf")


st.markdown("-------------------------------------------")
st.caption("Made with ❤️")
