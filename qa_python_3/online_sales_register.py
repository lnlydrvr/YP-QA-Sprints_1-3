import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            elif name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__name_items.append(name)
                self.__number_items += 1
        
        except ValueError as ve:
            print(ve)
        
        except NameError as ne:
            print(ne)
            
    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            else:
                self.__name_items.remove(name)
                self.__number_items -= 1
        
        except NameError as ne:
            print(ne)
            
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return total_sum
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        
        total = []                
        for item in twenty_percent_tax:
            total.append(self.__item_price[item])
        
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        
        total_twenty_percent_taxes = total_sum * 0.2
        return total_twenty_percent_taxes
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
        
        total = []
        for item in ten_percent_tax:
            total.append(self.__item_price[item])
            
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        
        total_ten_percent_taxes = total_sum * 0.1
        return total_ten_percent_taxes
    
    def total_tax(self):
        total_taxes = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total_taxes
    
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if not isinstance(telephone_number, int):
                raise ValueError('Необходимо ввести цифры')
            elif len(str(telephone_number)) > 10:     # Есть мысль, что нужно использовать != вместо >, но в задании указана именно такая проверка
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            else:
                return f"+7{telephone_number}"
            
        except ValueError as ve:
            print(ve)
    
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda h: h.hour],
            ['минуты', lambda m: m.minute],
            ['день', lambda D: D.day],
            ['месяц', lambda M: M.month],
            ['год', lambda Y: Y.year]
        ]
        
        for name, func in date:
            date_and_time.append(f"{name}: {func(now)}")
            
        return date_and_time
    
print(OnlineSalesRegisterCollector.get_date_and_time())