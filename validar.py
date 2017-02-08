class Validar():
    @staticmethod
    def s_input(message) -> str:
        x = input(message)
        try:
            str(x)
            return x
        except Exception as e:
            print("Error")

    @staticmethod
    def i_input(message) -> int:
        x = input(message)
        try:
            int(x)
            return x
        except Exception as e:
            print("Error")

    @staticmethod
    def v_code(code) -> bool:
        if len(code) > 9:
            return False
        else:
            return True
