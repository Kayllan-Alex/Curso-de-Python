from abc import ABC


class Pessoa(ABC):
    def __init__(
        self,
        nome: str | None = None,
        nascimento: int = 0,
    ) -> None:
        super().__init__()
        self._nome: str | None = nome
        if abs(nascimento) < 1900 or abs(nascimento) > 2026:
            raise ValueError("Digite um ano de nascimento válido.")
        else:
            self._nascimento: int = nascimento
            self._idade: int = 2026 - abs(nascimento)

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, novo_nascimento: int = 0) -> None:
        novo_nascimento = abs(novo_nascimento)
        if novo_nascimento < 1900 or novo_nascimento > 2026:
            raise ValueError("Digite um ano de nascimento válido.")
        self._nascimento = novo_nascimento
        self._idade = 2026 - novo_nascimento


class Aluno(Pessoa):
    def __init__(
        self, nome: str | None = None, nascimento: int = 0, curso: str | None = None
    ) -> None:
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
        if curso not in self.cursos_oficiais:
            raise ValueError("Esse curso não está na lista.")
        else:
            self._curso: str | None = curso

    @property
    def curso(self) -> str | None:
        return self._curso

    @curso.setter
    def curso(self, troca_do_curso: str | None = None) -> None:
        if troca_do_curso is None:
            raise ValueError("Digite um curso com 3 letras.")
        troca_do_curso = troca_do_curso.upper()
        if len(troca_do_curso) < 3 or len(troca_do_curso) > 3:
            raise ValueError("Digite apenas 3 caracteres do curso.")
        if troca_do_curso not in self.cursos_oficiais:
            raise ValueError("Esse curso não existe!")
        self._curso = troca_do_curso

    def add_curso(self, curso_desejado: str | None = None) -> None:
        if curso_desejado is None:
            raise ValueError("Digite um curso com 3 letras.")
        curso_desejado = curso_desejado.upper()
        if len(curso_desejado) < 3 or len(curso_desejado) > 3:
            raise ValueError("Digite apenas 3 caracteres do curso.")
        if curso_desejado in self.cursos_oficiais:
            raise ValueError("Esse curso já existe!")
        self.cursos_oficiais.append(curso_desejado)
