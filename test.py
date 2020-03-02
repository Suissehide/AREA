#!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))

def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
    
    #!/usr/bin/env python3

from math import sqrt


def calc_rsi(h, b):
    rsi = (h / (h + b)) * 100
    if rsi == 0 or rsi == 100:
        return 50
    return rsi#100 - (100/(1 + (h/b)))


def calc_candle_volume(open_position, close_position):
    volume = close_position - open_position
    if volume < 0:
        volume = volume * -1
    return volume


def calc_mobile_average(values, devise):
    total = 0
    i = 0
    evo = 0
    if len(values) == 0:
        return (1)
    while i < len(values) - 1: #len -1
        if devise == "BTC":
            evo = float(values[i + 1][1]) - float(values[i][1])
        elif devise == "ETH":
            evo = float(values[i + 1][3]) - float(values[i][3])
        elif devise == "other":
            evo = float(values[i + 1][5]) - float(values[i][5])
        if evo < 0:
            evo = 0
        total += evo
        i += 1
    return total / len(values)


def calculate_evo(valueList, period, last_input_poped):
    lastValue = float(valueList[len(valueList) - 1][1])

    if len(valueList) == period and len(last_input_poped) != 0:
        return int(round(((lastValue - float(last_input_poped[0][1])) / float(last_input_poped[0][1])) * 100))
    return "nan"


def calculate_standard_deviation(valueList, period):
    mean = 0
    variance = 0
    if len(valueList) == period:
        for elem in valueList:
            mean = mean + elem
        mean = mean / period
        for elem in valueList:
            variance = variance + (elem - mean) ** 2
        return "%.2f" % sqrt(variance / period)
    return "nan"


def get_rsi(candle_list):
    h = []
    b = []
    _open = 0
    _close = 0
    if len(candle_list) == 0:
        return(50)
    for candle in candle_list:
        _open = float(candle[0])
        _close = float (candle[1])
        if _open > _close:
            b.append(calc_candle_volume(_open, _close))
        else:
            h.append(calc_candle_volume(_open, _close))
    return calc_rsi(calc_mobile_average(h, "BTC"), calc_mobile_average(b, "BTC"))
