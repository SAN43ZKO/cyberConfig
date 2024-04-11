from flet import *
from commands import *
from variables import *
import flet_fastapi
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

@app.get('/download')
async def download():
    headers = {'Content-Disposition': 'attachment; filename="cyberCFG.cfg"'}
    return StreamingResponse("cyberCFG.cfg", headers=headers, media_type="text/txt")

async def main(page: Page):
        page.title = "CyberConfig"
        page.spacing = 0
        page.padding = 0
        page.scroll = ScrollMode.ADAPTIVE
        page.theme_mode = "dark"


        #Download Gold CFG
        async def dwn_btn_change(e):
                e.control.bgcolor = "#155498" if e.data == "true" else "#103f72"
                await e.control.update_async()

        header_dwn_btn = ElevatedButton("Gold CFG",url="https://google.com", color="#ffffff", bgcolor="#103f72", on_hover=dwn_btn_change, style=ButtonStyle(shape={MaterialState.DEFAULT: RoundedRectangleBorder(radius=10)}))
        
        #Create CFG File
        async def create_file(e):
                with open('./download/cyberCFG.cfg', 'a') as file:
                    result = f'{cros_color_text} "{cros_color_value.value}"\n'
                    file.writelines(result)


        file_btn = ElevatedButton("Create File", color="#ffffff", bgcolor="#103f72", on_click=create_file, on_hover=dwn_btn_change, style=ButtonStyle(shape={MaterialState.DEFAULT: RoundedRectangleBorder(radius=10)}))
        
        #Download file
        async def download_file(e):
             await page.launch_url_async(url='/download', web_window_name='_self')

        dwn_file_btn = ElevatedButton("Download File", color="#ffffff", bgcolor="#103f72", on_click=download_file, on_hover=dwn_btn_change, style=ButtonStyle(shape={MaterialState.DEFAULT: RoundedRectangleBorder(radius=10)}))

        

        header = Container(
            expand=True,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                Text("CyberConfig", size=25, color="#ffffff", weight="bold"),
                            ]
                        )
                    ),
                    Container(
                        expand=True,
                        content=Row(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                header_dwn_btn
                            ]
                        )
                    ),
                    Container(
                        content=Row(
                            controls=[
                                VerticalDivider(thickness=1, color="#ffffff"),
                                IconButton(icon=icons.FACEBOOK, icon_color="#ffffff"),
                                IconButton(icon=icons.FACEBOOK, icon_color="#ffffff"),
                                IconButton(icon=icons.FACEBOOK, icon_color="#ffffff"),
                            ]
                        )
                    ),
                ]
            )
        )

        main_content_text = Container(
            content=Column(
                spacing=30,
                controls=[
                    cros_scale,
                    cros_color,
                    cros_size,
                    cros_style
                ]
            )
        )

        main_content_field = Container(
            content=Column(
                controls=[
                    cros_scale_value,
                    cros_color_value,
                    cros_size_value,
                    cros_style_value,
                ]
            )
        )

        await page.add_async(
            Container(
                content=Column(
                    controls=[
                        Container(
                            padding=padding.only(left=10, right=10),
                            height=60,
                            bgcolor="#081d33",
                            content=Row(
                                expand=True,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[header]
                            )
                        ),
                        Container(
                            content=Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        padding=10,
                                        margin=margin.only(left=10, right=10, bottom=10),
                                        border=border.all(1, color="#ffffff"),
                                        border_radius=border_radius.all(10),
                                        content=Row(
                                            controls=[
                                                main_content_text,
                                                main_content_field,
                                            ]
                                        )
                                    ),
                                    Container(
                                        padding=10,
                                        margin=margin.only(left=10, right=10, bottom=10),
                                        border=border.all(1, color="#ffffff"),
                                        border_radius=border_radius.all(10),
                                        content=Row(
                                            controls=[
                                                main_content_text,
                                                main_content_field,
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        Container(
                            padding=10,
                            content=Row(
                                alignment=MainAxisAlignment.END,
                                controls=[
                                    file_btn,
                                    dwn_file_btn
                                ]
                            )
                        )
                    ]
                )
            )
            
        )
        await page.update_async()

# app(target=main, upload_dir="uploads", view=AppView.WEB_BROWSER)
app.mount('/', flet_fastapi.app(main),)