from docxtpl import DocxTemplate
from pandas import DataFrame

class generate_doc(): 
    file =""
    def __init__(self, data_required,df, file = "plantilla.docx") -> None:
        self.data_required = data_required
        self.file = file
        self.df = df
        self.doc = DocxTemplate(file)
        self.convertir_dataframe()

    def convertir_dataframe(self):
        self.df = DataFrame(self.df)
        

    def generar_docs(self):
        for index, row in self.df.iterrows():
            #print(dict(row))
            self.doc.render(dict(row))
            self.doc.save(f"dictamen_{index}.docx")