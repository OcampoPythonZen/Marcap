import xlrd

# Leer el archivo con las especificaciones mostradas
def open_file(path):
    book = xlrd.open_workbook(path)
    print('Numero de hojas:',book.nsheets)
    print('Nombre de las hojas:',book.sheet_names())
    get_first_sheet = book.sheet_by_index(0)
    print(get_first_sheet.row_values(0))
    cell = get_first_sheet.cell(1,1)
    print(cell)
    print(cell.value)
    print()
    
    cells = get_first_sheet.row_slice(rowx=0, start_colx=0, end_colx=20)
    for cell in cells:
        print(cell.value)

if __name__ == "__main__":
    path = '/home/eocampo/Django_Urbvan/Banquetes/Banquetes_Ocampo/Marcap/Orden de Compras.xlsx'
    open_file(path)
