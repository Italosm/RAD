import platform
import sys


def main():
    check_versions()
    sys.excepthook = (
        cef.ExceptHook
    )  # Para encerrar todos os processos do CEF em caso de erro
    cef.Initialize()
    cef.CreateBrowserSync(
        url="https://www.google.com/",
        window_title="Olá, mundo! Este é o primeiro exemplo do CEF Python",
    )
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print(
        "[hello_world.py] Python {ver} {arch}".format(
            ver=platform.python_version(), arch=platform.architecture()[0]
        )
    )
    assert (
        cef.__version__ >= "57.0"
    ), "CEF Python v57.0+ é necessário para executar este script."


if __name__ == "__main__":
    if sys.version_info.major == 3 and sys.version_info.minor == 6:
        from cefpython3 import cefpython as cef

        main()
    else:
        print(
            "Por favor instale a versão 3.6.15 do python! (Ou uma versão compatível com o cefpython3)"
        )
