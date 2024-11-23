from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def msg(ctx, mess):
        """
        mostra a mesg enviada do client
        """
        return f"alguma coisa {mess}"

application = Application(
    [HelloWorldService],
    tns="spyne.examples.text_service",
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == "__main__":
    server = make_server('0.0.0.0', 8080, WsgiApplication(application))
    print("SOAP server running...")
    server.serve_forever()
