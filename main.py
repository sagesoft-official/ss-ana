import os
import json
import random
from nicegui import ui

version = "v0.0.1"

@ui.page("/ana/a")
def ana_page():
    def file_not_found_error(file):
        file = str(file).replace("data/", "").replace(".json", "")
        ana_messages = [{
            "id": "error",
            "msg": f"语录{file}不存在！",
            "author": "None",
            "time": "None"
    }]
        return ana_messages

    def get_ana(file):
        if not os.path.exists(file):
            ana_messages = file_not_found_error(file)
            ana_status = False
            return ana_status, ana_messages
        else:
            # asyncio.run(load_ana(file))
            with open(file, 'r') as f:
                ana_messages = json.load(f)
            number = random.randint(0, len(ana_messages) - 1)
            print(number)
            ana_messages = ana_messages[number]
            ana_status = True
            return ana_status, ana_messages

    ana = get_ana("data/a.json")

    if not ana[0]:
        id = ana[1][0]["id"]
        msg = ana[1][0]["msg"]
        author = ana[1][0]["author"]
        time = ana[1][0]["time"]
    else:
        id = ana[1]["id"]
        msg = ana[1]["msg"]
        author = ana[1]["author"]
        time = ana[1]["time"]

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

with ui.card().classes("absolute-center"):
    ui.badge(f"桑尾草原语录 | ss_ana {version}", outline=True)
    ui.button("楠桐语录", on_click=lambda e: ui.open("ana/a")).classes("w-full")

ui.run(port=7777, title="桑尾草原语录", show=False, reload=True)