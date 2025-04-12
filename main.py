import re
import streamlit as st


def check_password(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include uppercase letters.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include lowercase letters.")
        
    # Digit Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        strength = "✅ Strong Password!"
    elif score == 3:
        strength = "⚠️ Moderate Password - Consider adding more security features."
    else:
        strength = "❌ Weak Password - Improve it using the suggestions above."

    return score, strength, feedback


def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

    st.title("🔒 Password Strength Meter")
    st.markdown("---")
    password = st.text_input(
        "Enter your password:", type="password", placeholder="Type your password..."
    )
    if password:

        score, strength, feedback = check_password(password)

        # Display strength meter
        st.subheader("Strength Assessment")
        st.markdown(
            f"<h3>{strength} Password (Score: {score}/5)</h3>", unsafe_allow_html=True
        )

        st.progress(score / 5)

        # Checklist Section
        col1 = st.columns(1)
        st.markdown(f"Length > 8 chars: {'✅' if len(password) >= 8 else '❌'}")
        st.markdown(
            f"Uppercase (A-Z): {'✅' if re.search(r'[A-Z]', password) else '❌'}"
        )
        st.markdown(
            f"Lowercase (a-z): {'✅' if re.search(r'[a-z]', password) else '❌'}"
        )
        st.markdown(
            f"Number digits (1-9): {'✅' if re.search(r'[1-9]', password) else '❌'}"
        )
        st.markdown(
            f"Special Char: {'✅' if re.search(r"[!@#$%^&*]", password) else '❌'}"
        )

        # Feedback Section
        st.write("Recommendations")

        if score == 5:
            st.write("🎊 Excellent! Your password meets all criteria")
            st.balloons()
        else:
            for i in feedback:
                st.warning(i)

            st.info(
                "💡 Tip: Try combining random words with numbers and symbols (e.g., 'Blue42$Monkey')"
            )


main()
