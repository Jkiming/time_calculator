


# este caso solo es posible cuando no hay valores excedientes que cambien de periodo (AM - PM)
# this case is only possible when there are no excess values that change the period (AM - PM)
def no_exceed_case(hora,minuto,periodo,dia=""):
    if minuto >= 60:
        hora +=1 
        minuto -= 60
    if dia != "":
        return f'{hora}:{minuto} {periodo}, {dia}'
    return f'{hora}:{minuto} {periodo}'

# devuelve el indice de un dia de la semana que fue recibido como parametro
# returns the index of a weekday received as a parameter
def dia_semana(day):
    d_lower = day.lower()
    dl = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    return dl.index(d_lower)

# devuelve el dia de la semana en forma de cadena si este cambia
# returns the weekday as a string if it change
def contador_dia_semana(dia,avance):
    dl = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    indice = dia_semana(dia)
    return dl[indice + avance]


# devuelve el periodo (AM - PM) dependiendo la hora recibida como parametro
# returns the period (AM - PM) depending on the hour received as a parameter
def pm_am(comienzo,duracion,periodo):
    hora, minutos, hour, minutes = map(int, comienzo + duracion)
    hr, hpc, mn = (hora + hour), (hr - hora), (minutos + minutes)

    if mn >= 60:
        hpc += 1 
        mn -= 60
        
    i = hora 
    hc = 1

    while i < hpc:
        print(hc, periodo, i)
        if hc == 11 and periodo == 'AM':
            periodo = 'PM'
            
        elif hc == 11 and periodo == 'PM':
            periodo = 'AM'
        
        i = i + 1
        hc = hc + 1
        if hc == 13:
            hc = 1
    return periodo

# devuelve los dias que pasaron si las horas ascienden una cantidad estimada mayor a 24
# returns the days that have passed if the total hours exceed an estimated amount of 24
def dias(horas,minutos):
    d = 0 
    horas = horas + 1 if minutos >= 60 else horas
    while horas >= 0:
        if horas % 24 == 0:
            d += 1
        horas -= 1
    return d


# devuelve una lista con las horas sin periodo
# returns a list with hours without a period
def splitear(horario):
    return horario.split(' ')


# devuelve una lista dividida entre horas y minutos
# returns a list divided between hours and minutes
def separador(expresion):
    hora = splitear(expresion)
    return hora[0].split(':')

# devuelve la string que contiene el periodo (AM - PM)
# returns the string containing the period (AM - PM)
def indentif_period(horario):
    return splitear(horario)[1]
    

# devuelve la sumatoria entre las horas de (start) y (duration) en variables de hora y minuto
# returns the sum of hours between (start) and (duration) as variables for hour and minute
def calcular(comienzo,duracion):
    hora, minutos, hour, minutes = map(int, comienzo + duracion)
    return (hora + hour), (minutos + minutes)




def add_time(start, duration, day=""):

    
    hora_s, hora_d = separador(start), separador(duration)
    r_periodo = indentif_period(start)
    r_hora, r_minuto = calcular(hora_s, hora_d)
    #f_periodo = pm_am(hora_s,hora_d,r_periodo)
    
    # caso donde la suma no excede las 12 hs y se mantiene en el mismo periodo
    new_time = no_exceed_case(r_hora, r_minuto, r_periodo, day)
    return new_time
