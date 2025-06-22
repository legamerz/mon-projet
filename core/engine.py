import importlib

def run_module(name):
    try:
        mod = importlib.import_module(f"modules.{name}")
        mod.run()
    except Exception as e:
        print(f"❌ Erreur : {e}")
