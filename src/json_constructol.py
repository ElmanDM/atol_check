import json

from src.data_file import checkData


def json_constructor(check_data: checkData) -> json:
    data = {
        "type": "sellCorrection",
        "taxationType": "osn",
        "electronically": True,
        "ignoreNonFiscalPrintErrors": False,

        "correctionType": "self",
        "correctionBaseDate": check_data.cor_date,
        "correctionBaseNumber": check_data.cor_doc_num,

        "operator": {
            "name": check_data.kassir_name,
            # "vatin": "123654789507"
        },

        "clientInfo": {
            "emailOrPhone": check_data.check_send_src
        },

        "items": check_data.items,
        "payments": [
            {
                "type": check_data.payment_type,
                "sum": check_data.total_amount
            }
        ],
        "total": check_data.total_amount

    }
    return json.dumps(data, indent=4, ensure_ascii=False)
