import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            app_name = "DrinkWaterMinder",
            app_icon = "D:\logo\Iconsmind-Outline-Glass-Water.ico",
            title    = "Time to Drink Water",
            message  = "Water helps in maintaining the temperature of body and keeps us cool",
            timeout  = 10
        )
        time.sleep(60*60)