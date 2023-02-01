from fastapi import FastAPI, WebSocket

app = FastAPI()

websocket_list = []


@app.websocket("/ws")
async def websocket_router(websocket: WebSocket):
    await websocket.accept()
    if websocket not in websocket_list:
        websocket_list.append(websocket)
    while True:
        data = await websocket.receive_text()
        for web in websocket_list:
            if web != websocket:
                await web.send_text(f"{data}")
