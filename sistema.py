def calcular_valor_consulta(tipo):
    if tipo == "rotina":
        return 100
    elif tipo == "urgencia":
        return 180
    elif tipo == "emergencia":
        return 250


def validar_valor_servico(valor):
    if valor <= 0:
        raise ValueError("O valor do serviço deve ser maior que zero")

    return valor


class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.atendimentos = []

    def adicionar_atendimento(self, valor):
        validar_valor_servico(valor)
        self.atendimentos.append(valor)

    def total_gasto(self):
        return sum(self.atendimentos)

    def calcular_desconto(self, valor):
        if len(self.atendimentos) >= 5:
            return valor * 0.9

        return valor


def consultar_total_gasto_animal(animais, nome):
    animal = buscar_animal_por_nome(animais, nome)
    return animal.total_gasto()


def aplicar_acrescimo_procedimento(valor, percentual):
    return valor + (valor * percentual / 100)


def identificar_retorno(dias, periodo):
    return dias <= periodo


def calcular_total_gasto_lista(animais):
    return sum(animal.total_gasto() for animal in animais)


def filtrar_animais_por_gasto(animais, limite):
    return [
        animal for animal in animais
        if animal.total_gasto() > limite
    ]


def ordenar_animais_por_gasto(animais):
    return sorted(
        animais,
        key=lambda animal: animal.total_gasto()
    )


def remover_animais_sem_atendimentos(animais):
    return [
        animal for animal in animais
        if len(animal.atendimentos) > 0
    ]


def buscar_animal_por_nome(animais, nome):
    for animal in animais:
        if animal.nome == nome:
            return animal

    raise ValueError("Animal não encontrado")


def somar_faturamento_total_lista(animais):
    return calcular_total_gasto_lista(animais)


def ranking_animais_por_total_gasto(animais):
    return sorted(
        animais,
        key=lambda animal: animal.total_gasto(),
        reverse=True
    )