from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'pdf_doc' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['pdf_doc']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.pdf'):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Process the file here (you can add your resume parsing logic)
        return jsonify({'message': f'File {filename} uploaded and processed successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file type. Please upload a PDF.'}), 400

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    # Here you would typically process the message and generate a response
    # For this example, we'll just echo the message back
    response = f"You said: {message}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)