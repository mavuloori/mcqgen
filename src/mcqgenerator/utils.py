import os
import PyPDF2
import json
import traceback


def read_file(file):
	if file.name.endswith(".pdf"):
		try:
			pdf_reader = PyPDF2.PdfFileReader(file)
			text=""
			for page in pdf_reader.pages:
				text+=page.extract_text()
			return text
		except Exception as e:
			raise Exception("Error reading the PDF file")
	elif file.name.endswith(".txt"):
		return file.read().decode("utf-8")

	else:
		raise Exception("Unsupported file format only pdf or text file supported")

def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dist = json.loads(quiz_str)
        quiz_table_data = []
        for key, value in quiz_dist.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False

# https://python.langchain.com/docs/modules/model_io/llms/token_usage_tracking

'''def generate_evaluate_chain():
#How to setup Token Usage Tracking in LangChain
    with get_openai_callback() as cb:
        response=generate_evaluate_chain(
            {
                "text": TEXT,
                "number": NUMBER,
                "subject":SUBJECT,
                "tone": TONE,
                "response_json": json.dumps(RESPONSE_JSON)
            }
            )
'''