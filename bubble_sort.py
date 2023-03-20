import pygame
import random
import sys
import pygame_widgets as pw
from pygame_widgets.button import Button
from itertools import count
import tkinter as tk
import time

pygame.init()

win = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Bubble Sort")

x = 40

width = 10

heights = [i * 10 for i in range(1, 78)]

random.shuffle(heights)


PURPLE = (255, 0, 255)

AQUA = (0, 255, 255)

BLACK = (0, 0, 0)


sort_button = Button(
    win,
    20,
    20,
    100,
    50,
    text="Sort",
    fontSize=50,
    textColour=PURPLE,
    margin=20,
    inactiveColour=BLACK,
    pressedColour=BLACK,
    radius=20,
    onRelease=lambda: sort(heights),
)


quit_button = Button(
    win,
    1470,
    20,
    100,
    50,
    text="Quit",
    fontSize=50,
    textColour=PURPLE,
    margin=20,
    inactiveColour=BLACK,
    pressedColour=BLACK,
    radius=20,
    onRelease=lambda: force_quit(),
)


def speed_input():
    root = tk.Tk()

    root.title("Choose Speed")

    root.geometry("300x100")

    root.eval("tk::PlaceWindow . center")

    root.resizable(False, False)

    root.configure(background="black")

    def input_fast():
        root.destroy()
        time.sleep(0.5)
        bubble_sort_fast()

    def input_slow():
        root.destroy()
        time.sleep(0.5)
        bubble_sort_slow()

    button_fast = tk.Button(
        root,
        height=2,
        width=12,
        text="Fast",
        command=lambda: input_fast(),
        font=(30),
        fg="purple",
        bg="black",
        borderwidth=0,
        activebackground="grey",
    )

    button_fast.grid(column=0, row=0, padx=16, pady=20)

    button_slow = tk.Button(
        root,
        height=2,
        width=12,
        text="Slow",
        command=lambda: input_slow(),
        font=(30),
        fg=("purple"),
        bg="black",
        borderwidth=0,
        activebackground="grey",
    )

    button_slow.grid(column=1, row=0, padx=16, pady=20)

    tk.mainloop()


def counter(count=count(1)):
    return next(count)


def display_heights(heights):

    for i in range(len(heights)):

        pygame.draw.rect(win, AQUA, (x + 20 * i, (900 - heights[i]), width, heights[i]))


def change_color(heights, index1, index2):

    for i in range(len(heights)):

        if i == index1:
            pygame.draw.rect(
                win,
                PURPLE,
                (x + 20 * index1, (900 - heights[index1]), width, heights[index1]),
            )
            pygame.draw.rect(
                win,
                PURPLE,
                (
                    x + 20 * index2,
                    (900 - heights[index2]),
                    width,
                    heights[index2],
                ),
            )
            pygame.display.update()


def bubble_sort_fast():

    for i in range(len(heights) - 1):

        swapped = False

        for j in range(len(heights) - i - 1):

            if heights[j] > heights[j + 1]:

                heights[j], heights[j + 1] = heights[j + 1], heights[j]

                swapped = True

            win.fill((0, 0, 0))

            display_heights(heights)

            change_color(heights, j, j + 1)

        if not swapped:
            break


def bubble_sort_slow():

    for i in range(len(heights) - 1):

        swapped = False

        for j in range(len(heights) - i - 1):

            if heights[j] > heights[j + 1]:

                heights[j], heights[j + 1] = heights[j + 1], heights[j]

                swapped = True

            win.fill((0, 0, 0))

            display_heights(heights)

            change_color(heights, j, j + 1)

            pygame.time.delay(10)

        if not swapped:
            break


def sort(heights):

    counter()

    if counter() - 1 == 1:
        speed_input()

    else:
        random.shuffle(heights)
        speed_input()


def main():
    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_q]:
            run = False

        win.fill((0, 0, 0))

        display_heights(heights)

        pw.update(event)

        sort_button.listen(event)

        sort_button.draw()

        quit_button.listen(event)

        quit_button.draw()

        pygame.display.update()

    force_quit()
   
def force_quit():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
