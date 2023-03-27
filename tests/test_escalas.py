"""
AAA - 3A - A3

Arange - Act - Assert
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_escala_deve_funcionar_com_notas_minusculas() -> None:
    # Arange
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_escala_deve_retornar_erro_que_a_nota_nao_existe() -> None:
    tonica = 'x'
    tonalidade = 'maior'
    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


def test_escala_deve_retornar_erro_que_a_escala_nao_existe() -> None:
    tonica = 'A'
    tonalidade = 'tonalidade'
    mensagem_de_erro = f'Essa escala não existe ou não foi implementada, tente uma dessas {ESCALAS.keys()}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado) -> None:
    resultado = escala(tonica, 'maior')

    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus() -> None:
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
