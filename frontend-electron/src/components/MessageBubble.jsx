function MessageBubble({
    sender,
    text
}) {

    const isUser =
        sender === 'user';

    return (

        <div
            className={
                isUser
                ? 'message user'
                : 'message assistant'
            }
        >

            <div className="avatar">

                {isUser
                    ? '👤'
                    : '🤖'}

            </div>

            <div className="bubble">

                {text}

            </div>

        </div>
    );
}

export default MessageBubble;