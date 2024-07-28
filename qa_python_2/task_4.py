class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    def get_hours(cls):
        hours = cls.hours
        if hours is None:
            hours = (7 - cls.rest_days) * 8
        return cls(cls.name, hours, cls.rest_days, cls.email)
    
    def get_email(cls):
        email = cls.email
        if email is None:
            email = f"{cls.name}@email.com"
        return cls(cls.name, cls.hours, cls.rest_days, email)

    def set_hourly_payment(cls, new_hourly_payment):
        new_hourly_payment = 450
        cls.hourly_payment = new_hourly_payment

    def salary(cls):
        return cls.hours * cls.hourly_payment
