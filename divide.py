def divide(a, b):
    try:
        result = a/float(b)
        return result
    except ZeroDivisionError:
        print("'0' a bölünme hatası")