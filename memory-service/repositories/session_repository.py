from database.connection import get_connection


class SessionRepository:

    @staticmethod
    def create_session(title):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO chat_session(title)
            VALUES(%s)
            RETURNING id
            """,
            (title,)
        )

        session_id = cursor.fetchone()[0]

        conn.commit()

        cursor.close()
        conn.close()

        return session_id

    @staticmethod
    def get_sessions():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
        """
        SELECT
            id,
            title,
            created_at
        FROM chat_session
        ORDER BY created_at DESC
        """
        )

        rows = cursor.fetchall()

        sessions = []

        for row in rows:

            sessions.append({

            "id": row[0],

            "title": row[1],

            "created_at": str(
                row[2]
            )
            })

        cursor.close()
        conn.close()
    
        return sessions
    
    @staticmethod
    def update_title(
        session_id,
        title
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
        """
        UPDATE chat_session
        SET title = %s
        WHERE id = %s
        """,
        (
            title,
            session_id
        )
        )

        conn.commit()

        cursor.close()
        conn.close()