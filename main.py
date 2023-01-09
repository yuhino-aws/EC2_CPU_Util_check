import boto3
from time import sleep
import time

# キューの名前を指定して
name = 'cm-test-queue'
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=name)

start = time.time() # forループ開始前のエポック時間を変数startに保存しておく。
duration = 3600
end = start + duration # forループの開始時間＋forループの実行時間 = forループの終了時間
sleep_time = 5

while time.time() <= end: 
    #print("running")
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

    