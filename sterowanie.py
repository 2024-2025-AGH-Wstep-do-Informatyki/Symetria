import POU

# Prędkość ruchu
step = 10
t = pou
# Flagi do sprawdzania, czy klawisz jest wciśnięty
is_left_pressed = False
is_right_pressed = False

# Funkcje do poruszania żółwiem
def move_left():
    global is_left_pressed
    is_left_pressed = True
    move()  # Rozpoczynaj ruch od razu, gdy klawisz zostanie wciśnięty

def move_right():
    global is_right_pressed
    is_right_pressed = True
    move()  # Rozpoczynaj ruch od razu, gdy klawisz zostanie wciśnięty

def stop_left():
    global is_left_pressed
    is_left_pressed = False

def stop_right():
    global is_right_pressed
    is_right_pressed = False

# Funkcja wykonująca ruch żółwia
def move():
    if is_left_pressed:
        t.setheading(180)  # Ustawienie kierunku na lewo
        t.forward(step)
        screen.ontimer(move, 50)  # Powtarzaj co 50ms, aż klawisz będzie wciśnięty
    elif is_right_pressed:
        t.setheading(0)  # Ustawienie kierunku na prawo
        t.forward(step)
        screen.ontimer(move, 50)  # Powtarzaj co 50ms, aż klawisz będzie wciśnięty

# Mapowanie przycisków na funkcje
screen.listen()  # Nasłuchiwanie naciśnięć klawiszy
screen.onkey(move_left, "Left")  # Strzałka w lewo
screen.onkey(move_right, "Right")  # Strzałka w prawo
screen.onkey(move_left, "a")  # Klawisz "a"
screen.onkey(move_right, "d")  # Klawisz "d"

# Zatrzymywanie ruchu po zwolnieniu klawisza
screen.onkey(stop_left, "KeyRelease_Left")  # Zatrzymaj, gdy klawisz lewy jest zwolniony
screen.onkey(stop_right, "KeyRelease_Right")  # Zatrzymaj, gdy klawisz prawy jest zwolniony
screen.onkey(stop_left, "KeyRelease_a")  # Zatrzymaj, gdy "a" jest zwolnione
screen.onkey(stop_right, "KeyRelease_d")  # Zatrzymaj, gdy "d" jest zwolnione

#pull request

