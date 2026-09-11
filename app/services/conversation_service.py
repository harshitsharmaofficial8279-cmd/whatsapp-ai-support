from app.database import db
from app.database.models import Conversation, Message


def get_or_create_conversation(phone_number):
    conversation = Conversation.query.filter_by(
        phone_number=phone_number
    ).first()

    if conversation:
        return conversation

    conversation = Conversation(phone_number=phone_number)

    db.session.add(conversation)
    db.session.commit()

    return conversation


def save_message(conversation_id, sender, message_text):
    message = Message(
        conversation_id=conversation_id,
        sender=sender,
        message_text=message_text
    )

    db.session.add(message)
    db.session.commit()

    return message
