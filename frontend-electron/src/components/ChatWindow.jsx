import { useState, useEffect } from "react";

import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import Sidebar from "./Sidebar";
import { useRef } from "react";

function ChatWindow() {
  const [sessionId, setSessionId] = useState(null);
  useEffect(() => {
    console.log("Session Changed:", sessionId);
  }, [sessionId]);
  const sessionCreated = useRef(false);

  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      text: "Welcome to AI OS",
    },
  ]);
  const [sessions, setSessions] = useState([]);
  const messagesEndRef = useRef(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const loadSessions = async () => {
    setLoading(true);
    const response = await fetch("http://localhost:8002/session/");
    setLoading(false);

    const data = await response.json();
    console.log("Sessions:", data);

    setSessions(data);
  };

  useEffect(() => {
    const initialize = async () => {
      if (sessionCreated.current) {
        return;
      }

      sessionCreated.current = true;

      await createSession();
      await loadSessions();
    };

    initialize();
  }, []);

  const createSession = async () => {
    console.log("Creating Session...");

    try {
      const response = await fetch("http://localhost:8002/session/", {
        method: "POST",
      });

      const data = await response.json();

      setSessionId(data.session_id);
      console.log("Session Created:", data.session_id);

      console.log("Session Created:", data.session_id);
    } catch (error) {
      console.error(error);
    }
  };

  const startNewChat = async () => {
    await createSession();

    setMessages([
      {
        sender: "assistant",
        text: "New Chat Started",
      },
    ]);
  };

  const loadChatHistory = async (selectedSessionId) => {
    console.log(
        "Loading session:",
        selectedSessionId
    );
    const response = await fetch(
      `http://localhost:8002/message/${selectedSessionId}`,
    );

    const data = await response.json();
    console.log(data);

    const history = data.map((message) => ({
      sender: message[0],
      text: message[1],
    }));

    setSessionId(selectedSessionId);
    console.log(history);
    setMessages(history);
  };

  const handleSend = async (message) => {
    console.log("Current Session ID:", sessionId);

    if (sessionId === null) {
      console.log("Waiting for session creation...");

      return;
    }

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: message,
      },
    ]);

    setMessages((prev) => [
      ...prev,
      {
        sender: "assistant",
        text: "Thinking...",
      },
    ]);

    if (messages.length === 1) {
      const url = `http://localhost:8002/session/session/${sessionId}?title=${encodeURIComponent(message)}`;

      console.log(url);

      const response = await fetch(url, {
        method: "PUT",
      });

      console.log(response.status);

      await loadSessions();
    }

    try {
      const response = await fetch("http://localhost:8000/chat/", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          session_id: sessionId,
          message: message,
        }),
      });

      const data = await response.json();

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          sender: "assistant",
          text: data.response,
        };

        return updated;
      });
    } catch (error) {
      console.error(error);

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          sender: "assistant",
          text: "Unable to connect to AI Service.",
        };

        return updated;
      });
    }
  };

  return (
    <div className="app-container">
      <Sidebar
        sessions={sessions}
        onNewChat={startNewChat}
        onSelectChat={loadChatHistory}
      />

      <div className="chat-container">
        <div className="chat-header">
          <h2>AI OS Assistant</h2>
        </div>

        <div className="messages">
          {messages.map((msg, index) => (
            <MessageBubble key={index} sender={msg.sender} text={msg.text} />
          ))}
        </div>

        {loading && (
          <div className="typing">
            <span />
            <span />
            <span />
          </div>
        )}

        <ChatInput onSend={handleSend} disabled={sessionId === null} />
      </div>
    </div>
  );
}

export default ChatWindow;
