
import random

quiz_data = [
    {
        "question": "What is a Virtual Assistant (VA)?",
        "choices": [
            "A robot that automates online services",
            "An in-office secretary for executives",
            "An online assistant who supports business tasks remotely",
            "A ghost working from the cloud"
        ],
        "answer": 2,
        "explanation": "A VA is an online assistant who helps businesses with tasks remotely—often from home."
    },
    {
        "question": "What makes a VA 'virtual'?",
        "choices": [
            "They only work in virtual reality",
            "They don't physically exist",
            "They work online/remotely",
            "They communicate telepathically"
        ],
        "answer": 2,
        "explanation": "Being 'virtual' means the VA works remotely—usually online, not in a physical office."
    },
    {
        "question": "Which of the following is a task commonly done by VAs?",
        "choices": [
            "Plumbing",
            "Flying a drone",
            "Data entry",
            "Driving clients to meetings"
        ],
        "answer": 2,
        "explanation": "Data entry is a common administrative task handled by VAs."
    },
    {
        "question": "What makes a General VA ideal for beginners?",
        "choices": [
            "It requires a business degree",
            "It’s task-heavy and high-pressure",
            "It focuses on basic admin work and tools",
            "It pays the highest rates"
        ],
        "answer": 2,
        "explanation": "General VA roles involve manageable admin tasks perfect for those just starting out."
    },
    {
        "question": "Which tool is helpful for a General VA?",
        "choices": [
            "Python IDE",
            "Trello",
            "Photoshop",
            "Unreal Engine"
        ],
        "answer": 1,
        "explanation": "Trello is a project management tool commonly used by General VAs."
    },
    {
        "question": "Who does an Executive VA typically assist?",
        "choices": [
            "Freelancers",
            "Office clerks",
            "CEOs and Coaches",
            "College students"
        ],
        "answer": 2,
        "explanation": "Executive VAs usually support high-level clients like CEOs, coaches, and executives."
    },
    {
        "question": "What’s a good skill for an Executive VA?",
        "choices": [
            "Anticipating client needs",
            "Drawing anime",
            "Writing poetry",
            "Pet grooming"
        ],
        "answer": 0,
        "explanation": "Being proactive and anticipating needs sets Executive VAs apart."
    },
    {
        "question": "What is a Specialized VA?",
        "choices": [
            "Someone with no clear focus",
            "A VA with a unique skillset",
            "A VA that works for free",
            "A VA that manages errands"
        ],
        "answer": 1,
        "explanation": "Specialized VAs offer premium services based on specific expert skills."
    },
    {
        "question": "Which is a good tool for a Specialized VA?",
        "choices": [
            "Instagram",
            "WordPress",
            "Chess.com",
            "Paint"
        ],
        "answer": 1,
        "explanation": "WordPress is often used by Specialized VAs for website updates and content."
    },
    {
        "question": "What’s a benefit of niching down as a Specialized VA?",
        "choices": [
            "You get fewer clients",
            "You become a jack-of-all-trades",
            "You can charge higher rates",
            "You avoid doing any tasks"
        ],
        "answer": 2,
        "explanation": "Specialists are valued more, which means higher pay for targeted skills."
    },
    {
        "question": "What’s one underrated skill even beginners should learn?",
        "choices": [
            "Note-taking during meetings",
            "Playing guitar",
            "Speed typing contests",
            "Coding Python"
        ],
        "answer": 0,
        "explanation": "Note-taking and summarizing action items help VAs support clients better."
    },
    {
        "question": "Which mindset is important for new VAs?",
        "choices": [
            "I need to be perfect before starting",
            "Clients only want experts",
            "Confidence + Consistency = Clients",
            "I need 10 certifications first"
        ],
        "answer": 2,
        "explanation": "A confident, consistent learner is more likely to succeed than a perfectionist."
    },
    {
        "question": "Which of the following matters more than being a tech genius?",
        "choices": [
            "Being easy to work with",
            "Being a perfectionist",
            "Having a fancy logo",
            "Bragging online"
        ],
        "answer": 0,
        "explanation": "Clients love VAs who are proactive, reliable, and easy to collaborate with."
    },
    {
        "question": "What's an ideal first step in your VA journey?",
        "choices": [
            "Charge premium rates right away",
            "Focus on freelancing only",
            "Start with small tasks and grow",
            "Ignore training and wing it"
        ],
        "answer": 2,
        "explanation": "Starting with small tasks allows you to learn and build confidence steadily."
    },
    {
        "question": "What is the long-term goal of becoming a VA?",
        "choices": [
            "Burnout",
            "Quick fame",
            "Freedom and sustainable career",
            "Becoming a celebrity"
        ],
        "answer": 2,
        "explanation": "The ultimate goal is freedom — financial, career, and lifestyle flexibility."
    },
    {
        "question": "Why is journaling or reflecting important in VA training?",
        "choices": [
            "To waste time",
            "To manifest and clarify goals",
            "To brag online",
            "To avoid working"
        ],
        "answer": 1,
        "explanation": "Journaling helps manifest goals, stay focused, and track growth."
    },
    {
        "question": "Which tool is commonly used by Executive VAs?",
        "choices": [
            "Zoom",
            "Paint",
            "Spotify",
            "Minecraft"
        ],
        "answer": 0,
        "explanation": "Executive VAs often use tools like Zoom for meetings and coordination."
    },
    {
        "question": "What does 'VA' stand for?",
        "choices": [
            "Virtual Admin",
            "Voice Assistant",
            "Virtual Assistant",
            "Verified Associate"
        ],
        "answer": 2,
        "explanation": "VA stands for Virtual Assistant — someone who supports businesses online."
    },
    {
        "question": "Which is NOT typically a VA task?",
        "choices": [
            "Graphic design",
            "Email management",
            "Website updates",
            "Plumbing"
        ],
        "answer": 3,
        "explanation": "Plumbing is not a remote or digital task suitable for VAs."
    },
    {
        "question": "What makes you more likely to be hired?",
        "choices": [
            "Confidence and being proactive",
            "Waiting until you're perfect",
            "Asking for free mentorships",
            "Spamming job posts"
        ],
        "answer": 0,
        "explanation": "Clients prefer confident, proactive VAs — even if they’re beginners."
    }
]

random.shuffle(quiz_data)
score = 0

for i, q in enumerate(quiz_data, 1):
    print(f"\nQuestion {i}: {q['question']}")
    for idx, choice in enumerate(q['choices']):
        print(f"{chr(65+idx)}. {choice}")
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    correct_letter = chr(65 + q['answer'])

    if user_answer == correct_letter:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer is {correct_letter}. {q['choices'][q['answer']]}")
    print("📘 Explanation:", q['explanation'])

print(f"\n🏁 Quiz Complete! Your score: {score} out of {len(quiz_data)}")
