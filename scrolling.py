from interstate75 import Interstate75, DISPLAY_INTERSTATE75_32X32
import time

i75 = Interstate75(display=Interstate75.DISPLAY_INTERSTATE75_32X32, panel_type=Interstate75.PANEL_FM6126A)
graphics = i75.display

width = i75.width
height = i75.height

RED = graphics.create_pen(255, 0, 0)
PURPLE = graphics.create_pen(255, 0, 255)
BLACK = graphics.create_pen(0, 0, 0)
GREEN = graphics.create_pen(0, 255, 0)
ORANGE = graphics.create_pen(255, 125, 0)
XX = graphics.create_pen(255, 125, 0)
PINK = graphics.create_pen(180, 100, 100)
MINT = graphics.create_pen(80, 180, 100)


X = graphics.create_pen(255, 95, 0)

BLUE = graphics.create_pen(0, 0, 255)


def text(content, color, left, down, fontsize):
    graphics.set_pen(color)
    graphics.text(content, left, down, False, fontsize)

def clear_screen():
    graphics.set_pen(BLACK)
    graphics.clear()
    i75.update()

def scroll_marquee(text_content, color, fontsize, scroll_speed, y_position):
    # Replace spaces with No-Break Space character
    text_content = text_content.replace(' ', '\u00A0')

    text_width = len(text_content) * fontsize * 6  # Approximate text width
    x_position = width  # Start off the right edge of the display

    while True:
        clear_screen()
        text(text_content, color, x_position, y_position, fontsize)
        
        x_position -= 1  # Move the text one pixel to the left

        # If the text has scrolled completely off the left edge, reset its position
        if x_position + text_width < 0:
            x_position = width

        i75.update()
        time.sleep(scroll_speed)


def main():
    clear_screen()
    scroll_marquee('<3 happy halloween!!!!!!!!!!!!', X, 6, 0.02, -6)


if __name__ == "__main__":
    main()