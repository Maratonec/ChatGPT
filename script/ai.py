import os
import openai
#Setup variables
api_key = "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"
api_model = "text-davinci-003"
print("AI is running...")
#Set api key
openai.api_key = api_key
#User prompt
def requestAI(user_prompt):
  openai.api_key = api_key
  #Data
  response = openai.Completion.create(
    model=api_model,
    prompt=user_prompt,
    temperature=0.9,
    max_tokens=50,
    frequency_penalty=0.8,
    presence_penalty=0.8,
    stop=[" Human:", " AI:"]
  )
  return response["choices"][0]["text"]