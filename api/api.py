from flask import Flask, request, jsonify
from sem_search import sem_search
from PyPDF2 import PdfReader
#import openai

app = Flask(__name__)

#openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/upload_doc', methods=['POST'])
def handle_doc():
    file = request.files['file']
    if file:
        # Read PDF file
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        results = sem_search(text)
        return jsonify(results)
    else:
        return jsonify({"error": "No file provided"}), 400

"""def handle_doc():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files['file']

    # Check if no file was sent
    if file.filename == '':
        return jsonify({"error": "No file selected."}), 400

    # Read PDF content using PyMuPDF (fitz)
    try:
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        text_data = ""
        for page in pdf_document:
            text_data += page.get_text()
    except Exception as e:
        return jsonify({"error": f"Error reading the PDF file: {e}"}), 500

    # Process with sem_search
    results = sem_search(text_data)


    results = ["University of California", "Greg Durrett"]

    # work with first page only
    page = pdf_document[0]
    for page in pdf_document:
        rl = page.search_for(results, quads=True)

        # mark all found quads with one annotation
        page.add_squiggly_annot(rl)

    # save to a new PDF
    pdf_document.save("a-squiggly.pdf")
    pdf_document.close()"""

"""@app.route('/ask_openai', methods=['POST'])
def ask_openai():
    question = request.json.get('question')
    
    if not question:
        return jsonify({"error": "Question not provided"}), 400

    response = openai.Completion.create(
      engine="davinci", # choose an engine I think this is the most versatile but maybe expensive
      prompt=question, 
      max_tokens=150
    )

    return jsonify({"answer": response.choices[0].text.strip()})"""

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Image not provided'}), 400

    image = request.files['image']
    
    
    # do some processing idk lol
    
    return jsonify({'message': 'Image received and saved'})


@app.route("/", methods=["GET"])
def test_endpoint():
    return "Server is active!"


if __name__ == "__main__":
    app.run(debug=True)


# Running: `python app.py` and then in a separate terminal instance run `ngrok http 5000` to host the server from your machine
