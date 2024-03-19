from tqdm import tqdm

import pandas as pd

from src.data_file import PATH_TO_OUTPUT, FILE_DATA


def excel_upload():
    file_data = pd.read_excel(FILE_DATA)

    for el in tqdm(file_data[file_data['Позиций'] > 0].iterrows()):
        pos = el[0] + 1
        count = int(el[1]['Позиций'])
        one_rec_item = file_data.iloc[pos:pos + count][
            ['Наименование предмета расчета', 'Количество', 'Цена', 'Ставка НДС']]
        if el[1]['Наличными'] > 0:
            path_output_type = PATH_TO_OUTPUT.joinpath('cash')
        elif el[1]['Безналичными'] > 0:
            path_output_type = PATH_TO_OUTPUT.joinpath('electronically')
        elif el[1]['Аванс'] > 0:
            path_output_type = PATH_TO_OUTPUT.joinpath('prepaid')

        file_output = path_output_type.joinpath(f'{el[1]["№ ФД"]}')
        one_rec_item.to_csv(file_output)
