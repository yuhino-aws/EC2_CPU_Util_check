import boto3
from time import sleep
import time
import json
import re

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
                queue_message = json.loads(message.body)
                utilization_str = queue_message['Message']
                utilization_array = utilization_str.split()
                utilization = (10000 - int(re.sub(r'\D', '',utilization_array[7])))/100
                print(utilization)
                #print(queue_message)
                message.delete()
                sleep(sleep_time)
        else:
            sleep(sleep_time)
            # メッセージがなくなったらbreak
            break

    