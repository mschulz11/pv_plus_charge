
class test_connection:
    def __init__(self):

        from pymodbus.client import ModbusTcpClient
        from pymodbus.constants import Endian
        from pymodbus.payload import BinaryPayloadDecoder
        from pymodbus.payload import BinaryPayloadBuilder


        self.inverter_ip="192.168.178.39"
        self.inverter_port="1502"  

        client = ModbusTcpClient(host=self.inverter_ip,port=self.inverter_port)
        client.connect()

        r1=client.read_holding_registers(108,2,slave=71)
        FloatRegister = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Little)
        result_FloatRegister =round(FloatRegister.decode_32bit_float(),2)
       

        print("Home own consumption from grid:")
        print(result_FloatRegister)

        client.close()


if __name__ == "__main__":
    try:
        Kostalquery = test_connection()
    except Exception as Badmain:
        print ("Ran into error executing Main kostal-RESTAPI Routine :", Badmain)                




# Stromstärke setzen!
# http://192.168.178.73/api/set?amp=16