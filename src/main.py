from tqdm import tqdm
from src.atolApi import atolJson
from src.data_converter import data_converter
from src.data_file import PATH_TO_OUTPUT, DRIVER_PATH

if __name__ == '__main__':
    print(' Start to load from Excel')
    # excel_upload()
    print('File imported')

    print('start to main proccess')

    cash_file_list = PATH_TO_OUTPUT.joinpath('cash').iterdir()
    electronically_file_list = PATH_TO_OUTPUT.joinpath('electronically').iterdir()
    prepaid_file_list = PATH_TO_OUTPUT.joinpath('prepaid').iterdir()

    atol = atolJson(DRIVER_PATH)
    for cash in tqdm(cash_file_list):
        msg = data_converter(cash)
        atol.send_json(msg)

    print('proccess finished')
