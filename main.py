from tkinter import *
from tkinter import messagebox
from api_part import get_weather
from api_part import get_forecast


def search():

    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img['file'] = f'C:\\Users\\mihai\\PycharmProjects\\weather_app\\weather_icons\\{weather[4]}.png'
        temp_lbl['text'] = '{:.2f} C'.format(weather[2])
        weather_lbl['text'] = weather[3]
        wind_speed_lbl['text'] = '{:.2f}'.format(weather[5]),'km/h'
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

def forecast():

    city = city_text.get()
    weather_forecast = get_forecast(city)
    if weather_forecast:
        location_lbl['text'] = '{}, {}'.format(weather_forecast[0], weather_forecast[1])
        temp_lbl_0['text'] = '{:.2f}'.format(weather_forecast[2])
        temp_lbl_1['text'] = '{:.2f}'.format(weather_forecast[4])
        temp_lbl_2['text'] = '{:.2f}'.format(weather_forecast[6])
        temp_lbl_3['text'] = '{:.2f}'.format(weather_forecast[8])
        temp_lbl_4['text'] = '{:.2f}'.format(weather_forecast[10])
        temp_lbl_5['text'] = '{:.2f}'.format(weather_forecast[12])
        temp_lbl_6['text'] = '{:.2f}'.format(weather_forecast[14])
        weather_lbl_0['text'] = weather_forecast[3]
        weather_lbl_1['text'] = weather_forecast[5]
        weather_lbl_2['text'] = weather_forecast[7]
        weather_lbl_3['text'] = weather_forecast[9]
        weather_lbl_4['text'] = weather_forecast[11]
        weather_lbl_5['text'] = weather_forecast[13]
        weather_lbl_6['text'] = weather_forecast[15]
        wind_speed_lbl_0['text'] = '{:.2f}'.format(weather_forecast[16]), 'km/h'
        wind_speed_lbl_1['text'] = '{:.2f}'.format(weather_forecast[17]), 'km/h'
        wind_speed_lbl_2['text'] = '{:.2f}'.format(weather_forecast[18]), 'km/h'
        wind_speed_lbl_3['text'] = '{:.2f}'.format(weather_forecast[19]), 'km/h'
        wind_speed_lbl_4['text'] = '{:.2f}'.format(weather_forecast[20]), 'km/h'
        wind_speed_lbl_5['text'] = '{:.2f}'.format(weather_forecast[21]), 'km/h'
        wind_speed_lbl_6['text'] = '{:.2f}'.format(weather_forecast[22]), 'km/h'
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


if __name__ == '__main__':
    app = Tk()
    app.title("Weather app")
    app.geometry('1250x600')
    app.configure(bg='lightblue')

    label_1 = Label(app, text='Instert city: ', font=('bold', 14), width = 16, bg='lightblue')
    label_1.grid(row=0, column=0)

    city_text = StringVar()
    city_entry = Entry(app, textvariable=city_text, font=('bold', 14), width = 16)
    city_entry.grid(row=0, column=1)

    search_btn = Button(app, text="Current weather", font=('bold', 14), width=16, command=search,bg='yellow')
    search_btn.grid(row=1, column=0)

    forecast_btn = Button(app, text="Weather Forecast", font=('bold', 14), width=16, command=forecast,bg='yellow')
    forecast_btn.grid(row=1, column=1)

    location_lbl = Label(app, text="", font=('bold ', 26), bg='lightblue')
    location_lbl.grid(row=2, column=0)

    img = PhotoImage(file='')
    image = Label(app, image=img, bg='lightblue')
    image.grid(row=2, column=1)

    temp_lbl = Label(app, text='',font=('Calibri bold', 36), bg='lightblue')
    temp_lbl.grid(row=3, column=0)

    temp_lbl_0 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_0.grid(row=5, column=0)

    temp_lbl_1 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_1.grid(row=5, column=1)

    temp_lbl_2 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_2.grid(row=5, column=2)

    temp_lbl_3 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_3.grid(row=5, column=3)

    temp_lbl_4 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_4.grid(row=5, column=4)

    temp_lbl_5 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_5.grid(row=5, column=5)

    temp_lbl_6 = Label(app, text='',font=('bold', 34), bg='lightblue')
    temp_lbl_6.grid(row=5, column=6)

    weather_lbl = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl.grid(row=2, column=2)

    weather_lbl_0 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_0.grid(row=7, column=0)

    weather_lbl_1 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_1.grid(row=7, column=1)

    weather_lbl_2 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_2.grid(row=7, column=2)

    weather_lbl_3 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_3.grid(row=7, column=3)

    weather_lbl_4 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_4.grid(row=7, column=4)

    weather_lbl_5 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_5.grid(row=7, column=5)

    weather_lbl_6 = Label(app, text='',font=('bold', 16), bg='lightblue')
    weather_lbl_6.grid(row=7, column=6)

    wind_speed_lbl = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl.grid(row=3, column=2)

    wind_speed_lbl_0 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_0.grid(row=10, column=0)

    wind_speed_lbl_1 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_1.grid(row=10, column=1)

    wind_speed_lbl_2 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_2.grid(row=10, column=2)

    wind_speed_lbl_3 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_3.grid(row=10, column=3)

    wind_speed_lbl_4 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_4.grid(row=10, column=4)

    wind_speed_lbl_5 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_5.grid(row=10, column=5)

    wind_speed_lbl_6 = Label(app, text='', font=('bold', 16), bg='lightblue')
    wind_speed_lbl_6.grid(row=10, column=6)


    app.mainloop()