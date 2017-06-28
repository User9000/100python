import pyglet 

win = pyglet.window.Window(width=650, height=490)

label = pyglet.text.Label("Hello world", font_name='Consolas',font_size=36,x=win.width//2, y=win.height//2, anchor_x='center', anchor_y='center')

@win.event
def on_draw():
    win.clear()
    label.draw()
  
    
pyglet.app.run()

