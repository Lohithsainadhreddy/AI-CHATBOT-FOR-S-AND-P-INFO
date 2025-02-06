import React, { useState } from "react";

function ChatInput({ onSend }) {
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSend(input);
    setInput("");
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 flex bg-gray-50 border-t border-gray-200">
      <input 
        type="text"
        className="flex-grow border border-gray-300 rounded-l px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-300"
        placeholder="Type your message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button 
        type="submit" 
        className="bg-blue-500 hover:bg-blue-600 transition text-white px-4 py-2 rounded-r focus:outline-none"
      >
        Send
      </button>
    </form>
  );
}

export default ChatInput;