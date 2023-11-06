from flexx import flx


class ExemploFlexx(flx.Widget):
    def init(self):
        flx.Button(text="Olá")
        flx.Button(text="World!")


if __name__ == "__main__":
    a = flx.App(ExemploFlexx, title="Flexx demonstração")
    m = a.launch()
    flx.run()
