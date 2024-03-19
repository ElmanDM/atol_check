from dataclasses import dataclass
from pathlib import Path

from src.setting import excel_file

ROOT_PATH = Path.cwd()
PATH_TO_OUTPUT = ROOT_PATH.joinpath('data').joinpath('records')
FILE_DATA = ROOT_PATH.joinpath('data').joinpath(excel_file).as_posix()
DRIVER_PATH = Path.cwd().joinpath('fptr10.dll').as_posix()

ndc_type = {
    'НДС 0%': 'vat0',
    'НДС 20%': 'vat20'
    }


@dataclass
class item_pos:
    '''
     vat = 'none'
     none - налогом не облагается
     vat0 - НДС 0%
     vat10 - НДС 10%
     vat110 - НДС 10/110
     vat20 - НДС 20%
     vat120 - НДС 20/120
    '''

    name: str
    price: float
    quality: int
    vat: str = 'none'

    def total(self) -> float:
        return self.price * self.quality


@dataclass
class checkData:
    '''
    tax_type = 'usnIncomeOutcome'
    osn - общая
     usnIncome - упрощенная (Доход)
     usnIncomeOutcome - упрощенная (Доход минус Расход)
     esn - единый сельскохозяйственный налог
     patent - патентна

      check_send_src  phone or email source for send check



          payment_type = 'cash'

     cash или 0 - наличными
     electronically или 1 - безналичными
     prepaid или 2 - предварительная оплата (аванс)
     credit или 3 - последующая оплата (кредит)
     5-9 - пользовательский тип оплаты
    '''

    cor_date: str
    cor_doc_num: str
    check_send_src: str
    address: str
    items: list
    total_amount: float
    kassir_name: str = 'Администратор'
    tax_type: str = "usnIncomeOutcome",
    payment_type: str = 'cash'
