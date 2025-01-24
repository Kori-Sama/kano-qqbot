
from dataclasses import dataclass
from typing import Literal


def parse_post(data):
    if data["post_type"] == "message":
        if data.get("group_id"):
            return GroupPost.parse(data)
        return MessagePost.parse(data)

    if data["post_type"] == "notice":
        if data["notice_type"] == "group_increase":
            return GroupMemberIncreaseNotice.parse(data)
        if data["notice_type"] == "notify":
            return GroupPokeNotice.parse(data)
        if data["notice_type"] == "group_decrease":
            return GroupWithdrawNotice.parse(data)


@dataclass
class Post:
    time: int
    self_id: int
    post_type: str

    @staticmethod
    def parse(data):
        return Post(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"]
        )


@dataclass
class MessageSender:
    user_id: int
    nickname: str

    @staticmethod
    def parse(data):
        return MessageSender(
            post_type=data["post_type"],
            user_id=data["user_id"],
            nickname=data["nickname"],


        )


@dataclass
class GroupMessageSender(MessageSender):
    card: str
    role: Literal["owner", "admin", "member"]

    @staticmethod
    def parse(data):
        return GroupMessageSender(
            user_id=data["user_id"],
            nickname=data["nickname"],
            card=data["card"],
            role=data["role"],
        )


@dataclass
class Message:
    type: str
    data: dict

    @staticmethod
    def parse(data):
        return Message(
            type=data["type"],
            data=data["data"]
        )


@dataclass
class MessagePost(Post):
    post_type: Literal["message"]
    message_type: str
    sub_type: str
    message_id: int
    user_id: int
    message: list[Message]
    message_seq: int
    message_format: str
    raw_message: str
    font: int
    sender: MessageSender

    @staticmethod
    def parse(data):
        return MessagePost(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"],
            message_type=data["message_type"],
            sub_type=data["sub_type"],
            message_id=data["message_id"],
            user_id=data["user_id"],
            message=map(Message.parse, data["message"]),
            message_seq=data["message_seq"],
            message_format=data["message_format"],
            raw_message=data["raw_message"],
            font=data["font"],
            sender=MessageSender.parse(data["sender"])
        )


@dataclass
class GroupPost(MessagePost):
    group_id: int
    sender: GroupMessageSender

    @staticmethod
    def parse(data):
        return GroupPost(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"],
            message_type=data["message_type"],
            sub_type=data["sub_type"],
            message_id=data["message_id"],
            user_id=data["user_id"],
            message=map(Message.parse, data["message"]),
            message_seq=data["message_seq"],
            message_format=data["message_format"],
            raw_message=data["raw_message"],
            font=data["font"],
            sender=GroupMessageSender.parse(data["sender"]),
            group_id=data["group_id"],
        )


@dataclass
class NoticePost(Post):
    post_type: Literal["notice"]
    notice_type: str

    @staticmethod
    def parse(data):
        return NoticePost(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"],
            notice_type=data["notice_type"]
        )


@dataclass
class GroupWithdrawNotice(NoticePost):
    group_id: int
    user_id: int
    operator_id: int
    message_id: int

    @staticmethod
    def parse(data):
        return GroupWithdrawNotice(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"],
            notice_type=data["notice_type"],
            group_id=data["group_id"],
            user_id=data["user_id"],
            operator_id=data["operator_id"],
            message_id=data["message_id"]
        )


@dataclass
class GroupMemberIncreaseNotice(NoticePost):
    notice_type: Literal["group_increase"]
    sub_type: Literal["approve", "invite"]
    group_id: int
    user_id: int
    operator_id: int

    @staticmethod
    def parse(data):
        return GroupMemberIncreaseNotice(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"],
            notice_type=data["notice_type"],
            sub_type=data["sub_type"],
            group_id=data["group_id"],
            user_id=data["user_id"],
            operator_id=data["operator_id"]
        )


@dataclass
class GroupPokeNotice(NoticePost):
    notice_type: Literal["notify"]
    sub_type: Literal["poke"]
    group_id: int
    user_id: int
    target_id: int

    @staticmethod
    def parse(data):
        return GroupPokeNotice(
            time=data["time"],
            self_id=data["self_id"],
            post_type=data["post_type"],
            notice_type=data["notice_type"],
            sub_type=data["sub_type"],
            group_id=data["group_id"],
            user_id=data["user_id"],
            target_id=data["target_id"]
        )
