from typing import List
from PIL import Image
from nos.client import Client

TEST_PROMPTS = ["a rabbit sitting on the grass."]

def test_mvdream():

    client = Client("[::]:50051")
    assert client is not None
    assert client.WaitForServer()
    assert client.IsHealthy()

    model_id = "mv-dream"
    models: List[str] = client.ListModels()
    assert model_id in models

    model = client.Module(model_id)
    assert model is not None
    assert model.GetModelInfo() is not None
    print(f"Test [model={model_id}]")

    response: List[Image.Image] = model(prompts=TEST_PROMPTS)
    assert isinstance(response, list)
