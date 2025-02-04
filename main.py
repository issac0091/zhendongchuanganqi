def on_forever():
    if pins.digital_read_pin(DigitalPin.P5) == 0:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
