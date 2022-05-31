from tensorbay import GAS
from tensorbay.dataset import Dataset as TensorBayDataset
from PIL import Image
from tensorbay.dataset import Data

gas = GAS("ACCESSKEY-e4b26b350476629bd6e9c4fae9a13db9")   
dataset = TensorBayDataset("resize_image", gas)
dataset_client = gas.get_dataset("resize_image")

segment = dataset["images"]
sample_data = segment[1]

from PIL import Image
image = Image.open(sample_data.open()).convert("RGB")
new_image = image.resize((400, 400))

new_image.save('new_image1.png')
dataset_client.create_draft("draft-2")

segment_client = dataset_client.get_segment("images") 
segment_client.upload_data(Data('new_image2.png'))
dataset_client.commit("add new")
