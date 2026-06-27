import { useState } from 'react';

function ChatInput({ onSend, disabled  }) {

    const [message, setMessage] =
        useState('');

    const sendMessage = () => {

        if (
            !message.trim()
        ) {
            return;
        }

        onSend(message);

        setMessage('');
    };

    return (

        <div className="chat-input">

            <input
                type="text"
                placeholder="Ask AI OS..."
                value={message}
                onChange={(e) =>
                    setMessage(
                        e.target.value
                    )
                }
                onKeyDown={(e) => {

                    if (
                        e.key === 'Enter'
                    ) {

                        sendMessage();
                    }
                }}
            />

            <button
                onClick={
                    sendMessage
                }
                disabled={disabled}
            >
                Send
            </button>

        </div>
    );
}

export default ChatInput;