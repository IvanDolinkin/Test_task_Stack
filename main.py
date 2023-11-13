# Необходимо сформировать файл чеки_по_папкам.txt, в котором:
# 1. "разложить" файлы по папкам месяцев в формате /месяц/названиефайла
# 2. указать, в каком месяце какая услуга не оплачена (если таковые имеются) в формате
# не оплачены:
# месяц:
# услуга
# услуга

with open('чеки.txt', encoding='utf-8-sig') as file:
    info = file.read()


file_names = info.split()
months_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
               'декабрь']
services_list = sorted(list(set([x.split('_')[0] for x in file_names])), key=str.casefold)

paid_receipt = []
unpaid_receipt = ['не оплачены:']
for month in months_list:
    for name in file_names:
        if month in name:
            paid_receipt.append(f'/{month}/{name}')
    for service in services_list:
        test_string = f'{service}_{month}.pdf'
        if test_string not in file_names:
            if f'{month}:' not in unpaid_receipt:
                unpaid_receipt.append(f'{month}:')
            unpaid_receipt.append(service)
result = '\n'.join(paid_receipt + unpaid_receipt)

with open('чеки_по_папкам.txt', 'w', encoding='utf-8') as file:
    file.write(result)


def test():
    all_receipts_number = len(months_list) * len(services_list)
    unpaid_receipt_number = len([x for x in unpaid_receipt if x in services_list])
    assert all_receipts_number == len(paid_receipt) + unpaid_receipt_number


test()
