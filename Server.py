class Server:

    @staticmethod
    def test(fo):
        return fo

    def getCPUtemp():
        temp = subprocess.check_output("sensors | grep 'Core 1'", shell=True)[17:21]
        return dict(temperature=temp)
