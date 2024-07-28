class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")

class ExtendedCase(Case):
    def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
        super().__init__(test_case_id, name, step_description, expected_result)
        self.precondition = precondition
        self.environment = environment
        
        
    def print_test_case_info(self):
        super().print_test_case_info()
        print(f"Предусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")
        
case = ExtendedCase(test_case_id = 1,
                    name = 'Наличие кнопки Принять',
                    step_description = '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ',
                    expected_result = 'Кнопка доступна',
                    precondition = 'Открыть сервис',
                    environment = 'Яндекс Браузер')

case.print_test_case_info()       