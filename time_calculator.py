def swap_denotation(den,dias):
    denotation = "PM" if den == "AM" else "AM"
    dias += 1 if denotation == "AM" else 0
    return denotation, dias


def get_days_difference(days):

    if not days:
        return ""
    
    if days == 1:
        return " (next day)"
    
    return f' ({days} days later)'



def sum_minutes(hours, minutes, sum_minutes):
    minutes += sum_minutes
    hours += 1 if minutes >= 60 else 0 
    minutes %= 60

    return hours, minutes


def get_weekdays(dias_para_sumar, dia_semana=""):
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if dia_semana == "":
        return ""
    dia_actual_indice = weekdays.index(dia_semana.capitalize())
    dia_sumado_indice = (dia_actual_indice + dias_para_sumar) % 7
     
    return f", {weekdays[dia_sumado_indice]}"
    
    

def sum_hours(hours,sum_hours):
    hours += sum_hours
    days = int(hours/24)
    hours %= 24 
    den_swap = hours >= 12 
    hours %= 12
    
    return hours if hours != 0 else 12, days, den_swap


def splitear(horario):
    horario_split = horario.split(' ')
    horas, minutos = horario_split[0].split(':')
    
    return int(horas), int(minutos), "" if len(horario_split) == 1 else horario_split[1]


def add_time(start, duration, day=""):

    hours, minutes, den = splitear(start)
    dur_hours, den_minutes, _ = splitear(duration)
    hours, minutes = sum_minutes(hours,minutes,den_minutes)
    hours, dias, den_swap = sum_hours(hours,dur_hours)
    
    if den_swap:
        den, dias = swap_denotation(den, dias)
        
    return f"{hours}:{minutes:02d} {den}{get_weekdays(dias,day)}{get_days_difference(dias)}"
