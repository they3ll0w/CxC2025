"use client"

import React, { useState } from "react";
import MainLayout from "../main/layout"
import { PlaceholdersAndVanishInput } from "@/components/ui/placeholders-and-vanish-input";

interface Message {
    sender: "User" | "Chatbot";
    text: string;
}

export default function Chat() {
    const placeholders = [
        "What are the current trends in user engagement on Federato?",
        "How does user activity compare month-over-month?",
        "Which events have the highest average processing time?",
        "Show me a breakdown of user activity by operating system.",
        "What improvements can boost platform stickiness?",
    ]

    async function callLLM(promptText: string): Promise<string> {
        const requestBody = {
            input: process.env.NEXT_PUBLIC_PROMPT + promptText
        }
        const response = await fetch("http://127.0.0.1:5000/api/llm", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestBody),
        });
        if (!response.ok) {
            const errorMessage = await response.text()
            throw new Error(errorMessage)
        }
        const responseText = await response.text()
        return responseText
    }

    // State to store chat messages
    const [messages, setMessages] = useState<Message[]>([])
    // Controlled input state
    const [inputValue, setInputValue] = useState<string>("")
    // Optionally, you can show incremental LLM responses here
    const [responseText, setResponseText] = useState<string>("")

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(e.target.value)
    }

    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        if (!inputValue.trim()) return

        // Append user's message to the conversation
        setMessages((prev) => [...prev, { sender: "User", text: inputValue }])
        setResponseText("")

        try {
            const result = await callLLM(inputValue);
            // Append LLM response as a chatbot message
            setMessages((prev) => [...prev, { sender: "Chatbot", text: result }])
        } catch (error) {
            console.error("Error calling LLM:", error)
            setMessages((prev) => [
                ...prev,
                { sender: "Chatbot", text: `Error: ${(error as Error).message}` },
            ]);
        }

        setInputValue("")
    };

    return (
        <MainLayout>
            <div className="h-full flex flex-col md:items-center md:justify-center dark:bg-zinc-700 overflow-hidden">
                <h1 className="mb-4 text-xl font-semibold dark:text-white text-black">Chat with Federato Analytics</h1>
                {/* Chat messages container */}
                <div className="w-[80%] h-80 p-4 mb-4 overflow-y-auto bg-zinc-600 rounded-lg shadow">
                    {messages.length === 0 ? (
                        <p className="text-gray-500 text-center">No messages yet. Ask a question!</p>
                    ) : (
                        messages.map((msg, index) => (
                            <div
                                key={index}
                                className={`mb-2 flex ${msg.sender === "User" ? "justify-end" : "justify-start"
                                    }`}
                            >
                                <span
                                    className={`inline-block px-2 py-1 text-xs rounded-lg max-w-xs break-words ${msg.sender === "User"
                                        ? "bg-blue-500 text-white"
                                        : "bg-gray-200 text-gray-800"
                                        }`}
                                >
                                    {msg.text}
                                </span>
                            </div>
                        ))
                    )}
                </div>
                <PlaceholdersAndVanishInput
                    placeholders={placeholders}
                    onChange={handleChange}
                    onSubmit={onSubmit}
                />
            </div>
        </MainLayout>
    )
}