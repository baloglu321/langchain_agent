import time
import os
import requests
import asyncio
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_classic import hub
import requests

CLOUDFLARE_TUNNEL_URL = "..."
OLLAMA_MODEL_ID = "gemma3:27b"
WEATHER_API = "..."


@tool
def WeatherInfoTool(location: str) -> str:
    "Fetches weather information for a given location."
    weather_start = time.time()
    url = f"https://api.weatherstack.com/current?access_key={WEATHER_API}"
    querystring = {"query": location}
    response = requests.get(url, params=querystring)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temperature"]
    weather_description = data["current"]["weather_descriptions"][0]
    weather_stop = time.time()
    weather_time = weather_stop - weather_start
    print(f"⏱️ Çalışma Süresi (weather tool cevap süresi): {weather_time:.2f} saniye")
    return f"Weather in {location}: {weather_description}, {str(temperature)}°C"


tools = [WeatherInfoTool]


# tool_list = [weather_tool]
llm_start_time = time.time()
print(f"LLM baglantisi kuruluyor: {OLLAMA_MODEL_ID} @ {CLOUDFLARE_TUNNEL_URL}")
llm = ChatOllama(
    model=OLLAMA_MODEL_ID,
    temperature=0,
    # DİKKAT: Burada sadece base URL yeterli, '/v1' EKLEMEYİN
    base_url=CLOUDFLARE_TUNNEL_URL,
)

llm_stop_time = time.time()
llm_time = llm_stop_time - llm_start_time
print(f"⏱️ Çalışma Süresi (LLM bağlantı süresi): {llm_time:.2f} saniye")
print("LlamaIndex FunctionAgent olusturuluyor...")
prompt = hub.pull("hwchase17/react")

# --- Agent Oluşturma (ReAct Stratejisi) ---
# create_tool_calling_agent YERİNE create_react_agent kullanıyoruz.
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,  # Model format hatası yaparsa düzeltmeye çalışır
)

# --- Test ---
print("\n--- TEST BAŞLIYOR: ReAct Agent ile ---")
try:
    result = agent_executor.invoke(
        {"input": "Şu an konyada hava durumu nedir?", "chat_history": []}
    )
    print(f"\n⭐ NİHAİ CEVAP: {result['output']}\n")
except Exception as e:
    print(f"Hata: {e}")
