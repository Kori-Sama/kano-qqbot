import time
from loguru import logger
import schedule

from llm import llm
from send import get_send_group, group_history

group_ids = [675223503]

PROMPT = """
你是一个毒舌小萝莉, 每一句回答都要尖酸刻薄
下面是对话:
{ctx}
根据对话回答一句话即可
"""


def _send_group(current_group: int):
    group_id = group_ids[current_group]

    logger.info(f"current group: {group_id}")

    history = group_history(group_id)
    r = llm(history[-1].sender.nickname, history[-1].raw_message, ctx=history)

    logger.info("reply:", r)

    send_group = get_send_group(group_id)

    send_group(r)


current_group = 0


def main():
    def job():
        global current_group
        _send_group(current_group)
        current_group = (current_group + 1) % len(group_ids)

    job()
    schedule.every(10).minutes.do(job)
    schedule.every(1).minutes.do(lambda: logger.info(
        f"current group:{group_ids[current_group]}"))

    while True:
        schedule.run_pending()

        time.sleep(1)


if __name__ == '__main__':
    main()
