# Some useful constants for describing pins
GPIOA = 'GPIOA'
GPIOB = 'GPIOB'
GPIOC = 'GPIOC'

# GPIO/FGPIO register bits assignment
MKE04Z_GPIOA = {
    0:  ('PTA0'),  1:  ('PTA1'),
    2:  ('PTA2'),  3:  ('PTA3'),
    4:  ('PTA4'),  5:  ('PTA5'),
    6:  ('PTA6'),  7:  ('PTA7'),
    8:  ('PTB0'),  9:  ('PTB1'),
    10: ('PTB2'),  11: ('PTB3'),
    12: ('PTB4'),  13: ('PTB5'),
    14: ('PTB8'),  15: ('PTB7'),
    16: ('PTC0'),  17: ('PTC1'),
    18: ('PTC2'),  19: ('PTC3'),
    20: ('PTC4'),  21: ('PTC5'),
    22: ('PTC8'),  23: ('PTC7'),
    24: ('PTD0'),  25: ('PTD1'),
    26: ('PTD2'),  27: ('PTD3'),
    28: ('PTD4'),  29: ('PTD5'),
    30: ('PTD6'),  31: ('PTD7'),
    }

MKE04Z_GPIOB = {
    0:  ('PTE0'),  1:  ('PTE1'),
    2:  ('PTE2'),  3:  ('PTE3'),
    4:  ('PTE4'),  5:  ('PTE5'),
    6:  ('PTE6'),  7:  ('PTE7'),
    8:  ('PTF0'),  9:  ('PTF1'),
    10: ('PTF2'),  11: ('PTF3'),
    12: ('PTF4'),  13: ('PTF5'),
    14: ('PTF8'),  15: ('PTF7'),
    16: ('PTG0'),  17: ('PTG1'),
    18: ('PTG2'),  19: ('PTG3'),
    20: ('PTG4'),  21: ('PTG5'),
    22: ('PTG8'),  23: ('PTG7'),
    24: ('PTH0'),  25: ('PTH1'),
    26: ('PTH2'),  27: ('PTH3'),
    28: ('PTH4'),  29: ('PTH5'),
    30: ('PTH6'),  31: ('PTH7'),
    }

MKE04Z_GPIOC = {
    0:  ('PTI0'),  1:  ('PTI1'),
    2:  ('PTI2'),  3:  ('PTI3'),
    4:  ('PTI4'),  5:  ('PTI5'),
    6:  ('PTI6'),  7:  ('PTI7'),
    8:  ('Reserved'),  9:  ('Reserved'),
    10: ('Reserved'),  11: ('Reserved'),
    12: ('Reserved'),  13: ('Reserved'),
    14: ('Reserved'),  15: ('Reserved'),
    16: ('Reserved'),  17: ('Reserved'),
    18: ('Reserved'),  19: ('Reserved'),
    20: ('Reserved'),  21: ('Reserved'),
    22: ('Reserved'),  23: ('Reserved'),
    24: ('Reserved'),  25: ('Reserved'),
    26: ('Reserved'),  27: ('Reserved'),
    28: ('Reserved'),  29: ('Reserved'),
    30: ('Reserved'),  31: ('Reserved'),
    }


def show(GPIO_n):
    if GPIO_n == 'GPIOA':
        prefix = 'A'
        MKE04Z_GPIO_n = MKE04Z_GPIOA
    if GPIO_n == 'GPIOB':
        prefix = 'B'
        MKE04Z_GPIO_n = MKE04Z_GPIOB
    if GPIO_n == 'GPIOC':
        prefix = 'C'
        MKE04Z_GPIO_n = MKE04Z_GPIOC
    for i in range(32):
        print(prefix+str(i), MKE04Z_GPIO_n[i])
