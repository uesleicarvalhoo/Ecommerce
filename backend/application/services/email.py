from backend.application.contracts import Client, Order, Streamer, Token


class EmailService:
    def __init__(self, streamer: Streamer) -> None:
        self.streamer = streamer

    def send_new_order_email(self, client: Client, order: Order) -> None:
        self.streamer.send_email(title=f"Pedido #{order.id}", to=client.email, content="Pedido realizado com sucesso!")

    def send_recovery_password_email(self, client: Client, recovery_token: Token) -> None:
        self.streamer.send_email(
            tilte="Recuperação de senha",
            to=client.email,
            content=f"Para recuperar o seu email, use o Token {recovery_token.acess_token}: ",
        )
