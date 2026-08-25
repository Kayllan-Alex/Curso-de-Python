from hashlib import sha256
from rich.panel import Panel
from rich.align import Align
from rich import print
from random import randint
from pwinput import pwinput


class ContaBancaria:
    def __init__(
        self,
        titular: str | None = None,
        saldo_bancario: float = 0.0,
        senha: str | None = None,
    ) -> None:
        self._id: str = str(randint(100000, 999999))
        self._titular: str | None = titular
        self.__saldo: float = saldo_bancario
        self.__pwhash: str
        if senha is None:
            while True:
                senha_digitada = pwinput("Digite uma senha com 8 ou mais digitos: ")

                if len(senha_digitada) >= 8:
                    self.__pwhash = sha256(senha_digitada.encode("utf-8")).hexdigest()
                    break

                print("A senha deve possuir pelo menos 8 dígitos.")
        else:
            self.__pwhash = sha256(senha.encode("utf-8")).hexdigest()
        print(self.painel_de_sucesso("Parabéns, sua conta foi criada!"))

    def verificar_senha(self) -> bool:
        senha_digitada = pwinput("Digite sua senha: ")
        if len(senha_digitada) < 8:
            print("Senha incorreta!")
            return False
        return sha256(senha_digitada.encode("utf-8")).hexdigest() == self.__pwhash

    def painel_de_erro(self, conteudo: str) -> Panel:
        return Panel(
            Align.center(conteudo),
            title=f"[bold red]ERROR[/] by user < [bold]{self._id}[/] >",
            width=80,
        )

    def painel_de_sucesso(self, conteudo: str) -> Panel:
        return Panel(
            Align.center(conteudo),
            title=f"[bold green]SUCCESS[/] action by user < [bold]{self._id}[/] >",
            width=80,
        )

    def sacar_dinheiro(self, valor: float = 0.0) -> Panel:
        valor = abs(valor)
        if valor == 0:
            return self.painel_de_erro(
                f"Não é possível sacar [bold green]R${valor:,.2f}[/]"
            )
        if self.verificar_senha():
            if valor > self.__saldo:
                return self.painel_de_erro(
                    f"Ocorreu um erro ao sacar o saldo desejado.\n"
                    f"você não pode sacar [bold green]R${valor:,.2f}[/] pois o seu saldo consta [bold green]R${self.__saldo:,.2f}"
                )
            self.__saldo -= valor
            return self.painel_de_sucesso(
                f"A sua ação foi aceita! Você acabou de sacar [bold green]R${valor:,.2f}[/]\n"
                f"Restando agora na sua conta [bold green]R${self.__saldo:,.2f}"
            )
        return self.painel_de_erro("A sua senha está INCORRETA!")

    def depositar(self, valor: float = 0.0) -> Panel:
        valor = abs(valor)
        if valor == 0:
            return self.painel_de_erro(
                f"Não é possível depositar [bold green]R${valor:,.2f}[/]"
            )
        if self.verificar_senha():
            self.__saldo += valor
            return self.painel_de_sucesso(
                f"A sua ação foi aceita ! Você acabou de depositar [bold green]R${valor:,.2f}[/]\n"
                f"Agora sua conta possui o total de [bold green]R${self.__saldo:,.2f}"
            )

        return self.painel_de_erro("A sua senha está INCORRETA!")

    def verificar_conta(self) -> Panel:
        return Panel(
            Align.center(
                f"A conta cujo o titular se chama: [bold purple]{self._titular}[/]\n"
                f"Com um Identificador numérico: [bold blue]{self._id}[/]\n"
                f"Tem um saldo bancario no total de: [bold green]R${self.__saldo:,.2f}[/]"
            ),
            title=f"Action by user < [bold]{self._id}[/] >",
            width=80,
        )
