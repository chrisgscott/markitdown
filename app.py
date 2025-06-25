from flask import Flask, request, jsonify
from markitdown import MarkItDown
import base64
import io
import os

app = Flask(__name__)
md = MarkItDown()

@app.route('/convert', methods=['POST'])
def convert_document():
    try:
        data = request.json
        
        # Get base64 file data from n8n
        file_data_b64 = data.get('file_data')
        filename = data.get('filename', 'document.pdf')
        
        if not file_data_b64:
            return jsonify({
                'success': False,
                'error': 'file_data is required'
            }), 400
        
        # Decode base64 to binary
        file_data = base64.b64decode(file_data_b64)
        file_stream = io.BytesIO(file_data)
        
        # Extract file extension
        file_ext = '.' + filename.split('.')[-1] if '.' in filename else '.pdf'
        
        # Convert with MarkItDown
        result = md.convert_stream(file_stream, file_extension=file_ext)
        
        return jsonify({
            'success': True,
            'text_content': result.text_content,
            'title': getattr(result, 'title', filename),
            'metadata': getattr(result, 'metadata', {})
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'service': 'MarkItDown Microservice',
        'version': '1.0.0',
        'endpoints': {
            'POST /convert': 'Convert documents to markdown',
            'GET /health': 'Health check'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
