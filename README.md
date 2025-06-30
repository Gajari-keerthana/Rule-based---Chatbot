Project Title: Student Support Chatbot (Rule-Based for EdTech Platform)
                         (Keerthana Gajari)
Objective:
The primary objective of this rule-based chatbot is to enhance the learning experience for students by providing timely and automated assistance with frequently asked questions and common problems encountered on the EdTech platform.
Goals:
● Deliver instant support to students 24/7.
● Help resolve common student issues like login failures, enrollment status, and
assignment submission errors.
● Improve student experience by reducing waiting times for help.
● Reduce the number of support tickets for the student services team.
Non-Goals:
● The chatbot will not replace human support for complex or escalated issues.
● It will not process real-time transactions (e.g., payment processing).
● Initially, it will not include deep NLP or generative responses (LLM to be explored in
later versions).
User Stories:
- I want to reset my password so I can log in to my account.
- I want to check my course enrollment status so I can attend classes on time.
- I want to know the schedule of my courses so I can plan my week.
Features and Functional Requirements
Feature Description
Predefined intents Covers key support topics: account access,
course info, tech issues, and deadlines.
Decision tree logic Rule-based flows guide students through
troubleshooting steps.
Quick reply to buttons Options like “Reset Password”, “View
Schedule”, “Check Enrollment” to guide
navigation.
Error handling Catch unrecognized input and redirect to a
relevant menu or retry.
Escalation to live agent Trigger human support when chatbot cannot
resolve the issue.
Fallback response Example: “I didn’t understand that. Try
asking about login, enrollment, or schedule.”
UI/UX - Wireframe Summary
Welcome screen: “Hi! I’m your student support bot. How can I help you today?”
● text input box to give questions
● answers based on the trained data set or if the question is out of the training set it uses
OpenAI LLMs and answers the queries.
Tech Stack:
● Python
● Tkinter
● Open AI - Chat GPT
● Model - Sklearn, Tensorflow
Platform:
● Web App
Feedback option “Was this helpful?” button to rate responses.
