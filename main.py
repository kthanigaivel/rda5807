from machine import Pin, I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

I2C_SEQ = 0x10
I2C_REG = 0x11

reg = memoryview(bytearray(b'\xf0\x03\x00\x00\x0a\x00\x88\x8f\x00\x00\x42\x02'))#2h,2l,3h,3l,4h,4l,5h,5l,6h,6l,7h,7l register high and low bytes


def _channel(value):
    assert 87 <= value <= 108
    channel = int(((value*1000) - 87000) // 100)
    reg[2:4] = bytearray([channel >> 2, ((channel << 6) & 0xc0) | 0x10])
        
i2c.writeto(I2C_SEQ,reg)
_channel(102.5)
reg[0]=0xf0
reg[1]=0x01
i2c.writeto(I2C_SEQ,reg)

for y in range(2,16):
    data=i2c.readfrom_mem(I2C_REG, y,2)
    print(hex(y)," ".join(hex(n) for n in data))