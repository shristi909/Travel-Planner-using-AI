import google.generativeai as palm
palm.configure(api_key="AIzaSyA7hq9nrmt923O6-F-nk5bvfxvKZyXruIM")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
}
while True:
  prompt = input("Question: ")
  response = palm.generate_text(
    **defaults,
    prompt=prompt
  )
  print("Answer:", response.result)