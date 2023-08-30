import arrow


# 时间日期操作
class DateTimeLib(object):

    @property
    def date(self):
        return str(arrow.now('+08:00').date())

    # 返回日期和时间属性
    @property
    def datetime(self):
        return str(arrow.now('+08:00').datetime).split('.')[0]

    # 返回日期和时间函数
    @staticmethod
    def method_datetime():
        return str(arrow.now('+08:00').datetime).split('.')[0]


dt = DateTimeLib()
