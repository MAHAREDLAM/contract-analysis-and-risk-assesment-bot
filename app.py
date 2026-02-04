import streamlit as st
from utils import read_file, split_clauses
from risk_rules import analyze_risks
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

st.set_page_config(
    page_title="Contract Analysis & Risk Assessment Bot",
    layout="wide"
)

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.caption("Automated legal risk detection & reporting")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:
    text = read_file(uploaded_file)
    clauses = split_clauses(text)

    results, total_score, max_score = analyze_risks(clauses)
    risk_percentage = round((total_score / max_score) * 100, 2)

    st.subheader("📊 Overall Risk Percentage")
    st.progress(int(risk_percentage))
    st.markdown(f"### ⚠️ **{risk_percentage}% Risk Detected**")

    st.subheader("🔍 Clause-wise Risk Analysis")

    
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Contract Risk Assessment Report")

    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Total Risk Percentage: {risk_percentage}%")

    y -= 40

    for item in results:
        if y < 100:
            c.showPage()
            y = height - 50

        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, f"{item['level']} RISK")
        y -= 15

        c.setFont("Helvetica", 10)
        c.drawString(50, y, f"Clause: {item['clause'][:90]}...")
        y -= 15

        c.drawString(50, y, f"Reason: {item['reason']}")
        y -= 25

        # UI DISPLAY
        emoji = {"HIGH": "🔴", "MEDIUM": "🟠", "LOW": "🟢"}[item["level"]]
        st.markdown(
            f"""
            **{emoji} {item['level']} RISK**  
            Clause: {item['clause']}  
            Reason: {item['reason']}
            ---
            """
        )

    c.save()
    pdf_buffer.seek(0)

    st.download_button(
        label="⬇️ Download PDF Risk Report",
        data=pdf_buffer,
        file_name="contract_risk_report.pdf",
        mime="application/pdf"
    )



