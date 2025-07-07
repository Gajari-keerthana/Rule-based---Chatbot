// React-based UI for Rule-Based EdTech Student Support Chatbot
// Backend must be running separately (Flask, FastAPI, or similar)

import React, { useState } from "react";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "🎓 Welcome to EdTech Student Support Chatbot! How can I help you today?" }
  ]);
  const [userInput, setUserInput] = useState("");

  const handleSend = async () => {
    if (!userInput.trim()) return;

    const newMessages = [...messages, { sender: "user", text: userInput }];
    setMessages(newMessages);

    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
      });
      const data = await response.json();
      setMessages([...newMessages, { sender: "bot", text: data.response }]);
    } catch (error) {
      setMessages([...newMessages, { sender: "bot", text: "❌ There was an error connecting to the server." }]);
    }

    setUserInput("");
  };

  return (
    <div className="flex flex-col items-center p-4 min-h-screen bg-gray-100">
      <div className="w-full max-w-xl shadow-lg rounded-2xl bg-white p-4 mb-4">
        <h2 className="text-xl font-bold text-center mb-2">EdTech Student Chatbot</h2>
        <div className="h-96 overflow-y-auto border p-2 rounded bg-gray-50">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`my-2 ${msg.sender === "bot" ? "text-left" : "text-right"}`}
            >
              <span
                className={`inline-block px-3 py-2 rounded-lg text-sm max-w-xs break-words ${
                  msg.sender === "bot"
                    ? "bg-blue-100 text-blue-900"
                    : "bg-green-100 text-green-900"
                }`}
              >
                {msg.text}
              </span>
            </div>
          ))}
        </div>
        <div className="flex mt-4">
          <input
            className="flex-grow px-3 py-2 border rounded-l-lg focus:outline-none"
            type="text"
            placeholder="Type your message..."
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
          />
          <button
            className="px-4 py-2 bg-blue-600 text-white rounded-r-lg hover:bg-blue-700"
            onClick={handleSend}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
