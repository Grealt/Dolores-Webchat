def detect_emotion(message):
    lowered = message.lower()
    if any(word in lowered for word in ['sad', 'upset', 'down']):
        return "empathetic"
    elif any(word in lowered for word in ['happy', 'great', 'excited']):
        return "joyful"
    elif any(word in lowered for word in ['angry', 'mad', 'furious']):
        return "calm"
    else:
        return "neutral"
