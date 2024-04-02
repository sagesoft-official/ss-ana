import os
import json
import random
from nicegui import ui

version = "v0.0.1"

def file_not_found_error(file):
    file = str(file).replace("data/", "").replace(".json", "")
    ana_messages = [{
        "id": "error",
        "msg": f"语录{file}不存在！",
        "author": "None",
        "time": "None"
}]
    return ana_messages

with ui.card().classes("absolute-center"):
        ui.badge(f"桑尾草原语录 | ss_ana {version}", outline=True)
        ui.button("楠桐语录", on_click=lambda e: ui.open("ana/a")).classes("w-full")

for dir in os.walk("data"):
    for file in dir[2]:
        if file.endswith(".json"):
            page = str(file).replace(".json", "")
            print(f"1:{page}")
            @ui.page(f"/ana/{page}")
            def ana_page():
                print(f"2:{page}")
                file = f"data/{page}.json"
                if not os.path.exists(file):
                    ana_messages = file_not_found_error(file)
                else:
                    with open(file, 'r') as f:
                        ana_messages = json.load(f)
                    number = random.randint(0, len(ana_messages) - 1)
                    print(number)
                    ana_messages = ana_messages[number]

                id = ana_messages["id"]
                msg = ana_messages["msg"]
                author = ana_messages["author"]
                time = ana_messages["time"]

                with ui.card().classes("absolute-center"):
                    ui.badge(f"桑尾草原语录 | ss_ana {version}", outline=True)
                    with ui.row():
                        ui.badge("id")
                        ui.label(id)
                    with ui.row():
                        ui.badge("语录")
                        ui.label(msg)
                    with ui.row():
                        ui.badge("作者")
                        ui.label(author)
                    with ui.row():
                        ui.badge("时间")
                        ui.label(time)
                return ana_messages

            @ui.page(f"/ana/{page}/json")
            def ana_json_page():
                print(f"3:{page}")
                from fastapi.responses import JSONResponse
                from fastapi.encoders import jsonable_encoder
                file = f"data/{page}.json"
                if not os.path.exists(file):
                    ana_messages = file_not_found_error(file)
                else:
                    with open(file, 'r') as f:
                        ana_messages = json.load(f)
                    number = random.randint(0, len(ana_messages) - 1)
                    print(number)
                    ana_messages = ana_messages[number]
                ana_messages = jsonable_encoder(ana_messages)
                return JSONResponse(ana_messages)

ui.run(port=7777, title="桑尾草原语录", show=False, reload=True)