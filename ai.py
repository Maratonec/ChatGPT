import os
import openai
import discord
#Setup variables
api_key = "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"
api_model = "text-davinci-003"

#Set api key
openai.api_key = api_key
#User prompt and welcome message
print("Type your prompt for ChatGPT:")
get_prompt = input()

#Data
response = openai.Completion.create(
  model=api_model,
  prompt=get_prompt,
  temperature=0.9,
  max_tokens=50,
  frequency_penalty=0.8,
  presence_penalty=0.8,
  stop=[" Human:", " AI:"]
)

#Print response
print(response["choices"][0]["text"])