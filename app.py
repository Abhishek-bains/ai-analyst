if uploaded_file:
    text = extract_text(uploaded_file)

    st.write("Analyzing...")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a financial analyst"},
            {"role": "user", "content": f"Summarize this report and give risks:\n{text[:5000]}"}
        ]
    )

    result = response.choices[0].message.content

    st.write(result)
