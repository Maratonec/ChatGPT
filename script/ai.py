import os
import openai
#Setup variables
backup_api_key = "nomne"
api_model = "text-davinci-003"
print("AI is running...")
#Set api key
openai.api_key = backup_api_key
#User prompt
def requestAI(user_prompt, api_key, api_limit):
  openai.api_key = api_key
  print(user_prompt)
  print(api_key)
  #Data
  response = openai.Completion.create(
    model=api_model,
    prompt=user_prompt,
    temperature=0.9,
    max_tokens=api_limit,
    frequency_penalty=0.8,
    presence_penalty=0.8,
    stop=[" Human:", " AI:"]
  )
  return response["choices"][0]["text"]