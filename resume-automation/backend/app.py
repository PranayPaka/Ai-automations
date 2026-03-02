from flask import Flask, request, jsonify
import json
from analyzer import extract_text, analyze_resume

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON received"}), 400

        pdf_path = data.get("pdfPath")
        job_description = data.get("jobDescription")

        if not pdf_path or not job_description:
            return jsonify({"error": "Missing pdfPath or jobDescription"}), 400

        # Extract resume text
        resume_text = extract_text(pdf_path)

        # Analyze against job description
        result = analyze_resume(resume_text, job_description)

        # Convert returned JSON string into actual JSON response
        return jsonify(json.loads(result))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)