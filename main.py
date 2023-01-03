# import uvicorn # uvicornのインポートを追加
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     print("this is root")
#     return {"message": "Hello World"}

# @app.post("/")
# async def recieveQueue():
#     print("")
#     return None

# # オプション(host=0.0.0.0とし、EC2の外部IPアドレスを指定してアクセス可能にする)
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

import boto3
from time import sleep
import time



# キューの名前を指定して
name = 'cm-test-queu'
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=name)

start = time.time() # forループ開始前のエポック時間を変数startに保存しておく。
duration = 3600
end = start + duration # forループの開始時間＋forループの実行時間 = forループの終了時間
sleep_time = 5

while time.time() <= end: 
    print("running")
    while True:
        # メッセージを取得
        msg_list = queue.receive_messages(MaxNumberOfMessages=1)
        if msg_list:
            for message in msg_list:
                #print(message.body["Message"])
                print(message.body)
                message.delete()
                sleep(sleep_time)
        else:
            sleep(sleep_time)
            # メッセージがなくなったらbreak
            break

    