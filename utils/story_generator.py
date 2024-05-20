from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_story(captions):
    prompt = " ".join(captions)
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=500, num_return_sequences=1)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story
