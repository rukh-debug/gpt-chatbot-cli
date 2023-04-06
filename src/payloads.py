presets = {
    "Chat": {
        "message": "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
        "inject": {
            "state": True,
            "start": "AI:",
            "end": "Human:"
        },
    },
    "Q&A": {
        "message": "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with 'Unknown'.\n",
        "inject": {
            "state": True,
            "start": "A:",
            "end": "Q:"
        },
    },
    "Grammar Correction": {
        "message": "Correct this to standard English:\n",
        "inject": {
            "state": False,
        }
    },
    "Eli5": {
        "message":"Summarize this for a second-grade student:\n",
        "inject": {
            "state": False,
        }
    },
    "Custom": {
        "message": "",
        "inject": {
            "state": False
        }
    }
}
