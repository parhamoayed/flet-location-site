
import flet as ft
import flet_geolocator as fg


def main(page: ft.Page):
    page.title = "My Location"
    page.padding = 20

    location_text = ft.Text(
        "هنوز موقعیت مکانی دریافت نشده است",
        size=18,
    )

    geolocator = fg.Geolocator()

    async def get_location(e):
        try:
            position = await geolocator.get_current_position()

            location_text.value = (
                f"Latitude: {position.latitude}\n"
                f"Longitude: {position.longitude}"
            )
        except Exception as error:
            location_text.value = f"Error: {error}"

        page.update()

    page.add(
        ft.Text("موقعیت مکانی من", size=26),
        ft.Button(
            "دریافت موقعیت من",
            on_click=get_location,
        ),
        location_text,
    )


ft.run(main)


#BROWSER=/home/parham/Downloads/firefox/firefox python 1.py