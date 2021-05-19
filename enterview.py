from datetime import date, timedelta


def DiaSemana(data_array):
    """
    - data recebe uma instância do tipo datetime.date
    - e retorna uma str
    """
    week_days = {
        0: "SEGUNDA",
        1: "TERÇA",
        2: "QUARTA",
        3: "QUINTA",
        4: "SEXTA",
        5: "SABADO",
        6: "DOMINGO",
    }
    week_day = data_array.weekday()
    return week_days[week_day]


def soma_dias(data, dias):
    """
    - data recebe um valor str no formato ("dd/mm/aaaa")
    - dias recebe um valor int
    - a função retorna uma instância de um objeto datetime.date
    """
    data = list(map(int, data.split("/")))

    data_array = date(
        day=data[0],
        month=data[1],
        year=data[2]
    )

    weekend_days = 0
    for dia in range(dias):
        tomorrow = DiaSemana(data_array + timedelta(days=dia+1))
        if tomorrow == "SABADO" or tomorrow == "DOMINGO":
            weekend_days += 1
    data_final = data_array + timedelta(days=dias)
    if weekend_days != 0:
        soma_dias(
            f"{data_final.day}/{data_final.month}/{data_final.year}",
            weekend_days
        )

    else:
        print(data_final)


soma_dias("19/05/2021", 4)
