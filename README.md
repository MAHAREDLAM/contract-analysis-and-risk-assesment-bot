# Contract Analysis and Risk Assessment Bot

This project is a web-based application that analyzes legal contracts and identifies potential risks in different clauses. It helps users understand complex contract language by highlighting risky clauses and explaining them in simple terms.

## Objective

The objective of this project is to:
- Analyze legal contracts
- Identify risky clauses
- Classify risks as High, Medium, or Low
- Calculate overall contract risk percentage
- Generate a downloadable risk report

## Features

- Upload contracts (PDF, DOCX, TXT)
- Clause-wise risk detection
- Risk categorization (High / Medium / Low)
- Overall risk percentage calculation
- Clear explanation for each risk
- Downloadable PDF report
- User-friendly interface

## Technologies Used

- Python
- Streamlit
- spaCy
- pdfplumber
- python-docx
- reportlab

## How to Run the Project

1. Install Python
2. Open Command Prompt
3. Navigate to the project folder
4. Install required packages:
   pip install -r requirements.txt
5. Download spaCy model:
   python -m spacy download en_core_web_sm
6. Run the application:
   streamlit run app.py

## Use Case

This project can be used by:
- Students
- Small business owners
- Freelancers
- Beginners learning NLP and AI

## Future Enhancements

- AI-based clause analysis
- Improved UI design
- Multi-language support
- Cloud deployment

## Author

Maha Lakshmi

## Note

This project is developed for educational purposes only and should not be considered as legal advice.
