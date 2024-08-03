import pandas as pd


class load_data():
    __data_required = {"FRAC_107", "FRAC_108", "FECHA_COMPARESENCIA", "SESION_VOTACION", 
                     "FECHA_VOTACION", "SESION_DICTAMEN", "FECHA_DICTAMEN",	"RESOLUCION", 
                     "FRAC_110", "NOMBRE_PRESIDENTE_CONSEJO"}
    file_name = ""
    rute = ""
    

    def __init__(self, file = "DATA.xlsx", rute = ".") -> None:
        self.file_name = file
        self.rute
        self.file = pd.read_excel(self.file_name)
        self.validate_columns()

    def get_data_required(self):
        return self.__data_required
    
    def get_data_file(self):
        return self.file
    
    def validate_columns(self):
        columnas = set(self.file.columns)
        columnas_faltantes = self.__data_required - columnas

        if columnas_faltantes:
            raise("faltan columnas")

        else:
            print("columans completas")

if __name__ == "__main__":
    data = load_data(file = "DICTAMENES.xlsx")
    