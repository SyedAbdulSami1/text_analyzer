import time
import streamlit as st

st.title("📜Text Analyzer🔍")
st.subheader("🧐Analyze the text you provide😊")
st.write("✏️Enter the text in the box below and click on the button to analyze the text.🔥")

with st.form("Text analzer form"):
    #1. User Input:
    user_text=st.text_area("Enter your paragraph here:", height=150)
    search_words=st.text_input("🔎Word to search:")
    replace_words=st.text_input("♻️Word to replace:")
    submitted = st.form_submit_button("Analyze Text🚀")

if submitted:
    with st.spinner("🔄 Processing... Please wait!............",show_time=True ):
        time.sleep(2)

    if not user_text:
        st.warning("✨Please enter the text to analyze.")
    else:
        words = user_text.split()
        #2. total number of words and characters and Vowel Count
        word_count = len(words)
        char_count = len(user_text)

        vowels = "aeiouAEIOU"
        get_all_vowels = ""
        for char_of_loop in user_text:
            if char_of_loop in vowels:
                get_all_vowels += char_of_loop
        vowels_count = len(get_all_vowels)
        #work of 3. Search and Replace:
        if search_words and replace_words:
            modified_text = user_text.replace(search_words, replace_words)
        elif search_words and not replace_words:
            modified_text = "✨Please enter the word to replace."
        else:
            modified_text = "✨Please enter the word to search and replace."
        #4. Uppercase and Lowercase Conversion:
        text_upper = f"🔠{user_text.upper()}"
        text_lower = f"🔡{user_text.lower()}"
        #3. Type Casting:Convert the word count and vowel count into strings.
        word_count = str(word_count)
        vowels_count = str(vowels_count)
        # 4 & 5. check paragraph contains the word "Python".
        if "python" in user_text.lower():
            contains_python = "✅ Yes"
        else:
            contains_python = "❌ No"
        #4. Operators:Use arithmetic operators to calculate the average word length (total characters / total words).
        average_word_length:float = int(char_count) / int(word_count)
        st.subheader("Analysis Results")
        col1, col2, col3, col4= st.columns(4)
        col1.metric("Total Words", f"📝{word_count}", delta=f"{type(word_count)}", border=True)
        col2.metric("Total Characters", f"🔢 {char_count}", delta=f"{type(char_count)}", border=True)
        col3.metric("Total Vowels", f"🧲{vowels_count}", delta=f"{type(vowels_count)}", border=True)
        col4.metric("Average Word Length", f"📏 {average_word_length}", delta=f"{type(average_word_length)}", border=True)
        
        st.metric(label="🐍 Contains the word Python", value=contains_python)
        st.metric(label="Modified Text", value=modified_text)
        st.metric(label="Uppercase Text", value=text_upper)
        st.metric(label="Lowercase Text", value=text_lower)
    st.success("🎉Analysis Completed🎉")
    st.write("💡 Created by **Syed Abdul Sami** 🚀")