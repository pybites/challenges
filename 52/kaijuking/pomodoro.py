from datetime import datetime, timedelta
import PySimpleGUI as sg


def pomodoro_gui():
    # Setup initial variables
    button_width = 10
    button_height = 2
    default_start = 10
    default_time_text = f"00:00:00"
    default_error_msg = "Please enter a valid number. Min = 1, Max = 120"
    default_break = 30
    now = None
    future_time = None
    timer_running = False
    

    input_layout = [[sg.Text("Enter Minutes:"), sg.InputText(f"{default_start}", key='-INPUT-')]]


    action_buttons = [
    sg.Button('Start', size=(button_width,button_height), key="-START-"),
    sg.Button('Stop', size=(button_width,button_height), key="-STOP-"),
    sg.Button('Break Time', size=(button_width,button_height), key="-BREAK-"),
    sg.Button('Exit', size=(button_width,button_height), key="-EXIT-")]


    frame_layout = [
        [sg.Text(text=f'{default_time_text}', justification="center", key="-TIME-", auto_size_text=True, expand_x=True, expand_y=True, font=("Arial", 75))]
    ]


    layout = [
        input_layout,
        [sg.Frame('Time Remaining', frame_layout, font='Any 12', title_color='blue', size=(600,150), element_justification='center')],
        action_buttons

    ]

    # Create the window
    window = sg.Window("PyBites Code Challenge #52: Pomodoro Timer", layout, resizable=False, finalize=True, element_justification='center')


    def disable_button_state(button_list: list, is_disabled: bool):
        for button in button_list:
            window[f"{button}"].update(disabled=is_disabled)
            window.refresh()


    def set_time_element_text_value(txt_value: str):
        window["-TIME-"].update(f"{txt_value}")

    
    def process_user_input(user_input: str):
        if not user_input.isdigit():
            return False
        elif not (int(user_input) > 0 and int(user_input) <= 120):
            return False
        else:
            return True


    while True:
        event, values = window.read(timeout=10)
        #set_button_state(['-STOP-', '-BREAK-'], True)
        
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break

        if event == "-STOP-":
            # Disable the timer 
            timer_running = False

            # Update the text elment's value and enable the appropriate buttons
            disable_button_state(['-START-', '-BREAK-'], False)
            set_time_element_text_value(default_time_text)

            # Need to refresh the window in order for the elment's new text value to show up
            window.refresh()

        if event == "-START-":
            
            #user_input = values['-INPUT-']
            result = process_user_input(values['-INPUT-'])
            if result:
                minutes_ = int(values['-INPUT-'])

                # Update/Set variables needed for the timer logic
                now = datetime.now()
                future_time = now + timedelta(minutes=minutes_)
                timer_running = True

                # Disable/Enable the appropriate buttons
                disable_button_state(['-START-', '-BREAK-'], True)
                disable_button_state(['-STOP-'], False)
            else:
                sg.popup_error(f'{default_error_msg}', title="Error")

        if event == "-BREAK-":
            #print("-BREAK-")
            now = datetime.now()
            #future_time = now + timedelta(minutes=10, seconds=0)
            future_time = now + timedelta(minutes=default_break)
            timer_running = True

            # Disable/Enable the appropriate buttons
            disable_button_state(['-START-', '-BREAK-'], True)
            disable_button_state(['-STOP-'], False)
        
        if timer_running:           
            if not now.strftime('%H:%M:%S') == future_time.strftime('%H:%M:%S'):

                # Get the delta and calculate the remaining hours, minutes and seconds
                delta = future_time - now
                minutes, seconds = divmod(delta.seconds, 60)
                hours, minutes = divmod(minutes, 60)

                # Update the text elment's value with the remaining time
                display_time = f"{hours}:{minutes}:{seconds}"
                set_time_element_text_value(display_time)

                # Need to refresh the window in order for the elment's new text value to show up
                window.refresh()

                # Update the "now" time
                now = datetime.now()

            else:
                # Disable the timer
                timer_running = False

                # Display a congratulatory popup message
                sg.popup(f"Timer is done. Current time = {now.strftime('%H:%M:%S')}", title="")

                #Update the elements
                set_time_element_text_value(default_time_text)
                disable_button_state(['-START-', '-BREAK-'], False)

                # Need to refresh the window in order for the elment's new text value to show up
                window.refresh()
                
    window.close()


if __name__ == '__main__':
    pomodoro_gui()