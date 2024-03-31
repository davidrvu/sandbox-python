# DAVIDRVU - 2023_12_18

import os
import openai

openai.api_key = os.getenv("ENV_OPENAI_API_KEY")

user_prompt = "Male model with a gray graphite shirt of brand ferouch"
print("user_prompt = " + str(user_prompt))

response = openai.Image.create(
	prompt = user_prompt,
	n=1,
	size="1024x1024",
)

image_url = response.data[0].url
