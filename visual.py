import pyglet

image = pyglet.image.load('igcboard.jpg') #Test image

window = pyglet.window.Window()

sprite = pyglet.sprite.Sprite(image)

# @window.event
# def on_

def update_image(dt):
  window.clear()
  sprite.draw()
  draw_arrow()


def draw_arrow():
    # TODO: Implement code to draw the arrow.
    pass


pyglet.clock.schedule_interval(update_image, 0.5) #Update time


pyglet.app.run()
