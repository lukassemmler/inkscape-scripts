# circle((width/2, height/2), 50, fill='#0000%02x', stroke='white')

def rect2D(x, y, width, height, round=None, **kwargs):
    """Shorthand to make creating rects easier
    `rect2D(width/2, height/2, 80, 60, (15, 40), fill='#ffcc00')`
    is equivalent to
    `rect((width/2, height/2), (width/2 + 80, height/2 + 60), (15, 40), fill='#ffcc00')`
    """
    rect((x, y), (x + width, y + height), round, **kwargs)


def createColorRects(colors, *, start_x=0, start_y=0, rect_width=32, rect_height=32, rect_rounding_x=8, rect_rounding_y=8,
                     cols=4, gutter_x=8, gutter_y=8):
    for index, key in enumerate(colors):
        color = colors[key]
        rect_x = start_x + (rect_width + gutter_x) * (index % cols)
        rect_y = start_y + (rect_height + gutter_y) * (index // cols)
        rect2D(rect_x, rect_y, rect_width, rect_height,
               (rect_rounding_x, rect_rounding_y), fill=color)
        #print(index, key, colors[key])


# rect((width/2, height/2), 50, fill='#ffcc00')
# rect((width/2, height/2), (50, 50), 12, fill='#ffcc00')
# rect((width/2, height/2), (width/2 + 80, height/2 + 60), (15, 40), fill='#ffcc00')

colors = {
    "absolute-white": "#ffffff",
    "absolute-black": "#000000",
    "black-blue": "#14111f",
    "strawberry-red": "#cc2844",
    "luminous-red": "#e73232",
    "luminous-orange": "#ff4a26",
    "broom-yellow": "#cf9f00",
    "zinc-yellow": "#f2c714",
    "may-green": "#53892e",
    "sapphire-blue": "#0d4164",
    "turquoise-blue": "#1c838c",
    "rose-red": "#e13464",
    "traffic-purple": "#a4349b",
    "antique-pink": "#ff7f7f",
    "pastel-yellow": "#ffa87c",
    "light-green": "#2cb399",
    "pastel-green": "#7cc17c",
    "pastel-turquoise": "#79bfc4",
    "light-pink": "#f099b1",
    "black-red": "#370014",
    "carmine-red": "#8c1411",
    "signal-orange": "#cf2534",
    "chrome-green": "#273710",
    "yellow-green": "#85891d",
    "red-violet": "#a43459",
    "antique-pink": "#ff8578",
    "dusk-00": "#ffffff",
    "dusk-10": "#f8f9fa",
    "dusk-15": "#f0f2f4",
    "dusk-20": "#e9ecef",
    "dusk-30": "#dee2e6",
    "dusk-40": "#ced4da",
    "dusk-50": "#adb5bd",
    "dusk-60": "#6c757d",
    "dusk-70": "#495057",
    "dusk-80": "#343a40",
    "dusk-90": "#212529",
    "dusk-93": "#1a1d20",
    "dusk-95": "#141618",
    "dusk-97": "#0c0d0e",
    "dusk-100": "#000000",
}
createColorRects(colors)
