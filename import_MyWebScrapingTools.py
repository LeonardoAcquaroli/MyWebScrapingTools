def import_MyWebScrapingTools():
  import importlib.machinery
  import requests
  # Fetch the raw content of the .py file.
  response = requests.get('https://raw.githubusercontent.com/LeonardoAcquaroli/MyWebScrapingTools/main/MyWebscrapingTools.py')
  response.raise_for_status()
  # Use importlib to import the .py file as a module.
  loader = importlib.machinery.SourceFileLoader('MyWsTools', 'MyWebscrapingTools.py')
  module = loader.load_module()
  return module
  
import_MyWebScrapingTools()
