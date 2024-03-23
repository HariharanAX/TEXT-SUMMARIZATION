from flask import Flask, render_template, request
from transformers import BertTokenizer, EncoderDecoderModel

app = Flask(__name__)

# Load the BERT2BERT model and tokenizer
model_type = 'patrickvonplaten/bert2bert-cnn_dailymail-fp16'
tokenizer = BertTokenizer.from_pretrained(model_type)
model = EncoderDecoderModel.from_pretrained(model_type)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']

    # Generate summary
    tok = tokenizer.encode("Summary:" + text, return_tensors='pt')
    summary = model.generate(tok)
    output = tokenizer.decode(summary[0])

    return render_template('index.html', text=text, summary=output)

if __name__ == '__main__':
    app.run(debug=True)
