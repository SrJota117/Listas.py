# Programa que valida uma data
def data_valida(dia, mes, ano):
    try:
        import datetime
        datetime.datetime(ano, mes, dia)
        return True
    except:
        return False
