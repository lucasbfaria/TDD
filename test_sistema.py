import pytest

from sistema import (
    calcular_valor_consulta,
    Animal,
    consultar_total_gasto_animal,
    validar_valor_servico,
    aplicar_acrescimo_procedimento,
    identificar_retorno,
    calcular_total_gasto_lista,
    filtrar_animais_por_gasto,
    ordenar_animais_por_gasto,
    remover_animais_sem_atendimentos,
    buscar_animal_por_nome,
    somar_faturamento_total_lista,
    ranking_animais_por_total_gasto
)


def test_calcular_valor_consulta_rotina():
    assert calcular_valor_consulta("rotina") == 100

def test_calcular_valor_consulta_urgencia():
    assert calcular_valor_consulta("urgencia") == 180

def test_calcular_valor_consulta_emergencia():
    assert calcular_valor_consulta("emergencia") == 250

def test_acumular_valores_varios_atendimentos():
    animal = Animal("Rex")

    animal.adicionar_atendimento(calcular_valor_consulta("rotina"))
    animal.adicionar_atendimento(calcular_valor_consulta("urgencia"))
    animal.adicionar_atendimento(calcular_valor_consulta("emergencia"))

    assert animal.total_gasto() == 530


def test_consultar_total_gasto_animal_existente():
    animais = [
        Animal("Rex"),
        Animal("Bob")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))
    animais[0].adicionar_atendimento(calcular_valor_consulta("urgencia"))

    assert consultar_total_gasto_animal(animais, "Rex") == 280

def test_aplicar_desconto_fidelidade():
    animal = Animal("Rex")

    for _ in range(5):
        animal.adicionar_atendimento(calcular_valor_consulta("rotina"))

    assert animal.calcular_desconto(100) == 90

def test_nao_aplicar_desconto_sem_fidelidade():
    animal = Animal("Rex")

    for _ in range(4):
        animal.adicionar_atendimento(calcular_valor_consulta("rotina"))

    assert animal.calcular_desconto(100) == 100

def test_calcular_atendimento_com_desconto():
    animal = Animal("Rex")

    for _ in range(5):
        animal.adicionar_atendimento(calcular_valor_consulta("rotina"))

    valor = calcular_valor_consulta("rotina")
    valor_final = animal.calcular_desconto(valor)

    assert valor_final == 90

def test_nao_permitir_valor_servico_zero():
    with pytest.raises(ValueError):
        validar_valor_servico(0)


def test_calcular_valores_decimais():
    assert validar_valor_servico(99.90) == 99.90


def test_nao_permitir_valor_negativo():
    with pytest.raises(ValueError):
        validar_valor_servico(-50)

def test_animal_inexistente_lanca_excecao():
    animais = [
        Animal("Rex"),
        Animal("Bob")
    ]

    with pytest.raises(ValueError):
        consultar_total_gasto_animal(animais, "Thor")

def test_registrar_novo_animal_sem_atendimentos():
    animal = Animal("Thor")

    assert animal.nome == "Thor"
    assert animal.total_gasto() == 0

def test_aplicar_acrescimo_procedimento_adicional():
    valor = calcular_valor_consulta("rotina")

    valor_final = aplicar_acrescimo_procedimento(valor, 20)

    assert valor_final == 120

def test_identificar_retorno_dentro_do_periodo():
    assert identificar_retorno(10, 30) is True
    assert identificar_retorno(40, 30) is False

def test_registrar_varios_animais_em_lista():
    animais = [
        Animal("Rex"),
        Animal("Bob"),
        Animal("Thor")
    ]

    assert len(animais) == 3
    assert animais[0].nome == "Rex"
    assert animais[1].nome == "Bob"
    assert animais[2].nome == "Thor"

def test_calcular_total_gasto_lista_animais():
    animais = [
        Animal("Rex"),
        Animal("Bob")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))
    animais[1].adicionar_atendimento(calcular_valor_consulta("urgencia"))

    assert calcular_total_gasto_lista(animais) == 280

def test_filtrar_animais_com_gasto_acima_de_limite():
    animais = [
        Animal("Rex"),
        Animal("Bob"),
        Animal("Thor")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))
    animais[1].adicionar_atendimento(calcular_valor_consulta("urgencia"))
    animais[2].adicionar_atendimento(calcular_valor_consulta("emergencia"))

    resultado = filtrar_animais_por_gasto(animais, 150)

    assert resultado == [animais[1], animais[2]]

def test_ordenar_animais_por_total_gasto():
    animais = [
        Animal("Rex"),
        Animal("Bob"),
        Animal("Thor")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))
    animais[1].adicionar_atendimento(calcular_valor_consulta("emergencia"))
    animais[2].adicionar_atendimento(calcular_valor_consulta("urgencia"))

    resultado = ordenar_animais_por_gasto(animais)

    assert resultado == [animais[0], animais[2], animais[1]]

def test_remover_animais_sem_atendimentos():
    animais = [
        Animal("Rex"),
        Animal("Bob"),
        Animal("Thor")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))

    resultado = remover_animais_sem_atendimentos(animais)

    assert resultado == [animais[0]]

def test_buscar_animal_por_nome():
    animais = [
        Animal("Rex"),
        Animal("Bob"),
        Animal("Thor")
    ]

    resultado = buscar_animal_por_nome(animais, "Bob")

    assert resultado == animais[1]

def test_somar_faturamento_total_lista():
    animais = [
        Animal("Rex"),
        Animal("Bob")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))
    animais[1].adicionar_atendimento(calcular_valor_consulta("urgencia"))

    assert somar_faturamento_total_lista(animais) == 280

def test_ranking_animais_por_total_gasto():
    animais = [
        Animal("Rex"),
        Animal("Bob"),
        Animal("Thor")
    ]

    animais[0].adicionar_atendimento(calcular_valor_consulta("rotina"))
    animais[1].adicionar_atendimento(calcular_valor_consulta("emergencia"))
    animais[2].adicionar_atendimento(calcular_valor_consulta("urgencia"))

    resultado = ranking_animais_por_total_gasto(animais)

    assert resultado == [animais[1], animais[2], animais[0]]