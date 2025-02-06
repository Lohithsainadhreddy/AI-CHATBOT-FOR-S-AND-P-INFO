import React, { useState } from "react";
import ChatWindow from "./ChatWindow";
import ChatInput from "./ChatInput";
import axios from "axios";

function Chatbot() {
  const [messages, setMessages] = useState([]);

  const handleSend = async (text) => {
    if (!text.trim()) 
        return;
    setMessages((prev) => [...prev, { sender: "user", text }]);

    try {
        const response = await axios.get(`http://127.0.0.1:8000/chat/query?user_query=${text}`);
        console.log(response.data)
        setMessages((prev) => [...prev, { sender: "bot", text: response.data }]);
    } catch (e) {
        setMessages((prev) => [...prev, { sender: "bot", text: "Sorry, I'm having trouble understanding you right now." }]);
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-blue-100 to-blue-50 relative">
      <div className="bg-blue-500 text-white text-center py-3 font-semibold fixed top-0 left-0 right-0 z-10">
        AI-Powered Chatbot for Supplier and Product Information
      </div>
      <div className="flex flex-col h-full pt-16 pb-16">
        <div className="flex-grow overflow-y-auto">
          <ChatWindow messages={messages} />
        </div>
        <div className="fixed bottom-0 left-0 right-0 z-10">
          <ChatInput onSend={handleSend} />
        </div>
      </div>
    </div>
  );
}

export default Chatbot;
