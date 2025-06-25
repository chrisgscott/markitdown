# MarkItDown Microservice

A Flask-based microservice that provides a REST API for converting documents to markdown using Microsoft's MarkItDown library.

## Features

- Convert various document formats (PDF, DOCX, PPTX, images, etc.) to markdown
- Base64 file input support for easy integration with n8n and other automation tools
- Health check endpoint
- Docker support for easy deployment

## API Endpoints

### POST /convert
Convert a document to markdown.

**Request Body:**
```json
{
  "file_data": "base64_encoded_file_data",
  "filename": "document.pdf"
}
```

**Response:**
```json
{
  "success": true,
  "text_content": "# Document Title\n\nConverted markdown content...",
  "title": "document.pdf",
  "metadata": {}
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

### GET /
Service information and available endpoints.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The service will be available at `http://localhost:5000`

## Docker Deployment

1. Build the image:
```bash
docker build -t markitdown-service .
```

2. Run the container:
```bash
docker run -p 5000:5000 markitdown-service
```

## Environment Variables

- `PORT`: Port to run the service on (default: 5000)

## Supported File Formats

MarkItDown supports various file formats including:
- PDF files
- Microsoft Office documents (DOCX, PPTX, XLSX)
- Images with text (PNG, JPEG, etc.)
- And more...
