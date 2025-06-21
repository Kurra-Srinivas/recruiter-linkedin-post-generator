import streamlit as st
import streamlit.components.v1 as components
from post_generator import generate_recruiter_post

st.set_page_config(page_title="Recruiter LinkedIn Post Generator", layout="centered")
st.title("🚀 Recruiter LinkedIn Post Generator")

st.markdown("Paste a job description below, and we'll turn it into a polished LinkedIn post😎🔥")

# Job Description Input
jd_input = st.text_area("📄 Job Description", height=300)

# Word/Character Counter
if jd_input:
    st.caption(f"📝 Word Count: {len(jd_input.split())} | Character Count: {len(jd_input)}")

# Tone Selector
tone = st.selectbox("🎤 Select Tone", ["Professional", "Friendly", "Excited", "Urgent"])

# Output Language Selector
language = st.selectbox("🌐 Output Language", ["English", "Hinglish", "Hindi", "French"])

# Generate Button
if st.button("✨ Generate Post"):
    if jd_input.strip() == "":
        st.error("⚠️ Please paste a job description.")
    else:
        with st.spinner("Generating with a touch of ✨ and emojis..."):
            post_text = generate_recruiter_post(jd_input, tone=tone, language=language).strip()

            # Split hashtags from body if included
            split_text = post_text.split("#")
            main_text = split_text[0].strip()
            hashtags = "#" + "#".join(split_text[1:]).replace("\n", " ").strip() if len(split_text) > 1 else ""

            # Display the post in clean markdown
            st.markdown("### 💼 Generated LinkedIn Post")
            st.markdown(main_text)

            if hashtags:
                st.markdown(f"**{hashtags}**", unsafe_allow_html=True)

            # Save as text file
            st.download_button(
                label="💾 Save Post as .txt",
                data=post_text,
                file_name="linkedin_post.txt",
                mime="text/plain"
            )

            # Hidden textarea for clipboard copy
            components.html(f"""
                <textarea id=\"copyText\" style=\"display:none;\">{post_text}</textarea>
                <button onclick=\"copyText()\" style=\"
                    background-color:#0072b1;
                    color:white;
                    padding:10px 16px;
                    font-size:14px;
                    border:none;
                    border-radius:8px;
                    cursor:pointer;
                    margin-top:10px;\">
                    📋 Copy to Clipboard
                </button>

                <script>
                function copyText() {{
                    var textArea = document.getElementById('copyText');
                    textArea.style.display = 'block';
                    textArea.select();
                    document.execCommand('copy');
                    textArea.style.display = 'none';
                    alert('✅ Post copied to clipboard!');
                }}
                </script>
            """, height=100)

        st.caption("💡 Tip: Paste a different JD to regenerate a new post anytime!")
