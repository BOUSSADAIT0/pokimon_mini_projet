# code effectue un stress test en envoyant 1000 requêtes asynchrones à chaque URL dans URLS.
# L'objectif est de tester les performances et la capacité d'un serveur à gérer une charge élevée.




import asyncio
import aiohttp

URLS = [
    "https://api.example.com/data1",
    "https://api.example.com/data2",
    "https://api.example.com/data3"
]

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()





async def stress_test():
    async with aiohttp.ClientSession() as session: # Crée une session HTTP asynchrone avec aiohttp.ClientSession().
        tasks = [fetch(url, session) for url in URLS * 1000]  # 1000 requêtes
        results = await asyncio.gather(*tasks) #  pour exécuter toutes les requêtes en parallèle.

        print(f"Nombre de réponses: {len(results)}")

asyncio.run(stress_test())
