
import random

quiz_data = [
    {
        "question": "What makes this VA course different from others?",
        "choices": ["It focuses on theory only", "It's designed only for experienced VAs", "It offers a hand-holding, beginner-friendly roadmap", "It's mostly about resume writing"],
        "answer": "C",
        "explanation": "The course is designed for total beginners and includes step-by-step guidance, not just theory."
    },
    {
        "question": "Which skill is NOT specifically mentioned as part of in-demand VA skills in the course?",
        "choices": ["Admin work", "Social media tasks", "Data entry", "Web development"],
        "answer": "D",
        "explanation": "Web development is not mentioned; the course focuses on common VA tasks like admin and social media."
    },
    {
        "question": "What is the goal of identifying your ideal clients?",
        "choices": ["To avoid working at all", "To make quick money", "To find clients that are kind, pay well, and offer a healthy environment", "To practice interviews"],
        "answer": "C",
        "explanation": "The course emphasizes finding ideal clients who are kind, pay well, and provide a healthy work environment."
    },
    {
        "question": "What tool will help you apply for jobs even with no experience?",
        "choices": ["High school diploma", "Mii's templates for resumes and portfolios", "A fancy laptop", "Paid advertising"],
        "answer": "B",
        "explanation": "Mii provides sample templates to help you showcase your potential without prior experience."
    },
    {
        "question": "What's the goal of the proposal masterclass?",
        "choices": ["To beg for jobs", "To create random templates", "To teach proven scripts for beginners", "To avoid proposals altogether"],
        "answer": "C",
        "explanation": "It aims to equip you with effective and proven scripts to stand out even as a beginner."
    },
    {
        "question": "How does the course help you with client interviews?",
        "choices": ["Avoid them completely", "Just wing it", "Practice answering common questions confidently", "Hire someone to do it"],
        "answer": "C",
        "explanation": "The course teaches how to confidently answer common client questions in interviews."
    },
    {
        "question": "After being hired, what's the next focus of the course?",
        "choices": ["Quitting immediately", "Learning onboarding skills", "Changing careers", "Refunding the client"],
        "answer": "B",
        "explanation": "The course shows how to onboard clients professionally and stay organized."
    },
    {
        "question": "What does 'Deliver WOW Results' mean?",
        "choices": ["Overdeliver always", "Make clients dependent", "Gain repeat clients by providing excellent service", "Say yes to everything"],
        "answer": "C",
        "explanation": "You're taught how to impress clients to gain loyalty and repeat work."
    },
    {
        "question": "What is encouraged after landing a client?",
        "choices": ["Do nothing", "Wait for instructions", "Act organized and professional", "Ask to be micromanaged"],
        "answer": "C",
        "explanation": "You're expected to take initiative, stay organized, and be professional right after being hired."
    },
    {
        "question": "What's the long-term goal of this course?",
        "choices": ["Just get one client", "One-time earnings", "Make freelancing a full-time scalable career", "Make online friends"],
        "answer": "C",
        "explanation": "The course prepares you for a sustainable, scalable VA career."
    },
    {
        "question": "What is one of the teaching styles in this course?",
        "choices": ["Textbooks only", "All self-study", "Video lessons with hands-on tasks", "PowerPoint lectures"],
        "answer": "C",
        "explanation": "The course includes step-by-step video lessons and practice activities after each module."
    },
    {
        "question": "What is emphasized when you're not confident yet?",
        "choices": ["Wait until perfect", "Don't try yet", "Action beats overthinking", "Ask others to do the work"],
        "answer": "C",
        "explanation": "The course encourages action even if you're not 100% confident or ready."
    },
    {
        "question": "How should you handle not knowing something?",
        "choices": ["Quit", "Hide it", "Be curious and Google it", "Ignore it"],
        "answer": "C",
        "explanation": "Being curious and willing to learn is highly encouraged—even Googling helps."
    },
    {
        "question": "Why should you set boundaries early?",
        "choices": ["To look bossy", "To reduce tasks", "To prevent abuse and set expectations", "To ask for raises"],
        "answer": "C",
        "explanation": "Boundaries ensure a respectful relationship and prevent abuse, even for newbies."
    },
    {
        "question": "Why document everything?",
        "choices": ["To show off", "To reduce memory usage", "To stay organized and have reference", "To submit it to school"],
        "answer": "C",
        "explanation": "Documenting helps you stay organized and keeps useful records for future tasks."
    },
    {
        "question": "What mindset should you have as a VA?",
        "choices": ["Job-seeker", "Just an assistant", "Business owner", "Casual worker"],
        "answer": "C",
        "explanation": "Treating your VA work like a business helps you track, grow, and succeed long-term."
    },
    {
        "question": "Why collect feedback and reviews?",
        "choices": ["For drama", "To make friends", "To impress teachers", "To build credibility and get better clients"],
        "answer": "D",
        "explanation": "Feedback and reviews serve as social proof to win high-paying clients later."
    },
    {
        "question": "What is encouraged after finishing the course?",
        "choices": ["Relax forever", "Forget clients", "Keep growing and learning", "Switch industries"],
        "answer": "C",
        "explanation": "The course encourages continuous improvement and learning even after completion."
    },
    {
        "question": "What is the purpose of the manifestation task?",
        "choices": ["To share dreams with friends", "To write your goals and get clear on your why", "To waste time", "To show off"],
        "answer": "B",
        "explanation": "It helps you align your goals with your action plan—important for staying motivated."
    },
    {
        "question": "What's Mii's message for students who have doubts?",
        "choices": ["Give up", "You'll never make it", "YES. YOU. CAN.", "Try something else"],
        "answer": "C",
        "explanation": "Mii reassures students that they absolutely can succeed, even with no experience."
    }
]

def run_quiz():
    print("🧠 General Virtual Assistant Mastery: Quiz on Becoming a VA\n")
    score = 0
    random.shuffle(quiz_data)

    for i, item in enumerate(quiz_data, 1):
        print(f"Question {i}: {item['question']}")
        for idx, choice in zip("ABCD", item["choices"]):
            print(f"  {idx}. {choice}")

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        correct = item["answer"]
        print("\nResult:")

        if answer == correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer is {correct}.")

        print("💡", item["explanation"])
        print("-" * 50)

    print(f"\n🎉 Quiz Completed! Your Score: {score} / {len(quiz_data)}")

if __name__ == "__main__":
    run_quiz()
