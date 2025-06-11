// src/components/MessageBubble.jsx

import React from "react";
import ReactMarkdown from "react-markdown";

const MessageBubble = ({ text, sender }) => {
  const bubbleClass =
    sender === "user"
      ? "bg-blue-600 text-white self-end"
      : "bg-gray-700 text-gray-100 self-start";

  return (
    <div
      className={`max-w-xl px-4 py-3 rounded-lg whitespace-pre-wrap break-words ${bubbleClass}`}
    >
      <ReactMarkdown>{text}</ReactMarkdown>
    </div>
  );
};

export default MessageBubble;
