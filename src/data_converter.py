import dataclasses
import json
from pathlib import Path

import pandas as pd

from src.data_file import item_pos, ndc_type, checkData
from src.json_constructol import json_constructor
from src.setting import check_send_src, cor_date, cor_doc_num, address, tax_type


def data_converter(file_name: Path) -> json:
    file_data = pd.read_csv(file_name)
    items_list_class = []
    total_amount = 0.0
    for el in file_data.iterrows():
        total_amount = 0.00
        items_list_class = []
        item_class = item_pos(
            el[1]['Наименование предмета расчета'],
            el[1]['Количество'],
            el[1]['Цена'],
            ndc_type[el[1]['Ставка НДС']],
        )
        items_list_class.append(dataclasses.astuple(item_class))
        total_amount += item_class.total()
    recipe_data = checkData(
        check_send_src=check_send_src,
        cor_date=cor_date,
        cor_doc_num=cor_doc_num,
        address=address,
        tax_type=tax_type,
        payment_type='cash',
        total_amount=round(total_amount, 2),
        items=items_list_class
    )
    return json_constructor(recipe_data)
