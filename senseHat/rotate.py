from sense_hat import SenseHat

sense = SenseHat()
sense.flip_h()
# sense.set_rotation(180)
# alternatives
# sense.rotation = 180

blue = (0, 0, 255)
yellow = (255, 255, 0)

while True:
  sense.show_message("Astro Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)
