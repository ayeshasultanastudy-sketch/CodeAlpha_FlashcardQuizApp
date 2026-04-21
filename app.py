import streamlit as st

# -----------------------------
# Flashcard Data (Session State)
# -----------------------------
if "flashcards" not in st.session_state:
    st.session_state.flashcards = [
        {"question": "What is Python?", "answer": "A high-level programming language"},
        {"question": "What is Streamlit?", "answer": "A Python framework for web apps"},
        {"question": "What is a variable?", "answer": "A container used to store data"},
        {"question": "What is a function?", "answer": "A block of reusable code"},
        {"question": "What is a loop?", "answer": "Used to repeat a block of code"},
        {"question": "What is HTML?", "answer": "A markup language for web pages"},
        {"question": "What is CSS?", "answer": "Used to style web pages"},
        {"question": "What is JavaScript?", "answer": "A programming language for web interactivity"},
        {"question": "What is Git?", "answer": "A version control system for tracking code changes"},
    ]

if "index" not in st.session_state:
    st.session_state.index = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False


# -----------------------------
# Functions
# -----------------------------
def next_card():
    st.session_state.index = (st.session_state.index + 1) % len(st.session_state.flashcards)
    st.session_state.show_answer = False

def prev_card():
    st.session_state.index = (st.session_state.index - 1) % len(st.session_state.flashcards)
    st.session_state.show_answer = False

def delete_card():
    if st.session_state.flashcards:
        st.session_state.flashcards.pop(st.session_state.index)
        st.session_state.index = 0
        st.session_state.show_answer = False


# -----------------------------
# UI
# -----------------------------
st.title("📚 Flashcard Quiz App (CodeAlpha Task 1)")

cards = st.session_state.flashcards

if cards:

    card = cards[st.session_state.index]

    st.subheader(f"Card {st.session_state.index + 1} / {len(cards)}")

    st.write("### ❓ Question:")
    st.info(card["question"])

    # Show Answer Button
    if st.button("Show Answer"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.success(f"💡 Answer: {card['answer']}")

    # Navigation Buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("⬅ Previous", on_click=prev_card)

    with col2:
        st.button("Next ➡", on_click=next_card)

    with col3:
        st.button("🗑 Delete", on_click=delete_card)

else:
    st.warning("No flashcards available. Add one below!")


# -----------------------------
# Add Flashcards Section
# -----------------------------
st.markdown("---")
st.subheader("➕ Add New Flashcard")

q = st.text_input("Enter Question")
a = st.text_input("Enter Answer")

if st.button("Add Flashcard"):
    if q and a:
        st.session_state.flashcards.append({"question": q, "answer": a})
        st.success("Flashcard added successfully!")
    else:
        st.error("Please enter both question and answer")