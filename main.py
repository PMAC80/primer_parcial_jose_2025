from controller.cliente_controller import ClienteController
from view.app_gui import AppGUI

if __name__ == "__main__":
    controlador = ClienteController()
    app = AppGUI(controlador)
    app.mainloop()