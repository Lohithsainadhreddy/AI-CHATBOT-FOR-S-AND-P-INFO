import React, { useRef, useEffect } from "react";

function ChatWindow({ messages }) {
  const containerRef = useRef(null);

  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div ref={containerRef} className="flex-grow p-4 bg-white border-t border-b border-gray-200 overflow-y-auto space-y-2">
      {messages.map((msg, idx) => (
        <div key={idx} className={`flex ${msg.sender === "bot" ? "justify-start" : "justify-end"}`}>
          <div className={`px-4 py-2 rounded-xl max-w-72 sm:max-w-[35rem] md:max-w-xl lg:max-w-7xl break-words ${msg.sender === "bot" ? "bg-gray-200 text-gray-800 rounded-bl-none" : "bg-blue-500 text-white rounded-br-none"}`}>
            {msg.text}
          </div>
        </div>
      ))}
    </div>
  );
}

export default ChatWindow;