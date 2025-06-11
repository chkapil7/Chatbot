import google.generativeai as genai
genai.configure(api_key="AIzaSyBwXhkUedmEENI_Vkq4r8rj4gtfebpEMlsAIzaSyBwXhkUedmEENI_Vkq4r8rj4gtfebpEMls")

for m in genai.list_models():
    print(m.name)
