class Date:
    def __init__(self, month):
        self.inner_month = month

    @property
    def month(self):
        return self.inner_month

    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month
        else:
            print(Exception("허용 범위 초과"))

today = Date(8)
today.month = 15
print(today.month)
