from elevenlabs import generate, play, voices
from elevenlabs import set_api_key
set_api_key("f9c97646ef9d171b94b4c22fa5c7b9be")
voices = voices()

print(voices)

audio = generate(
  text="Hi! My name is Bella, nice to meet you!",
  voice="OldIndian",
  model="eleven_monolingual_v1"
)

play(audio)
#print(audio)