from load_data import load_data
from generate_doc import generate_doc

df = load_data(file = "DICTAMENES.xlsx")
doc = generate_doc(data_required=df.get_data_required(),df = df.get_data_file(),file="PLANTILLA_DICTAMEN-CTCE.docx")
doc.generar_docs()