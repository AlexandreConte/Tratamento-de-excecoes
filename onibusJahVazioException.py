class OnibusJahVazioException(Exception):
    def __init__(self) -> None:
        super().__init__("O onibus jah esta vazio!")
