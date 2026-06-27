function Sidebar({
    sessions,
    onNewChat,
    onSelectChat
}) {

    return (

        <div className="sidebar">

            <h1>AI OS</h1>

            <button
                onClick={onNewChat}
            >
                + New Chat
            </button>

            <div className="history">

                {
                    sessions.map(
                        session => (

                            <div
                                key={session.id}
                                className="history-item"
                                onClick={() =>
                                    onSelectChat(
                                        session.id
                                    )
                                }
                            >

                                {
                                    session.title
                                }

                            </div>

                        )
                    )
                }

            </div>

        </div>
    );
}

export default Sidebar;