format_dic = {
    'ymd':'{0.year}{0.mon}{0.day}'
}


class Date:
    def __init__(self,day,mon,year):
        self.day = day
        self.mon = mon
        self.year = year

    def __format__(self, format_spec):
        print("我执行了")
        print('---->',format_spec)
        if not format_spec or format_spec not in format_dic:
            format_spec='ymd'
        fm = format_dic[format_spec]
        return fm.format(self)

d1=Date(26,12,2016)
format(d1)
print(format(d1,'ymd'))