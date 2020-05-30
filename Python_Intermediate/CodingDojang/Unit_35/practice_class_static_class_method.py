class Data:
    @staticmethod
    def is_data_valid(data_string):
        year, month, day = map(int, data_string.split('-'))
        return month <= 12 and day <= 31

if Data.is_data_valid('2000-10-31'):
    print('올바른 날짜 형식입니다')
else:
    print('잘못된 날짜 형식입니다')