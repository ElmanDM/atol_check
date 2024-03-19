
from libfptr10 import IFptr


class atolJson:

    def __init__(self, dll_path):

        self.fptr = IFptr(dll_path)
        settings = {
            IFptr.LIBFPTR_SETTING_MODEL: IFptr.LIBFPTR_MODEL_ATOL_AUTO,
            IFptr.LIBFPTR_SETTING_PORT: IFptr.LIBFPTR_PORT_USB,
        }
        self.fptr.setSettings(settings)

    def send_json(self, msg):
        try:
            self.fptr.open()
            is_open = self.fptr.isOpened()
            if not is_open:
                print('no connect \n')
            else:
                print('connected \n')

            self.fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA, msg)
            self.fptr.processJson()

            result = self.fptr.getParamString(IFptr.LIBFPTR_PARAM_JSON_DATA)
        except Exception as ex:
            self.fptr.close()
            return f'err - {ex}'

        self.fptr.close()
        return result
