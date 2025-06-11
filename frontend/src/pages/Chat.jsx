import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Chat = () => {
  const [token, setToken] = useState(null);
  const [message, setMessage] = useState("");
  const [botResponse, setBotResponse] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    if (!storedToken) {
      navigate("/login");  // No token, redirect to login
    } else {
      setToken(storedToken);
    }
  }, [navigate]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    try {
      const res = await fetch("http://localhost:8000/chat/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ text: message }),
      });

      if (!res.ok) {
        throw new Error("Failed to send message");
      }

      const data = await res.json();
      setBotResponse(data.bot_message?.text || "No response from bot");
      setMessage("");
    } catch (err) {
      console.error(err);
      setBotResponse("Error communicating with server");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Chat</h2>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
      />
      <button onClick={sendMessage}>Send</button>
      {botResponse && (
        <div style={{ marginTop: "1rem" }}>
          <h4>Response:</h4>
          <p>{botResponse}</p>
        </div>
      )}
    </div>
  );
};

export default Chat;
