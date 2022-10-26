import PySimpleGUI as sg

layout = [
        [sg.Input(key = '-INPUT-'),
        sg.Spin(['km to mile', 'kg to pound', 'mile to km', 'pound to kg'], key = '-UNITS-')],
        [sg.Button('Convert', key = '-CONVERT-')],
        [sg.Text('Output', key = '-OUTPUT-')]
    ]
window = sg.Window('Converter',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'mile to km':
                    output = round(float(input_value) * 1.609344, 2)
                    output_string = f'{input_value} miles are {output} kms.'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'pound to kg':
                    output = round(float(input_value) * 0.4535924, 2)
                    output_string = f'{input_value} pound are {output} kgs.'
            
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please input a number')
window.close()