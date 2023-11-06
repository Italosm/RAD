import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class PyFormsExample(BaseWidget):
    def __init__(self):
        super(PyFormsExample, self).__init__("PyFormsExample")

        # Definition of the forms fields
        self._firstname = ControlText("Nome", "Default value")
        self._lastname = ControlText("Sobrenome")
        self._fullname = ControlText("Nome completo")
        self._button = ControlButton("Pressione o Botão")
        # define a ação do botão
        self._button.value = self.__buttonAction

    def __buttonAction(self):
        """Button action event"""
        self._fullname.value = self._firstname.value
        +" "
        +self._lastname.value


if __name__ == "__main__":
    pyforms.start_app(PyFormsExample)
