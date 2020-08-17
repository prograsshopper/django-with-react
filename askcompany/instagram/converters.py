class YearConverter:
    # 자주 쓰는 패턴이 있다면 이렇게 커스텀 컨버터를 활용하는 것도 괜찮다.
    regex = r"20\d{2}"
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)


class MonthConverter(YearConverter):
    regex = r"\d{1,2}"


class DayConverter(YearConverter):
    regex = r"[0123]\d"
