from database.connection import get_connection


class MessageRepository:

    @staticmethod
    def save_message(
            session_id,
            sender,
            content
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO chat_message
            (
                session_id,
                sender,
                content
            )
            VALUES
            (%s,%s,%s)
            """,
            (
                session_id,
                sender,
                content
            )
        )

        conn.commit()

        cursor.close()

        conn.close()

    @staticmethod
    def get_messages(session_id):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT sender,
                   content
            FROM chat_message
            WHERE session_id=%s
            ORDER BY id
            """,
            (session_id,)
        )

        rows = cursor.fetchall()

        cursor.close()

        conn.close()

        return rows